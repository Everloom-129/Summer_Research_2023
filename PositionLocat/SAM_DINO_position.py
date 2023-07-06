import os
import cv2
# filter some annoying debug info
import warnings
warnings.filterwarnings('ignore')

import torch
import torchvision
import supervision as sv

import numpy as np
from PIL import Image
from pathlib import Path

import termcolor
import matplotlib.pyplot as plt

from groundingdino.util.inference import Model
from segment_anything import sam_model_registry, SamPredictor
#TODO name!
from groundingdino.util.inference import load_model, load_image, predict, annotate

import SAM_utility

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# Paths to GroundingDINO and SAM checkpoints
GROUNDING_DINO_CONFIG_PATH = "/root/autodl-tmp/DINO/groundingdino/config/GroundingDINO_SwinT_OGC.py"
GROUNDING_DINO_CHECKPOINT_PATH = "/root/autodl-tmp/DINO/weights/groundingdino_swint_ogc.pth"
model_type = "default"
SAM_CHECKPOINT_PATH = "/root/autodl-tmp/sam_vit_h_4b8939.pth"

# Predict classes and hyper-param for GroundingDINO
BOX_TRESHOLD = 0.25
TEXT_TRESHOLD = 0.25
NMS_THRESHOLD = 0.8

# Initialize GroundingDINO model
grounding_dino_model = Model(
    model_config_path=GROUNDING_DINO_CONFIG_PATH, 
    model_checkpoint_path=GROUNDING_DINO_CHECKPOINT_PATH, 
    device=DEVICE
)

# Initialize SAM model and predictor
sam = sam_model_registry[model_type](checkpoint=SAM_CHECKPOINT_PATH)
sam.to(device=DEVICE)
sam_predictor = SamPredictor(sam)


# Prompting SAM with ROI
def segment_ROI(sam_predictor: SamPredictor, image: np.ndarray, xyxy: np.ndarray):
    sam_predictor.set_image(image)
    result_masks = []
    for box in xyxy:
        masks_np, scores_np, _ = sam_predictor.predict(
        point_coords=None,
        point_labels=None,
        box= box,
        multimask_output=True,
        )
        index = np.argmax(scores_np)
        result_masks.append(masks_np[index])

    return np.array(result_masks)

def detect_road(image_path,output_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            print(f"Image at path {image_path} could not be loaded. Skipping.")
            return None
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


        image_source, image2 = load_image(image_path)
    except Exception as e:
        print(f"Failed to process image at {image_path}. Error: {e}")
        return None
    
    TEXT_PROMPT = "road . sidewalk"
    CLASSES = ['road', 'sidewalk']
    

    # detect objects
    detections = grounding_dino_model.predict_with_classes(
        image=image,
        classes = CLASSES,
        box_threshold= BOX_TRESHOLD,
        text_threshold=TEXT_TRESHOLD
    )

    box_annotator = sv.BoxAnnotator()

    labels = [
    f"{CLASSES[class_id]} {confidence:0.2f}" 
    for _, _, confidence, class_id, _ 
    in detections]
    
    # NMS post process
    nms_idx = torchvision.ops.nms(
        torch.from_numpy(detections.xyxy), 
        torch.from_numpy(detections.confidence), 
        NMS_THRESHOLD
    ).numpy().tolist()

    detections.xyxy = detections.xyxy[nms_idx]
    detections.confidence = detections.confidence[nms_idx]
    detections.class_id = detections.class_id[nms_idx]


    annotated_frame = box_annotator.annotate(scene=image.copy(), detections=detections.copy(), labels=labels)
    # sv.plot_image(annotated_frame, (16, 16))


    # cv2.imwrite("annotated_image.jpg", annotated_frame)
    


    DINO_boxes = np.array(detections.xyxy)


    SAM_masks = segment_ROI(
        sam_predictor=sam_predictor,
        image= image,
        xyxy= DINO_boxes,
    )

    plt.figure(figsize=(16,9))

    # Display the original image
    plt.imshow(image)
    plt.axis('off')


    for mask in SAM_masks:
        SAM_utility.show_mask(mask, plt.gca(), random_color=True)
    for box in DINO_boxes:
        SAM_utility.show_box(box, plt.gca())

    plt.savefig(output_path)
    plt.close()


    return DINO_boxes,labels

def main():
    image_dir = Path("input")
    output_dir = Path('DINOmasked')
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Start =====")
    i = 1
    # for filename in os.listdir(image_dir):
    #     if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
    #         image_path = os.path.join(image_dir, filename)
    #         output_path = os.path.join(output_dir, filename)
    #         if not os.path.exists(output_path):
    #             print("Processing: ", i)
    #             i += 1 # improve this in more elegant way
    #             print(f"Image path: {termcolor.colored(os.path.basename(image_path), 'green')}")
    #             result = detect_road(image_path)
    #             print(f"Detected: {termcolor.colored(result, 'blue')}")

    # Use rglob to recursively find all image files
    for image_path in image_dir.rglob('*'):
        if SAM_utility.is_image_file(str(image_path)):
            relative_path = image_path.relative_to(image_dir)

            output_path = output_dir / relative_path
            output_path.parent.mkdir(parents=True,exist_ok=True)

            if not output_path.exists():
                print("Processing: ", i)
                i += 1
                print(f"Image path: {termcolor.colored(os.path.basename(str(image_path)), 'green')}")
                result = detect_road(str(image_path),str(output_path))
                if result is not None:
                    print(f"Detected: {termcolor.colored(result, 'blue')}")
                else:
                    fail_str = "failed to detect result"
                    print(f" {termcolor.colored(fail_str, 'blue')}")



if __name__ == "__main__":
    # text program to make sure the label works
    # DINO_boxes,labels = detect_road("input/scene_2.png")
    # print(DINO_boxes, labels)   
    '''
    [[  1.7368164 187.55162   893.4925    430.34235  ]
    [351.7953    195.08667   893.7616    429.8313   ]] ['road 0.50', 'sidewalk 0.31']
    '''
    main()