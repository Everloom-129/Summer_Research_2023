# Readme

the data file is too large, if anyone is interested in the generated product, download the source file from JAAD and run the script plz.

## video classification

### task:

 based on your understanding of JAAD api, classify the video clip data set into three folder: 

- long, median and short
- 



From the list of functions you provided, it appears that the code for JAAD (Joint Attention in Autonomous Driving) dataset handling can be roughly divided into several key areas:

1. Initialization and Setup: 
   - `__init__`: Initializes the JAAD object, sets paths, and determines if the existing database should be regenerated.

2. Path Helpers: 
   - `cache_path`: Returns or creates a cache directory for storing temporary data.
   - `_get_default_path`: Returns the default path where jaad_raw files are expected to be placed.
   - `_get_video_ids_split`: Returns a list of video ids for a given data split (train, test, validation).
   - `_get_video_ids`: Returns a list of all video ids in the dataset.
   - `_get_image_path`: Generates the path to a given image using its video and frame ids.

3. Visualization Helpers:
   - `update_progress`: Creates a progress bar to track the progress of a running process.
   - `_print_dict`: Prints a dictionary, making it easier to visualize key-value pairs.

4. Image Processing:
   - `_squarify`: Changes the ratio of bounding boxes to a fixed ratio.
   - `extract_and_save_images`: Extracts images from video clips and saves them on drive.

5. Annotation Handling:
   - `_get_annotations`: Gets pedestrian annotations for a given video.
   - `_get_ped_attributes`: Gets pedestrian attributes for a given video.
   - `_get_ped_appearance`: Gets pedestrian appearance for a given video.
   - `_get_traffic_attributes`: Gets traffic attributes for a given video.
   - `_get_vehicle_attributes`: Gets vehicle attributes for a given video.

6. Database Generation and Management:
   - `generate_database`: Generates a database of all annotations in the form of a dictionary and saves it as a .pkl file in the cache directory.
   - `get_data_stats`: Gets statistics of the data.
   - `balance_samples_count`: Balances the samples count in the dataset.

7. Pedestrian ID Handling:
   - `_get_pedestrian_ids`: Returns pedestrian ids based on the sample type.
   - `_get_random_pedestrian_ids`: Returns random pedestrian ids for train/test (or validation) subsets.
   - `_get_kfold_pedestrian_ids`: Returns k-fold split pedestrian ids for cross-validation.

8. Data Generation for Different Models:
   - `_get_data_frcnn`: Gets data for Faster R-CNN model.
   - `_generate_csv_data_retinanet`: Generates csv data for RetinaNet model.
   - `_generate_csv_data_yolo3`: Generates csv data for YOLOv3 model.
   - `_generate_csv_data_ssd`: Generates csv data for SSD model.

9. Data Processing:
   - `_get_data_ids`: Gets data ids for a given image set and parameters.
   - `_height_check`: Checks if pedestrian scale is within the defined range.
   - `_get_center`: Gets the center of a bounding box.

10. Sequence Analysis:
    - `generate_data_trajectory_sequence`: Generates sequence data for trajectories, intentions, and crossings.
    - `_get_trajectories`: Gets trajectories for a given image set and annotations.
    - `_get_crossing`: Gets crossing data for a given image set and annotations.
    - `_get_intention`: Gets intention data for a given image set and annotations.

This structure reflects the complexity of processing and annotating video data for autonomous driving systems, with a focus on pedestrian interactions. Each of these function categories has a clear role in the processing and annotation pipeline, from extracting frames and adjusting bounding boxes to generating data for different detection models and handling data split for cross-validation.

