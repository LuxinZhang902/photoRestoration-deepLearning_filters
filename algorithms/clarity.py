import cv2
import numpy as np
def calculate_clarity_score(image_path):
    """
    Calculate the clarity score of the given image using Gaussian Blur.

    Parameters:
    image_path(List: A list of images' paths)

    Returns:
    score (double): The final score of clarity

    Author: Luxin Zhang
    """
    # Read the image
    original_image = cv2.imread(image_path)
    if original_image is None:
        return None

    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(original_image, (5, 5), 0)

    # Calculate the difference between the original and blurred images
    difference = cv2.absdiff(original_image, blurred_image)

    # Convert the difference to grayscale
    gray_difference = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

    # Calculate the clarity score as the mean of the gray difference
    score = np.mean(gray_difference)
    
    return score

