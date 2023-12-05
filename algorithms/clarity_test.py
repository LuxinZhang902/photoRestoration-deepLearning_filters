import cv2
import numpy as np

def calculate_clarity_score(image_path):
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Laplacian
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Apply Sobel
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_total = np.sqrt(sobelx**2 + sobely**2)
    sobel_mean = np.mean(sobel_total)

    # Clarity score - you can experiment with how you combine these
    clarity_score = 0.5 * laplacian_var + 0.5 * sobel_mean 

    return clarity_score * 0.1

# # Example usage
# score = calculate_image_clarity('path_to_your_image.jpg')
# print("Clarity Score:", score)
