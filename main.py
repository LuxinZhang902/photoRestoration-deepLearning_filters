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
    directory_path = './OldPic'
    image_paths = get_image_paths(directory_path)

    clarity_list = []
    noise_list = []
    ISO_list = []
    color_list = []
    general_list = []

    for path in image_paths:
        
        clarity_score = calculate_clarity_score(path)
        clarity_list.append(clarity_score)

        noise_score = calculate_noise_score(path)
        noise_list.append(noise_score)

        # iso_score = calculate_iso_score(path)
        iso_score = 2000
        ISO_list.append(iso_score)

        color_score = calculate_color_score(path)
        color_list.append(color_score)

        # Weights for each score
        clarity_weight = 0.3  # 30%
        iso_weight = 0.2      # 20%
        noise_weight = 0.3    # 30%
        color_weight = 0.2    # 20%

        final_score = restoration_score(clarity_score, iso_score, noise_score, color_score, clarity_weight, iso_weight, noise_weight, color_weight)
        print(f"Restoration Score: {restoration_score}")
        general_list.append(final_score)

print(f'Clarity list: {clarity_list}\n')
print(f'Noise list: {noise_list}\n')
print(f'ISO list: {ISO_list}\n')
print(f'Color list: {color_list}\n')
print(f'General list: {general_list}\n')