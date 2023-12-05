import cv2
import numpy as np

def calculate_noise_score(image_path):
    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    noise_score = np.std(gray_image)

    return noise_score * 0.1

# image_path_noise = 'test_img/noise1.jpeg'
# image_path_clear = 'test_img/clear1.jpg'
# score_noise = calculate_noise_score(image_path_noise)
# score_clear = calculate_noise_score(image_path_clear)
# print(f"Noise score for the noise image: {score_noise}")
# print(f"Noise score for the noise clear: {score_clear}")