import os
import pandas as pd

from algorithms.color import calculate_color_score
from algorithms.noise import calculate_noise_score
from algorithms.clarity import calculate_clarity_score
from algorithms.contrast import calculate_contrast
# from algorithms.clarity_test import calculate_clarity_score
from compare import compareImage


def get_image_paths(directory):
    """
    This method stores all image paths in the given directory.

    Parameters:
    directory (string): The string that is the path of the file that contains all image files

    Returns:
    List: A list of images' paths
    """
    extensions = ['.jpg', '.jpeg', '.png'] # It supports three different extensions, add more if needed
    image_paths = [os.path.join(directory, file) for file in os.listdir(directory) 
                   if os.path.splitext(file)[1].lower() in extensions]
    return image_paths


def export_excel(old_score, dl_score, self_score):
    column = ["Picture {}".format(i + 1) for i in range(16)]

    old_df = pd.DataFrame({'clarity_score': old_score[0],
                           'noise_score': old_score[1],
                           'contrast_score': old_score[2],
                           'color_score': old_score[3],
                           'restoration_score': old_score[4]})
    
    dl_df = pd.DataFrame({'clarity_score': dl_score[0],
                          'noise_score': dl_score[1],
                          'contrast_score': dl_score[2],
                          'color_score': dl_score[3],
                          'restoration_score': dl_score[4]})
    
    self_df = pd.DataFrame({'clarity_score': self_score[0],
                            'noise_score': self_score[1],
                            'contrast_score': self_score[2],
                            'color_score': self_score[3],
                            'restoration_score': self_score[4]})
    
    old_df.columns = ['old_' + col for col in old_df.columns]
    dl_df.columns = ['dl_' + col for col in dl_df.columns]
    self_df.columns = ['self_' + col for col in self_df.columns]
    
    combined_df = pd.concat([old_df, dl_df, self_df], axis=1)
    
    combined_df.insert(0, 'Picture', column)
    
    combined_df.to_excel('scores.xlsx', index=False)



def restoration_score(clarity_score, contrast_score, noise_score, color_score, clarity_weight, contrast_weight, noise_weight, color_weight):
    """
    Calculates a general score for photo restoration based on clarity, ISO, noise, and color scores.
    """

    total_weight = clarity_weight + contrast_weight + noise_weight + color_weight
    # print(total_weight)
    if total_weight != 1:
        raise ValueError("The sum of weights must be 1.")

    restoration_score = (color_score * color_weight) - (noise_score * noise_weight) - \
                        (clarity_score * clarity_weight) + (contrast_score * contrast_weight)
                        
    
    return restoration_score



def calculate_score(directory_path):
    image_paths = get_image_paths(directory_path)

    clarity_list = []
    noise_list = []
    contrast_list = []
    color_list = []
    final_list = []

    for path in image_paths:
        
        # calculate clarity score and put them into the list
        clarity_score = calculate_clarity_score(path)
        clarity_list.append(clarity_score)

        # calculate noise score and put them into the list
        noise_score = calculate_noise_score(path)
        noise_list.append(noise_score)

        # calculate contrast score and put them into the list
        contrast_score = calculate_contrast(path)
        contrast_list.append(contrast_score)

        # calculate color score and put them into the list
        color_score = calculate_color_score(path)
        color_list.append(color_score)


        # Weights for each score
        clarity_weight = 0.4       # 40%
        contrast_weight = 0.2      # 20%
        noise_weight = 0.3         # 30%
        color_weight = 1 - clarity_weight - contrast_weight - noise_weight    # 10%

        final_score = restoration_score(clarity_score, contrast_score, noise_score, color_score, clarity_weight, contrast_weight, noise_weight, color_weight)
        final_list.append(final_score)

    print(f'Clarity list: {clarity_list}\n')
    print(f'Noise list: {noise_list}\n')
    print(f'Contrast list: {contrast_list}\n')
    print(f'Color list: {color_list}\n')
    print(f'General list: {final_list}\n')

    return [clarity_list, noise_list, contrast_list, color_list, final_list]

if __name__ == "__main__":

    OldPic_list = './OldPic'
    print('Scores for old pictures')
    old_list = calculate_score(OldPic_list)

    DlPic_list = './DlPic'
    print('Scores for deep learning pictures')
    dp_list = calculate_score(DlPic_list)

    SelfPic_list = './SelfPic'
    print('Scores for self-implemented algorithm')
    self_list = calculate_score(SelfPic_list)

    # Export the result into the excel
    export_excel(old_list, dp_list, self_list)

    # Compare the result
    compareImage(OldPic_list, DlPic_list, SelfPic_list, output_dir='result_out')

    # # test
    # print("old_list: ", old_list)
    # print("dp_list: ", dp_list)
    # print("self_list: ", self_list)