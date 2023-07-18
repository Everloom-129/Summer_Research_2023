import os
import shutil
import random

# Directories
output_dir = ".\\output"
selected_dir = ".\\selected"

# Create the selected directory if it doesn't exist
os.makedirs(selected_dir, exist_ok=True)

# Get list of video directories in the output directory
video_dirs = [d for d in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, d))]

for video_dir in video_dirs:
    # Get list of images in the video directory
    image_files = [f for f in os.listdir(os.path.join(output_dir, video_dir)) if f.endswith('.png')]

    # Randomly select one image file
    selected_image = random.choice(image_files)

    # Create new image name as 'video0xxx_00xx'
    new_image_name = video_dir + '_' + selected_image.split('_')[1]

    # Copy the selected image to the selected directory
    shutil.copy(os.path.join(output_dir, video_dir, selected_image), os.path.join(selected_dir, new_image_name))

print("Image copying completed.")
