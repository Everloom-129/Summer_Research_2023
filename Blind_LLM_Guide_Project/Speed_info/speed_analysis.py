import cv2
import numpy as np
from imutils.object_detection import non_max_suppression
import imutils

# Step 1: Video Frame Extraction
def extract_frames(video_path):
    frames = []
    
    vidcap = cv2.VideoCapture(video_path)
    success, frame = vidcap.read()

    while success:
        frames.append(frame)
        success, frame = vidcap.read()
    
    return frames

# Step 2: Object Detection
def detect_objects(frames):
    detected_objects = []

    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    for frame in frames:
        frame = imutils.resize(frame, width=min(400, frame.shape[1]))
        (rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4),
            padding=(8, 8), scale=1.05)
        
        # apply non-maxima suppression to the bounding boxes using a
        # fairly large overlap threshold to try to maintain overlapping
        # boxes that are still people
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
        
        detected_objects.append(pick)
        
    return detected_objects

# Step 3: Object Tracking
def track_objects(detected_objects):
    tracked_objects = []
    
    # Here we would use an object tracking algorithm, for simplicity we are assuming objects are tracked correctly
    # In a real-world application, you could use algorithms like SORT (Simple Online and Realtime Tracking)
    tracked_objects = detected_objects
    
    return tracked_objects

# Step 4: Speed Calculation
def calculate_speed(tracked_objects, frame_rate):
    object_speeds = []

    # calculate speed of each object by using their positions across frames and frame rate of the video.
    for i in range(1, len(tracked_objects)):
        prev_frame, current_frame = tracked_objects[i-1], tracked_objects[i]
        for prev_pos, current_pos in zip(prev_frame, current_frame):
            # calculate Euclidean distance between previous and current position
            dist = np.sqrt(np.sum((current_pos - prev_pos)**2))
            speed = dist * frame_rate  # pixels/second
            object_speeds.append(speed)
    
    return object_speeds

# Step 5: Speed Classification
def classify_speed(object_speeds):
    speed_classification = []

    # classify the speed into: still, slow, moderate, fast
    for speed in object_speeds:
        if speed == 0:
            speed_classification.append('still')
        elif speed < 30:
            speed_classification.append('slow')
        elif speed < 60:
            speed_classification.append('moderate')
        else:
            speed_classification.append('fast')
    
    return speed_classification

# Put all steps together
def analyze_video(video_path):
    frames = extract_frames(video_path)
    detected_objects = detect_objects(frames)
    tracked_objects = track_objects(detected_objects)
    object_speeds = calculate_speed(tracked_objects, frame_rate=30)  # assuming 30 FPS
    speed_classification = classify_speed(object_speeds)
    
    return speed_classification

# Run the analysis
speed_classification = analyze_video('video_0197.mp4')
print(speed_classification)
