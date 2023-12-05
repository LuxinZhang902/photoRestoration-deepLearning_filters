import cv2
import numpy as np
import os
import shutil

def sharpen_image(origin_img):    
    # Define the sharpening kernel
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    # Apply the kernel for convolution to sharpen the image
    sharpened_image = cv2.filter2D(origin_img, -1, kernel)

    return sharpened_image

   
def cmp_clarity(img):
    """
    Calculate the clarity score of the given image using Gaussian Blur.
    Input: image 2D matrix
    Output: socre double
    """
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(img, (5, 5), 0)

    # Calculate the difference between the original and blurred images
    difference = cv2.absdiff(img, blurred_image)

    # Convert the difference to grayscale
    gray_difference = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

    # Calculate the clarity score as the mean of the gray difference
    score = np.mean(gray_difference)
    return score


def self_imp_alg(img):
    """
    Do four types of processing and using clarity as the score to choose the one with best performance
    Input: image 2D matrix
    Output: image 2D matrix
    """
    k_size = 5
    kernel_size=(5,5)
    sigmaX=0
    # Dict for record score of each filter
    clarity = {'guassian':0.0,'bilateral':0.0,'median':0.0,'sharpen':0.0}
    # Dict for result of each filter
    result_imgs = {}
    
    # Apply Gaussian blur for each channel
    guassian_img = cv2.GaussianBlur(img, kernel_size, sigmaX)
    clarity['guassian'] = cmp_clarity(guassian_img)
    result_imgs['guassian'] = guassian_img
    
    # Apply bilateral filter for each channel
    denoised_img = cv2.bilateralFilter(img, 8, 30, 75)
    clarity['bilateral'] = cmp_clarity(denoised_img)
    result_imgs['bilateral'] = denoised_img
    
    # Apply median blur for each channel
    median_blurred_image = cv2.medianBlur(img, k_size)
    clarity['median'] = cmp_clarity(median_blurred_image)
    result_imgs['median'] = median_blurred_image
    
    # Apply sharpen image function for the image
    sharpened_image = sharpen_image(img)
    clarity['sharpen'] = cmp_clarity(sharpened_image)
    result_imgs['sharpen'] = sharpened_image
    
    # Find the key corresponding to the largest value
    best_filter = max(clarity.items(), key=lambda x: x[1])[0]
    return result_imgs[best_filter]


def remove_existed_img(directory_path):
    """
    Ensure each time the output file is empty
    Input: output file path str
    """
    # Remove all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Error removing {file_path}: {e}")
    print("Empty the file successfully.")



if __name__ == "__main__":
    input_file_path = "./Old pic/"
    output_file_path = "./alg result/"
    remove_existed_img(output_file_path)
    
    # total picture number
    pic_num = 16
    
    for i in range(pic_num):
        input_image_path = input_file_path + str(i+1) + ".jpg"
        output_image_path = output_file_path + str(i+1) + ".jpg"
        
        # read the image from file
        img = cv2.imread(input_image_path)
        
        # implement our algorithm
        result_img = self_imp_alg(img)
        
        # save the result image
        cv2.imwrite(output_image_path,result_img)
    
    print("Self implement algorithm done")

    
