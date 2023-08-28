
import os
import sys
import numpy as np
from typing import List


import ultralytics
import yolox
import supervision


from yolox.tracker.byte_tracker import BYTETracker, STrack
from onemetric.cv.utils.iou import box_iou_batch
from dataclasses import dataclass

from pathlib import Path
from ultralytics import YOLO

SOURCE_VIDEO_PATH = "videos/bdd/b1c9c847-3bda4659.mov"



@dataclass(frozen=True)
class BYTETrackerArgs:
    track_thresh: float = 0.25
    track_buffer: int = 30
    match_thresh: float = 0.8
    aspect_ratio_thresh: float = 3.0
    min_box_area: float = 1.0
    mot20: bool = False


from supervision.draw.color import ColorPalette
from supervision.geometry.dataclasses import Point
from supervision.video.dataclasses import VideoInfo
from supervision.video.source import get_video_frames_generator
from supervision.video.sink import VideoSink
from supervision.notebook.utils import show_frame_in_notebook
from supervision.tools.detections import Detections, BoxAnnotator


# converts Detections into format that can be consumed by match_detections_with_tracks function
def detections2boxes(detections: Detections) -> np.ndarray:
    return np.hstack((
        detections.xyxy,
        detections.confidence[:, np.newaxis]
    ))


# converts List[STrack] into format that can be consumed by match_detections_with_tracks function
def tracks2boxes(tracks: List[STrack]) -> np.ndarray:
    return np.array([
        track.tlbr
        for track
        in tracks
    ], dtype=float)


# matches our bounding boxes with predictions
def match_detections_with_tracks(
    detections: Detections,
    tracks: List[STrack]
) -> Detections:
    if not np.any(detections.xyxy) or len(tracks) == 0:
        return np.empty((0,))

    tracks_boxes = tracks2boxes(tracks=tracks)
    iou = box_iou_batch(tracks_boxes, detections.xyxy)
    track2detection = np.argmax(iou, axis=1)

    tracker_ids = [None] * len(detections)

    for tracker_index, detection_index in enumerate(track2detection):
        if iou[tracker_index, detection_index] != 0:
            tracker_ids[detection_index] = tracks[tracker_index].track_id

    return tracker_ids





def process_video_for_mot(input_video_path,output_dir):
    """
    Process a video for Multi-Object Tracking (MOT) using BYTETracker and YOLO model.

    Args:
        model: The YOLO model instance.
        input_video_path (str): Path to the source video.
        output_dir (str): directory path for the result.
    """

    video_name = os.path.basename(input_video_path).split('.')[0]
    output_txt = f"{output_dir}/car_{video_name}.txt"
    output_video = f"{output_dir}/car_{video_name}.mp4"
    
    if os.path.exists(output_video):
        print(f"already tracked {output_video}")
        return
    else:
        print(f"start tracking {output_video}!")
    MODEL = "models/yolov8x.pt"
    model = YOLO(MODEL)
    model.fuse()


    # dict mapping class_id to class_name
    CLASS_NAMES_DICT = model.model.names
    # class_ids of interest - person, car, motorcycle, bus and truck
    CLASS_ID = [2,7]

    # create BYTETracker instance
    byte_tracker = BYTETracker(BYTETrackerArgs())
    # create VideoInfo instance
    video_info = VideoInfo.from_video_path(input_video_path)
    # create frame generator
    generator = get_video_frames_generator(input_video_path)
    # create instance of BoxAnnotator
    box_annotator = BoxAnnotator(color=ColorPalette(), thickness=2, text_thickness=1, text_scale=0.5)

    # open target video file
    with VideoSink(output_video, video_info) as sink:
        # loop over video frames
        with open(output_txt, 'w') as f:
            for frame_number, frame in enumerate(generator):
                # model prediction on single frame and conversion to supervision Detections
                results = model(frame)
                detections = Detections(
                    xyxy=results[0].boxes.xyxy.cpu().numpy(),
                    confidence=results[0].boxes.conf.cpu().numpy(),
                    class_id=results[0].boxes.cls.cpu().numpy().astype(int)
                )

                # filtering out detections with unwanted classes
                mask = np.array([class_id in CLASS_ID for class_id in detections.class_id], dtype=bool)
                detections.filter(mask=mask, inplace=True)
                # tracking detections
                tracks = byte_tracker.update(
                    output_results=detections2boxes(detections=detections),
                    img_info=frame.shape,
                    img_size=frame.shape
                )
                tracker_id = match_detections_with_tracks(detections=detections, tracks=tracks)
                detections.tracker_id = np.array(tracker_id)
                # filtering out detections without trackers
                mask = np.array([tracker_id is not None for tracker_id in detections.tracker_id], dtype=bool)
                detections.filter(mask=mask, inplace=True)
                # format custom labels
                labels = [
                    f"#{tracker_id} {CLASS_NAMES_DICT[class_id]} {confidence:0.2f}"
                    for _, confidence, class_id, tracker_id
                    in detections
                ]
                # annotate and display frame
                frame = box_annotator.annotate(frame=frame, detections=detections, labels=labels)
                sink.write_frame(frame)

                ### Corrected code ------
                for i, (confidence, class_id, tracker_id) in enumerate(zip(detections.confidence, detections.class_id, detections.tracker_id)):
                    x1, y1, x2, y2 = detections.xyxy[i]
                    line = f"{frame_number},{tracker_id},{x1},{y1},{x2},{y2},{confidence},{class_id},-1,-1\n"
                    f.write(line)
    
# process_video_for_mot(model,"videos/jaad/video_0194.mp4","./YOLOX_outputs/car_videos/")


import argparse

# Your existing imports and code...



def main():
    parser = argparse.ArgumentParser(description="Process a video for Multi-Object Tracking (MOT) using BYTETracker and YOLO model.")
    parser.add_argument("input_video_path", type=str, help="Path to the source video.")
    parser.add_argument("output_dir", type=str, help="Directory path for the result.")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_video_path):
        print(f"Error: File {args.input_video_path} does not exist.")
        return

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    process_video_for_mot(args.input_video_path, args.output_dir)
    print(f"finished tracking {args.input_video_path}")
if __name__ == "__main__":
    main()
