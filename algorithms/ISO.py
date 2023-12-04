from PIL import Image
from PIL.ExifTags import TAGS

def get_iso(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Extract EXIF data
    exif_data = img._getexif()

    # Convert EXIF data to human-readable form
    labeled_exif = {TAGS[key]: value for key, value in exif_data.items() if key in TAGS}

    # Extract ISO score
    iso_score = labeled_exif.get('ISOSpeedRatings', None)


    return iso_score


def calculate_iso_score(image_path):
    iso = get_iso(image_path)
    print("iso is ")
    print(type(iso))
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

