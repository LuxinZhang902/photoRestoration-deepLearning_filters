import os

from algorithms.color import calculate_color_score
from algorithms.noise import calculate_noise_score
from algorithms.clarity import calculate_clarity_score
from algorithms.ISO import calculate_iso_score


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
        
        score = calculate_clarity_score(path)
        if score is not None:
            print(f"Clarity score for {path}: {score}")


    # Testing ISO
    iso_value = 3000
    print(f"Score for ISO {iso_value}: {calculate_iso_score(iso_value)}")

    # Testing Color Score
    image_path_color = 'pics/colorful.jpg'
    image_path_gray = 'pics/OIP.jpeg'
    color_score = calculate_color_score(image_path_color)
    gray_score = calculate_color_score(image_path_gray)
    print(f"Color score for the color image: {color_score}")
    print(f"Color score for the gray image: {gray_score}")

    # Testing Noise Score
    # image_path_noise = 'test_img/noise1.jpeg'
    # image_path_clear = 'test_img/clear1.jpg'
    score_noise = calculate_noise_score(image_path_color)
    score_clear = calculate_noise_score(image_path_gray)
    print(f"Noise score for the noise image: {score_noise}")
    print(f"Noise score for the noise clear: {score_clear}")


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

