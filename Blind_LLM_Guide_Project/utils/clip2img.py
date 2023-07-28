import os
import cv2
import numpy as np
import math

# Input video directory
input_video_dir = "HZ3" # "path_to_your_video_directory"

# Output directory
output_dir = ".\\output"

# Fetch all video file names
video_files = [f for f in os.listdir(input_video_dir) if f.endswith('.mp4')]

for video_file in video_files:
    # Create a VideoCapture object
    cap = cv2.VideoCapture(os.path.join(input_video_dir, video_file))
    # Get the frames per second (fps) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    # Get the total number of frames in the video
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # Calculate the duration of the video clip
    duration = num_frames / fps

    # Calculate the frame interval for each 1/3 second
    frame_interval = math.floor(fps / 3)
    if frame_interval == 0:
        break
    # Create output directory for each video
    video_dir = os.path.join(output_dir, video_file.split(".")[0])
    os.makedirs(video_dir, exist_ok=True)

    # Frame sequence number
    seq_num = 0

    # Read until video is completed
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) % frame_interval == 0:
                seq_num += 1
                cv2.imwrite(os.path.join(video_dir, f'image_{seq_num:04d}.png'), frame)

            if seq_num == math.floor(duration * 3):  # Adjust the break condition
                break
        # Break the loop if no frame is returned
        else:
            break

    # Release the video capture object
    cap.release()

print("Video processing completed.")
