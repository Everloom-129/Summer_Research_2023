
import numpy as np
import matplotlib.pyplot as plt
import torch
import torchvision
import supervision as sv
NMS_THRESHOLD = 0.85

DEBUG = 0
# ## Utility Function
def show_mask(mask, ax, random_color=False):
    '''Display single mask to its image'''
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([30/255, 144/255, 255/255, 0.6])
    h, w = mask.shape[-2:] # more robust way of extracting the spatial dimensions of the array
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)
    
def show_points(coords, labels, ax, marker_size=375):
    pos_points = coords[labels==1]
    neg_points = coords[labels==0]
    ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)
    ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)   
    
def show_box(box, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0,0,0,0), lw=2))    

def display_mask(SAM_masks,P_masks, P_boxes, DINO_boxes,  person_annotation,output_path):
    # Create a new subplot
    plt.figure(figsize=(16,9))
    # image = cv2.cvtColor( cv2.imread(image_path),cv2.COLOR_BGR2RGB )
    # Display the original image
    plt.axis('off')
 
    plt.imshow(person_annotation)
    i,j,k,d = 0,0,0,0
    for mask in SAM_masks:
        i += 1
        show_mask(mask, plt.gca(), random_color=True)
    for box in DINO_boxes:
        j += 1
        show_box(box, plt.gca())
    for mask in P_masks:
        k += 1
        show_mask(mask, plt.gca(), random_color=True)
    for box in P_boxes:
        d += 1
        show_box(box,plt.gca())
    if DEBUG:
        print("number of Surface mask, Road&sidewalk, People 's mask, actural people: ",i,j,k,d)

    plt.savefig(output_path)
    plt.close()
    return (i, j, k, d)

def nms_processing(detections ):
    """
    Non-Maximum Suppression (NMS) on detection results to eliminate overlapping bounding boxes.
    
    Args:
        detections (Detection): 
        - 'xyxy' (bounding box coordinates),
        - 'confidence' (confidence scores), 
        - 'class_id' (class IDs).
        
        nms_threshold (float): The threshold for the IOU (Intersection Over Union). Bounding boxes with IOU values greater than this 
        threshold will be suppressed.
    
    Returns:
        detections: The updated detections after performing NMS. 
    """
    nms_idx = torchvision.ops.nms(
        torch.from_numpy(detections.xyxy), 
        torch.from_numpy(detections.confidence), 
        NMS_THRESHOLD 
    ).numpy().tolist()

    detections.xyxy = detections.xyxy[nms_idx]
    detections.confidence = detections.confidence[nms_idx]
    detections.class_id = detections.class_id[nms_idx]
    return detections

def is_overlap(mask_a: np.ndarray, mask_b: np.ndarray):
    """
    Check if the bottom part of mask_a overlaps with mask_b.
    
    Args:
        mask_a: numpy array of shape (H, W). Binary mask of object A.
        mask_b: numpy array of shape (H, W). Binary mask of object B.

    Returns:
        bool. True if there is overlap, False otherwise.
    """
    
    # Check the inputs are binary masks
    assert mask_a.shape == mask_b.shape, "Both masks should have the same shape."
    assert np.logical_or(mask_a == 0, mask_a == 1).all(), "Mask A should be a binary mask."
    assert np.logical_or(mask_b == 0, mask_b == 1).all(), "Mask B should be a binary mask."

    # Find the lowest true point in mask A 
    y_coords, _ = np.nonzero(mask_a)
    lowest_point = int(np.max(y_coords) * 0.9 )#(huamn feet point)

    mask_a_copy = mask_a.copy()
    # Slice mask A from the lowest point to the top
    mask_a_copy[:lowest_point, :] = 0

    # Check for overlap
    overlap = np.logical_and(mask_a_copy, mask_b)

    return np.any(overlap), lowest_point

def compute_overlap(mask_a: np.ndarray, mask_b: np.ndarray):
    """
    Compute the percentage of mutual coverage between mask_a and mask_b.
    
    Args:
        mask_a: numpy array of shape (H, W). Binary mask of object A.
        mask_b: numpy array of shape (H, W). Binary mask of object B.

    Returns:
        float. The percentage of mutual coverage.
    """
    # Check the inputs are binary masks
    assert mask_a.shape == mask_b.shape, "Both masks should have the same shape."
    assert np.logical_or(mask_a == 0, mask_a == 1).all(), "Mask A should be a binary mask."
    assert np.logical_or(mask_b == 0, mask_b == 1).all(), "Mask B should be a binary mask."

    # Compute the intersection between the two masks
    intersection = np.logical_and(mask_a, mask_b)
    
    # Compute the union of the two masks
    union = np.logical_or(mask_a, mask_b)

    # Calculate the mutual coverage percentage
    overlap_percentage = np.sum(intersection) / np.sum(union)

    return overlap_percentage

# Surface Utility Function
def get_location(bbox:np.ndarray, img_shape:np.ndarray):
    img_height, img_width = img_shape[:2]
    x_center = (bbox[0] + bbox[2]) / 2
    y_center = (bbox[1] + bbox[3]) / 2

    if x_center < img_width / 3:
        x_pos = "left"
    elif x_center < 2 * img_width / 3:
        x_pos = "middle"
    else:
        x_pos = "right"

    if y_center < img_height / 2:
        y_pos = "up"
    else:
        y_pos = "down"

    return f"{x_pos}_{y_pos}"

def get_surface_info(obj_dict , f):
    
    for key, obj_info in obj_dict.items():
        object_type = obj_info.object_type
        id = obj_info.id
        bbox = obj_info.box
        h, w = obj_info.mask.shape[-2:]
        location = get_location(bbox, (h, w)) 
        if DEBUG:
            print(f"{object_type} {id} is at {location}")
        f.write(f"{object_type} {id} is at {location}\n")
        if obj_info.object_type == "person":
            f.write(f"The [distance,angle] from {object_type} {id} to our dashcam is: [{obj_info.distance},{obj_info.angle}]\n")
            if DEBUG:
                print(f"The [distance,angle] from {object_type} {id} to our dashcam is: [{obj_info.distance},{obj_info.angle}]\n")
