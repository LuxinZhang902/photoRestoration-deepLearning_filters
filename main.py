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



def score_iso(iso):
    """
    Scores a photo based on its ISO value.
    Lower ISO values receive higher scores.

    Parameters:
    iso (double): The ISO value extracted from the pic itself

    Returns:
    double: The given score for ISO

    Author: Luxin Zhang
    """

    if iso <= 100:
        score = 10  # Highest score for ISO 100 or lower
    elif iso <= 200:
        score = 9
    elif iso <= 400:
        score = 8
    elif iso <= 800:
        score = 7
    elif iso <= 1600:
        score = 6
    elif iso <= 3200:
        score = 5
    else:
        score = 4  # Lower score for very high ISO values

    return score


def restoration_score(clarity_score, iso_score, noise_score, color_score, clarity_weight, iso_weight, noise_weight, color_weight):
    """
    Calculates a general score for photo restoration based on clarity, ISO, noise, and color scores.
    
    Author: Luxin Zhang
    """

    total_weight = clarity_weight + iso_weight + noise_weight + color_weight
    if total_weight != 1:
        raise ValueError("The sum of weights must be 1.")

    restoration_score = (clarity_score * clarity_weight) + (iso_score * iso_weight) + \
                        (noise_score * noise_weight) + (color_score * color_weight)
    
    return restoration_score


if __name__ == "__main__": 
    # Testing
    directory_path = './pics'
    image_paths = get_image_paths(directory_path)

    for path in image_paths:
        
        score = clarity_score(path)
        if score is not None:
            print(f"Clarity score for {path}: {score}")


    # Testing ISO
    iso_value = 3000
    print(f"Score for ISO {iso_value}: {score_iso(iso_value)}")


    # Testing general score
    clarity_score = 8.5  # hypothetical clarity score
    iso_score = 14      # hypothetical ISO score
    noise_score = 7.5   # hypothetical noise score
    color_score = 9.0   # hypothetical color score

    # Weights for each score
    clarity_weight = 0.3  # 30%
    iso_weight = 0.2      # 20%
    noise_weight = 0.3    # 30%
    color_weight = 0.2    # 20%

    restoration_score = restoration_score(clarity_score, iso_score, noise_score, color_score, clarity_weight, iso_weight, noise_weight, color_weight)
    print(f"Restoration Score: {restoration_score}")

