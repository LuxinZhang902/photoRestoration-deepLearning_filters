import cv2
import numpy as np

def calculate_color_score(image_path):
    image = cv2.imread(image_path)

    (B, G, R) = cv2.split(image.astype("float"))

    rg = np.absolute(R - G)
    yb = np.absolute(0.5 * (R + G) - B)

    (rbMean, rbStd) = (np.mean(rg), np.std(rg))
    (ybMean, ybStd) = (np.mean(yb), np.std(yb))

    std_root = np.sqrt((rbStd ** 2) + (ybStd ** 2))
    mean_root = np.sqrt((rbMean ** 2) + (ybMean ** 2))

    color = std_root + (0.3 * mean_root)

    return color

# image_path_color = 'test_img/color1.png'
# image_path_gray = 'test_img/gray1.png'
# color_score = calculate_color_score(image_path_color)
# gray_score = calculate_color_score(image_path_gray)
# print(f"Color score for the color image: {color_score}")
# print(f"Color score for the gray image: {gray_score}")