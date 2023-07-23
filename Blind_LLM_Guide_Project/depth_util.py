import torch 
import numpy as np

from DPT_module.dpt.models import DPTDepthModel
from DPT_module.dpt.midas_net import MidasNet_large
from DPT_module.dpt.transforms import Resize, NormalizeImage, PrepareForNet
import DPT_module.util.io as DPT_io
from torchvision.transforms import Compose

DEBUG = False

def predict_depth(image_path, output_path, model_path="DPT_module/weights/dpt_large-midas-2f21e586.pt", model_type="dpt_large", optimize=True):
    """
    Predict the depth map of a single image using DPT model.

    Args:
        img (ndarray): Input image.
        model_path (str): Path to the model weights.
        model_type (str): Type of the DPT model to use.

    Returns:
        prediction (ndarray): The predicted depth map.
    """
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if DEBUG:
        print("initialize")
        print("device: %s" % device)
    # load network
    if model_type == "dpt_large":
        model = DPTDepthModel(
            path=model_path,
            backbone="vitl16_384",
            non_negative=True,
            enable_attention_hooks=False,
        )
        normalization = NormalizeImage(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    else:
        raise ValueError("Unsupported model type. Please use 'dpt_large'.")

    net_w = net_h = 384

    transform = Compose(
        [
            Resize(
                net_w,
                net_h,
                resize_target=None,
                keep_aspect_ratio=True,
                ensure_multiple_of=32,
                resize_method="minimal",
                image_interpolation_method=cv2.INTER_CUBIC,
            ),
            normalization,
            PrepareForNet(),
        ]
    )

    model.eval()

    if optimize == True and device == torch.device("cuda"):
        model = model.to(memory_format=torch.channels_last)
        model = model.half()

    model.to(device)

    # transform input
    img = DPT_io.read_image(image_path)
    img_input = transform({"image": img})["image"]
    # print("img.shape is",  img.shape)
    # compute depth map
    with torch.no_grad():
        sample = torch.from_numpy(img_input).to(device).unsqueeze(0)

        if optimize == True and device == torch.device("cuda"):
            sample = sample.to(memory_format=torch.channels_last)
            sample = sample.half()

        prediction = model.forward(sample)
        prediction = (
            torch.nn.functional.interpolate(
                prediction.unsqueeze(1),
                size=img.shape[:2],
                mode="bicubic",
                align_corners=False,
            )
            .squeeze()
            .cpu()
            .numpy()
        )
    # DPT_io.write_depth(output_path, prediction, bits=2)
    
    # print("finished")
    return prediction

def get_distance_category(depth_map, person_mask):
    # Define depth categories
    categories = ['very close', 'close', 'medium', 'far', 'very far']


    # Find the lowest true point in mask A 
    y_coords, _ = np.nonzero(person_mask)
    lowest_point = int(np.max(y_coords) * 0.9 )#(huamn feet point)
    # print(y_coords, lowest_point)
    mask_a_copy = person_mask.copy().astype(bool)
    # Slice mask A from the lowest point to the top
    mask_a_copy[:lowest_point, :] = False
    obj_depths = depth_map[mask_a_copy]
      # Handle case where no depth value is available
    if obj_depths.size == 0:
        return "unknown"
    feet_depth = np.median(obj_depths)


    # Compute depth range of the image
    min_depth, max_depth = np.min(depth_map), np.max(depth_map)

    # Compute boundaries for each category
    boundaries = np.linspace(min_depth, max_depth, len(categories) + 1)

    # Find which category the median depth of the object belongs to
    for i in range(len(boundaries) - 1):
        if boundaries[i] <= feet_depth < boundaries[i + 1]:
            return categories[i]

    return categories[-1]  # If for some reason it wasn't caught in the loop