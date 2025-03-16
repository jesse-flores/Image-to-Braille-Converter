import cv2
import numpy as np

# Braille characters arranged from light to dark
BRAILLE_CHARS = [
    "⠀", "⠁", "⠂", "⠃", "⠄", "⠅", "⠆", "⠇", "⠈", "⠉", "⠊", "⠋", "⠌", "⠍", "⠎", "⠏", "⠐", "⠑", "⠒", "⠓", "⠔", "⠕", "⠖", "⠗", "⠘", "⠙", "⠚", "⠛", "⠜", "⠝", "⠞", "⠟", "⠠", "⠡", "⠢", "⠣", "⠤", "⠥", "⠦", "⠧", "⠨", "⠩", "⠪", "⠫", "⠬", "⠭", "⠮", "⠯", "⠰", "⠱", "⠲", "⠳", "⠴", "⠵", "⠶", "⠷", "⠸", "⠹", "⠺", "⠻", "⠼", "⠽", "⠾", "⠿", "⣿"
]



# Function to resize the image to fit within a specified width
def resize_image(image, new_width=200):
    height, width = image.shape[:2]
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

# Function to convert the image to grayscale
def grayify(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Function to apply thresholding to improve contrast and clarity
def threshold_image(image, threshold=108):
    _, thresh_img = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return thresh_img

# Function to map each pixel to an braille character
def pixels_to_braille(image):
    # Divide the image into blocks, such as 3x3 pixels for each Braille character
    height, width = image.shape
    braille_str = ""
    for y in range(0, height, 3):  # Iterate over the image in 3-pixel chunks (height)
        for x in range(0, width, 2):  # Iterate over the image in 2-pixel chunks (width)
            block = image[y:y+3, x:x+2]
            if block.shape != (3, 2):
                continue  # Skip if the block is smaller than 3x2 (edge case)
            
            # Compute the average brightness of the block
            avg_brightness = np.mean(block)
            
            # Map the average brightness to a Braille character
            braille_char = BRAILLE_CHARS[int(avg_brightness / 3.93)]
            braille_str += braille_char
        braille_str += "\n"
    
    return braille_str

# Function to convert an image to braille
def image_to_braille(image_path, new_width=200):
    try:
        # Load image using OpenCV
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found or invalid")
    except Exception as e:
        print(e)
        return
    
    # Resize and convert the image to grayscale
    image = resize_image(image, new_width)
    gray_image = grayify(image)
    
    # Apply thresholding for better contrast (optional)
    thresholded_image = threshold_image(gray_image, threshold=108)
    
    # Convert pixels to Braille
    braille_str = pixels_to_braille(thresholded_image)
    
    return braille_str

# Specify the image path
image_path = "assets/starry_night.png"

# Convert the image to Braille representation
braille_art = image_to_braille(image_path)
print(braille_art)