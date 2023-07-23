# # Semantic Segment Road and Sidewalk
# Tony Wang July 04 2023
# 
# After semantic segmentation of road and sidewalk, we obtain the pixel level binary mask of them. Which can be used to detect human-road relationship using rule-based comparision. Since the SAM didn't provide necessary api, I write some utility func to realize it
# 
# > This notebook is used for tutuorial demo, because I believe, compared to the unstable .py file, jupyter notebook would provide a vivid description and data pipeline demonstration.


# ## Library & Model Loading


import os
import cv2
# filter some annoying debug info
# import warnings
# warnings.filterwarnings('ignore')

import torch
import torchvision
import supervision as sv

import numpy as np
from PIL import Image
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt

from groundingdino.util.inference import Model
from segment_anything import sam_model_registry, SamPredictor
from groundingdino.util.inference import load_model, load_image, predict, annotate

from depth_util import predict_depth,get_distance_category
from mask_util  import show_mask,show_points,show_box,display_mask,nms_processing,is_overlap,compute_overlap,get_location,get_surface_info
from file_io    import is_image_file
from angle_util import describe_angle,estimate_angle
# import SAM_utility # 

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# Paths to GroundingDINO and SAM checkpoints
GROUNDING_DINO_CONFIG_PATH = "../GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py"
GROUNDING_DINO_CHECKPOINT_PATH = "./weights/groundingdino_swint_ogc.pth"
MODEL_TYPE = "vit_b"
SAM_CHECKPOINT_PATH = "./weights/sam_vit_b_01ec64.pth"

# Predict classes and hyper-param for GroundingDINO
BOX_TRESHOLD = 0.25
TEXT_TRESHOLD = 0.25
PED_TRESHOLD = 0.5

IOU_THRESHOLD = 0.5

DEBUG = True

# Initialize GroundingDINO model
grounding_dino_model = Model(
    model_config_path=GROUNDING_DINO_CONFIG_PATH, 
    model_checkpoint_path=GROUNDING_DINO_CHECKPOINT_PATH, 
    device=DEVICE
)

# Initialize SAM model and predictor
sam = sam_model_registry[MODEL_TYPE](checkpoint=SAM_CHECKPOINT_PATH)
sam.to(device=DEVICE)
sam_predictor = SamPredictor(sam)

# # Data structure
# LocationInfo: pack form to help data-alignment

class LocationInfo:
    def __init__(self, object_type, id, box, mask,confidence):
        self.object_type = object_type  # ('sidewalk', 'road', or 'person')
        self.id = id  # Unique ID within the type
        self.box = box  # Bounding box in xyxy format
        self.mask = mask  # Binary mask indicating the precise location of the object
        self.confidence = confidence #confidence of bbox
        self.distance = None # str,{very close,close, median, far, very far}
        self.angle = None    # horizontal angle relative to camera
    def get_area(self):
        """
        int: The area of the object in pixels.
        """
        return np.sum(self.mask)


def obj_print(obj_dict,image):
    for name, person in obj_dict.items():
        print(name)
        print(person.box)
        print(person.distance)
        person.angle = estimate_angle(image,person)

        print(f"angle is {person.angle},it is {describe_angle(person.angle)}")
        print("\n\n")

def write_to_txt(image_path, output_path, p_surface_overlaps, counts, labels, p_labels,obj_dict):
    '''
    str image_path: the relative path to input image
    str output_path: "DINOmasked/video_0018/man.png"
    
    
    '''
    output_dir = Path(output_path).parent
    img_name = image_path[-8:-4]
    txt_name = "Info_Video_"+ str(output_dir)[-4:] +".txt"
    txt_path = os.path.join(output_dir, txt_name) 

    if DEBUG:
        print("output_dir: ", output_dir)
        print("image_name: ", img_name)
        print("txt_path: ", txt_path)
    # Check if file already exists
    if DEBUG:
        if os.path.exists(txt_path):
            # Read in existing data
            with open(txt_path, 'r') as f:
                existing_data = f.read()

            # If the info of the current image has already been recorded, return without appending
            if f"INFO of {img_name}:\n" in existing_data:
                print(f"ERROR: the info of{img_name} has been generated")
                return
    with open(txt_path, 'a') as f: # 'a' option is for appending to the file if it exists
        f.write(f"INFO of {img_name}:\n")

        get_surface_info(obj_dict,f)
        
        for person, surfaces in p_surface_overlaps:
            if surfaces:
                surface_str = ', '.join([f"{surface.object_type} {surface.id}" for surface in surfaces])
                f.write(f"Person {person.id} is on the {surface_str}\n")
            else:
                f.write(f"Person {person.id} is not on any detected surface\n")
                
        f.write(f"number of Surface mask, Road&sidewalk, People 's mask, actural people: {counts}\n")
        f.write(f"Labels: [{', '.join(labels)}]\n")
        f.write(f"Person Labels: [{', '.join(p_labels)}]\n\n")


# ## Key Function

# Prompting SAM with Region of Interest
def segment_ROI(sam_predictor: SamPredictor, image: np.ndarray, boxes: np.ndarray):

    sam_predictor.set_image(image)
    result_masks = []
    for box in boxes:
        masks_np, iou_predictions, _ = sam_predictor.predict(
        point_coords=None,
        point_labels=None,
        box=box,
        multimask_output=True,
        )
        #TODO Remove the following line to get all the person masks
        # index = np.argmax(scores_np) 
        # Add all masks to the result, not just the one with the highest score
        # Filter out masks with IoU scores below the threshold
        for mask, score in zip(masks_np, iou_predictions):
            if score >= IOU_THRESHOLD:
                result_masks.append(mask)

    return np.array(result_masks)

def detect_road(image_path,output_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            print(f"Image at path {image_path} could not be loaded. Skipping.")
            return None
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    except Exception as e:
        print(f"Failed to process image at {image_path}. Error: {e}")
        return None
    
    ROAD_SIDEWALK = ['road', 'sidewalk'] 
    P_CLASS     = ['person'] #,'bike']
    # the person label lower gDINO's performance
    # so I split them

    # detect road and sidewalk
    detections = grounding_dino_model.predict_with_classes(
        image=image,
        classes = ROAD_SIDEWALK,
        box_threshold= BOX_TRESHOLD,
        text_threshold=TEXT_TRESHOLD
    )
    detections = nms_processing(detections)
    # detect person 
    p_detections = grounding_dino_model.predict_with_classes(
        image = image,
        classes = P_CLASS , 
        box_threshold= BOX_TRESHOLD,
        text_threshold=PED_TRESHOLD - 0.3
    )
    p_detections = nms_processing(p_detections)

    box_annotator = sv.BoxAnnotator()
    person_annotator = sv.BoxAnnotator()

    labels = [
        f"{ROAD_SIDEWALK[class_id]} {i} {confidence:0.2f}" 
        for i, (_, _, confidence, class_id, _) in enumerate(detections)]

    P_labels = [
        f"{P_CLASS[class_id]} {i} {confidence:0.2f}" 
        for i, (_, _, confidence, class_id, _) in enumerate(p_detections)]

    DINO_boxes = np.array(detections.xyxy)
    P_boxes    = np.array(p_detections.xyxy)
    
    annotated_frame = box_annotator.annotate(scene=image.copy(), detections=detections ,labels=labels)
    if DEBUG:
        sv.plot_image(annotated_frame, (16, 16))
    person_annotation = person_annotator.annotate(scene=annotated_frame,detections= p_detections,labels= P_labels)
    if DEBUG:
        sv.plot_image(person_annotation, (16, 16))
    # cv2.imwrite("annotated_image.jpg", annotated_frame)
    
    SAM_masks = segment_ROI(sam_predictor,image,DINO_boxes)
    P_masks = segment_ROI(sam_predictor,image,DINO_boxes)

    # Create a list of LocationInfo objects for each detected object
    obj_dict = Counter()
    
    for i, (box, label, mask) in enumerate(zip(DINO_boxes, labels, SAM_masks)):
        object_type, id, confidence   = label.split(' ')
        index = object_type +id
        obj_dict[index] =  (LocationInfo(object_type, int(id), box, mask,confidence)) 

    for i, (box, label, mask) in enumerate(zip(P_boxes, P_labels, P_masks)):
        object_type, id, confidence = label.split(' ')
        index = object_type+id
        obj_dict[index] = (LocationInfo(object_type, int(id), box, mask,confidence)) 

    depth_map = predict_depth(image_path,output_path)
    
    # Analyze where each person is standing
    p_surface_overlaps = []
    
    for name, person in obj_dict.items():
        if person.object_type != "person":
            continue # We only want to analyze persons
        person.distance = get_distance_category(depth_map,person.mask)
        person.angle   = estimate_angle(image,person)
        
        overlaps = []
        for name, surface in obj_dict.items():
            # We only want to analyze surfaces (road or sidewalk)
            if surface.object_type not in ROAD_SIDEWALK: 
                continue

            # Check if the person and the surface overlap
            overlap, _ = is_overlap(person.mask, surface.mask)
            if overlap:
                overlaps.append(surface)

        p_surface_overlaps.append((person, overlaps))


    if DEBUG:
        # Print out the analysis results
        for person, surfaces in p_surface_overlaps:
            if surfaces:
                surface_str = ', '.join([f"{surface.object_type} {surface.id}" for surface in surfaces])
                print(f"Person {person.id} is on the {surface_str}")
            else:
                print(f"Person {person.id} is not on any detected surface")

    (i, j, k, d) = display_mask(SAM_masks,P_masks,P_boxes,DINO_boxes,person_annotation,output_path)
    

    write_to_txt(image_path, output_path, p_surface_overlaps, (i, j, k, d), labels, P_labels,obj_dict)

    plt.close()
    
    return obj_dict,image

# ## Main Function

# 21]:
def main():
    input_dir = Path("input") # contain many folders  JAAD_seg_by_sec
    output_dir = Path('DINOmasked')
    output_dir.mkdir(parents=True, exist_ok=True)

    print("===== Start =====")
    i = 1
    # Use rglob to recursively find all image files
    for image_path in input_dir.rglob('*'):
        if is_image_file(str(image_path)):
            relative_path = image_path.relative_to(input_dir)

            output_path = output_dir / relative_path
            output_path.parent.mkdir(parents=True,exist_ok=True)

            if output_path.exists():
                print(f"Already scanned {output_path}, next one")
                continue
            else:
                print("Processing: ", i)
                i += 1
                print(f"Image path: {os.path.basename(str(image_path))}")

                result = detect_road(str(image_path),str(output_path))

                if result is not None:
                    print(f"Detected: {image_path}") 
                else: 
                    print( "failed to detect result")

    print("===== END =====")

if __name__ == "__main__":
    main()