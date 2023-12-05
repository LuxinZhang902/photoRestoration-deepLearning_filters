import os
from PIL import Image
from tqdm import tqdm
import matplotlib.pyplot as plt

# Paths to your directories
dir1 = './OldPic'
dir2 = './SelfPic'
dir3 = './DlPic'

# Paths to your directories
output_dir = 'result_out'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get the list of images
images1 = sorted(os.listdir(dir1))
images2 = sorted(os.listdir(dir2))
images3 = sorted(os.listdir(dir3))

# Number of images to compare
num_images = len(images1)

for i in tqdm(range(num_images), desc="Processing Images"):
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    img1 = Image.open(os.path.join(dir1, images1[i]))
    img2 = Image.open(os.path.join(dir2, images2[i]))
    img3 = Image.open(os.path.join(dir3, images3[i]))

    axs[0].imshow(img1)
    axs[0].set_title(f"Image {i+1} from Dir1")
    axs[0].axis('off')

    axs[1].imshow(img2)
    axs[1].set_title(f"Image {i+1} from Dir2")
    axs[1].axis('off')

    axs[2].imshow(img3)
    axs[2].set_title(f"Image {i+1} from Dir3")
    axs[2].axis('off')

    # Save the figure
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, f'comparison_{i+1}.png'))

    plt.close(fig)
