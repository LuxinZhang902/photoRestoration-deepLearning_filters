
from PIL import Image
import numpy as np

def calculate_contrast(image_path):
    # Step 1: Load the image
    img = Image.open(image_path)

    # Step 2: Convert to grayscale
    grayscale_img = img.convert('L')

    # Step 3: Calculate contrast (using standard deviation)
    img_array = np.array(grayscale_img)
    contrast = np.std(img_array)

    # Score the image (normalize to a 0-100 scale)
    max_possible_std = 255  # Max standard deviation for 8-bit image
    score = (contrast / max_possible_std) * 100

    return score

# Example usage
# image_path = '../SelfPic/1.jpg'
# contrast_score = calculate_contrast(image_path)
# print(f"Contrast Score: {contrast_score}")