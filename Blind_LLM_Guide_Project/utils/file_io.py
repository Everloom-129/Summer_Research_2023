
def is_image_file(filename):
    IMAGE_EXT = ['.jpg', '.jpeg', '.png', '.bmp']
    return any(filename.endswith(extension) for extension in IMAGE_EXT)
