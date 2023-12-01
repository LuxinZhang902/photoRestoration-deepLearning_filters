import os
import cv2
import numpy as np


def get_image_paths(directory):
    """
    This method stores all image paths in the given directory.

    Parameters:
    directory (string): The string that is the path of the file that contains all image files

    Returns:
    List: A list of images' paths

    Author: Luxin Zhang
    """
    extensions = ['.jpg', '.jpeg', '.png'] # It supports three different extensions, add more if needed
    image_paths = [os.path.join(directory, file) for file in os.listdir(directory) 
                   if os.path.splitext(file)[1].lower() in extensions]
    return image_paths



def clarity_score(image_path):
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


# Testing
directory_path = './pics'
image_paths = get_image_paths(directory_path)

for path in image_paths:
    score = clarity_score(path)
    if score is not None:
        print(f"Clarity score for {path}: {score}")

