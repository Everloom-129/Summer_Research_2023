import numpy as np

# Get the estimated angle of each person to the dashcam
def estimate_angle(image, person, fov_horizontal = 170):
    
    # Step 1: Filter out detections that are not pedestrians
    if person.object_type!= 'person':
        return None
    
    # Step 2: Estimate distance
    box = person.box
    bottom_center = (box[0]+box[2])/2, box[3] # feet 
    
    distance = person.distance
    # If the distance is a descriptive string, we need to convert it into a numerical representation
    if isinstance(distance, str):
        distance_mapping = {"very close": 1, "close": 2, "median": 3, "far": 4, "very far": 5}
        if distance in distance_mapping:
            distance = distance_mapping[distance]
        else:
            print(f"Invalid distance description: {distance}")
            return None
    elif not isinstance(distance, (int, float)):
        print(f"Invalid distance type: {type(distance)}")
        return None
    
    # Step 3: Estimate angle
    image_center_y = image.shape[1] / 2
    pedestrian_center = bottom_center[0]
    relative_position = pedestrian_center - image_center_y

    angle = np.arctan(relative_position / distance * np.tan(np.radians(fov_horizontal) / 2))
    
    return np.degrees(angle)

def describe_angle(angle):
    """Describe the angle in simple terms."""
    if angle == None:
        return "unknown"
    # Handle the straight-ahead case
    if -10 <= angle <= 10:
        return "straight ahead"

    # Handle the right side
    if 10 < angle <= 45:
        return "slightly to the right"
    elif 45 < angle <= 135:
        return "to the right"
    elif angle > 135:
        return "far to the right"

    # Handle the left side
    if -45 >= angle > -10:
        return "slightly to the left"
    elif -135 >= angle > -45:
        return "to the left"
    elif angle < -135:
        return "far to the left"
