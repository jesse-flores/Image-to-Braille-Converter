# Image to Braille Converter

This project converts images into Braille characters, representing pixel intensity using Braille symbols. It processes an image and converts it into a series of Braille characters based on pixel brightness, using a grid of characters to represent light-to-dark shades.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

## Overview

This project uses OpenCV and NumPy to process images, converting them into Braille text that visually represents the image’s pixel intensities. Braille is a tactile writing system used by visually impaired people, and this project translates visual data into a form that could be more accessible to those using Braille.

The project processes the image by dividing it into small blocks, averaging the pixel intensities, and mapping them to Braille characters. The final output is a text representation of the image in Braille.

## Features

- Convert images to Braille
- Customize image width for better fit and resolution
- Supports different levels of contrast via thresholding
- Uses a custom set of Braille characters

## Requirements

Before using the script, make sure you have the following libraries installed:

- `opencv-python` for image processing.
- `numpy` for handling numerical operations and image arrays.

You can install these dependencies via pip:

```bash
pip install opencv-python numpy
```

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/image-to-braille.git
   ```

2. Navigate to the project directory:

   ```bash
   cd image-to-braille
   ```

3. Install the necessary Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the script, run it with the path to the image you want to convert. Make sure the image is in a compatible format (JPG, PNG, etc.).

### Command-Line Usage

1. Place the image you want to convert in the appropriate directory or specify its full path in the code.
2. Run the script:

```bash
python image_to_braille.py
```

This will convert the specified image into a string of Braille characters and print it to the console.

### Customizing the Output

- **Width of the image**: You can adjust the `new_width` parameter in the `image_to_braille` function to control the width of the output. Larger widths will result in a higher resolution output.

```python
image_to_braille("path/to/your/image.png", new_width=500)
```

- **Thresholding**: The `threshold` parameter in the `threshold_image` function controls the contrast level. Higher values make the image more binary (black/white).

```python
thresholded_image = threshold_image(gray_image, threshold=200)
```

## Example

For an example, assume you have an image of Van Gogh's Starry Night painting. The following code converts this image into Braille text and prints it:

```python
image_path = "assets/starry_night.png"
braille_art = image_to_braille(image_path)
print(braille_art)
```

This will display the Braille version of the image.

### Example Output:

![image](https://github.com/user-attachments/assets/637917aa-cb51-482a-9422-d1db30dc45d2)


C:\Users\18s0m\Downloads\program\image_to_braille>python image_to_braille.py
⠀⠀⠀⠀⠀⠀⠊⠫⠫⣿⠶⣿⠫⠫⠕⠀⠀⠀⠀⠀⠀⠕⠠⠕⠊⠀⠀⠀⠀⠀⠀⠊⠀⠶⠶⠶⠶⠊⠊⠀⠀⠊⠀⠕⠊⠕⠫⠕⠕⠶⠫⠊⠕⠀⠊⠀⠀⠊⠀⠊⠀⠀⠀⠀⠀⠀⠕⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠊⠀⠕⠊⠠⠕⠠⠠⠕⠊⠊⠠⠕⠕⠕⠊⠕⠊⠀⠀⣿
⠀⠀⠊⠀⠀⠀⠕⠶⣿⣿⠫⣿⠶⣿⠶⠊⠊⠀⠀⠀⠊⠠⠠⠶⠫⠕⠀⠀⠀⠀⠀⠕⠶⣿⣿⣿⠶⠶⠕⠊⠀⠀⠊⠊⠊⠕⠕⠕⠕⠊⠊⠕⠀⠊⠊⠀⠀⠀⠕⠀⠕⠀⠕⠊⠀⠕⠊⠀⠀⠊⠕⠊⠀⠊⠀⠀⠀⠕⠕⠀⠕⠊⠊⠀⠕⠀⠕⠕⠕⠕⠶⠕⠠⠕⠠⠊⠕⠕⠕⠶
⠀⠀⠀⠀⠀⠀⠕⣿⣿⣿⠫⣿⣿⠶⠫⠊⠀⠀⠀⠀⠊⠕⠫⠫⠶⠫⠀⠀⠀⠀⠀⠠⠶⠶⣿⠶⣿⣿⠕⣿⣿⠫⠶⠠⠊⠀⠕⠀⠊⠠⠀⠊⠀⠊⠀⠀⠀⠠⠠⠠⠕⠠⠕⠊⠊⠊⠊⠀⠀⠕⠀⠀⠊⠊⠊⠀⠊⠊⠊⠊⠕⠫⠕⠠⠫⠫⣿⣿⣿⠶⠶⣿⠶⣿⠫⠫⠫⠠⠕⣿
⠀⠀⠀⠀⠀⠀⠕⠫⠠⠶⣿⣿⣿⣿⣿⠕⠀⠀⠀⠀⠀⠀⠀⠊⠊⠕⠀⠕⠀⠀⠀⠕⠶⠶⠶⠶⠕⠫⠊⠶⣿⠶⣿⠶⠊⠕⠊⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⠶⣿⠶⠫⠶⠫⠠⠀⠀⠕⠀⠀⠕⠀⠀⠀⠀⠠⠊⠕⠀⠀⠊⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⠶⠠⠫⣿
⠀⠀⠀⠀⠀⠀⠊⠕⠠⠶⣿⠫⠠⠫⠊⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠕⠀⠀⠊⠕⠊⠀⠀⠀⠊⠀⠀⠠⠶⠫⠊⠊⠀⠀⠀⠕⠀⠊⠊⠀⠀⠀⠀⠊⠠⣿⣿⠶⣿⣿⣿⣿⠠⠶⠊⠀⠀⠀⠀⠀⠀⠀⠀⠫⠕⠊⠠⠊⠕⠶⠶⣿⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⣿⠶⣿⠶⣿
⠕⠀⠀⠀⠀⠀⠊⠊⠀⠕⠀⠊⠠⠊⠀⠀⠀⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠕⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠊⠊⠠⠀⠀⠀⠀⠀⠀⠫⠫⠶⣿⣿⣿⣿⣿⠫⠫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠕⠕⠠⠫⠶⠶⠶⣿⣿⣿⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠊⠕⠊⠀⠀⠀⠀⠊⠀⠀⠕⠀⠀⠀⠊⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠠⠫⠫⣿⠶⠶⠕⠫⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠶⣿⠶⠫⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⠶⣿⣿⣿⣿⣿⠶⠶⣿⣿
⠫⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠕⠫⣿⠕⠕⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠊⠕⠕⠀⠀⠀⠊⠕⠕⠀⠀⠀⠊⠀⠀⠊⠀⠀⠀⠠⠫⠕⠶⠊⠀⠊⠀⠀⠀⠊⠀⠀⠀⠊⠀⠀⠀⠊⠕⠶⠶⠫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠫
⠫⠕⠶⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠫⠶⠶⠶⣿⣿⠠⠕⠀⠀⠀⠀⠀⠀⠀⠊⠀⠊⠠⠠⠕⠠⠀⠊⠊⠊⠊⠕⠠⠕⠕⠀⠊⠊⠊⠀⠀⠀⠀⠊⠀⠀⠀⠊⠀⠀⠀⠕⠊⠀⠀⠕⠕⠀⠊⠊⠠⠶⠕⠫⠶⣿⣿⣿⣿⣿⣿⣿⠶⣿⣿⣿⣿⣿⣿⠶⣿⣿⣿⣿
⣿⠠⠀⠕⠀⠀⠀⠀⠊⠀⠊⠊⠊⠊⠀⠀⠀⠀⠊⠀⣿⠫⠶⠶⣿⣿⠫⠕⠀⠀⠀⠀⠊⠊⠀⠀⠕⠕⠊⠶⣿⣿⣿⣿⠶⣿⣿⣿⣿⠶⣿⠊⠠⠠⠠⣿⠠⠕⠕⠀⠀⠀⠀⠀⠀⠀⠊⠕⠠⠠⠫⠶⠕⠠⠊⠠⠕⠕⠫⣿⣿⣿⣿⣿⣿⠫⣿⣿⣿⣿⣿⣿⣿⣿⣿⠫⠶⣿⣿⣿
⠶⠠⠊⠕⠫⠊⠀⠀⠀⠀⠊⠀⠀⠊⠀⠀⠀⠀⠊⠀⠠⠠⣿⠶⠶⣿⠶⠀⠀⠀⠊⠕⠊⠕⠠⠕⠠⠫⣿⣿⠶⣿⣿⠶⠠⠊⠠⠠⠫⠫⠶⠕⠠⠕⠠⠶⠠⠫⣿⠫⠊⠊⠀⠀⠀⠊⠶⠶⣿⠶⣿⠶⠶⠫⠠⠕⠠⠠⠶⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠕⠕⠕⠠⠶⠊⠀⠊⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠕⠀⠕⠕⠊⠊⠀⠀⠊⠊⠠⠠⠕⠠⠠⠶⠫⠠⠠⣿⠶⠕⠕⠕⠫⠠⠫⠕⠠⠫⠠⠫⠕⠕⠠⠕⠫⠕⠶⠕⠊⠠⠊⠀⠀⠊⠫⠶⣿⣿⣿⣿⣿⠠⠶⠕⠊⠠⠠⠠⠶⠫⣿⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⣿⣿⣿⣿
⠫⣿⠶⠫⠶⠠⠫⠕⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠕⠊⠫⠠⠶⠠⠠⠠⠶⣿⠶⠕⠠⣿⠶⣿⣿⠕⠀⠕⠕⠀⠊⠠⠀⠠⠶⠀⠫⠶⠊⠕⠠⠠⠫⠶⠶⠶⠶⠀⠀⠊⠠⣿⣿⣿⣿⠶⠫⣿⠶⠫⠕⠕⠕⠠⠶⠊⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⠶⠫⠶
⠶⠫⠫⣿⠫⠶⠠⠶⣿⠫⠠⠕⠕⠀⠀⠀⠀⠊⠊⠀⠕⣿⠶⠠⠠⠶⣿⠠⠫⠫⣿⠶⠶⠶⠶⠶⠶⣿⠠⠕⠊⠀⠀⠊⠀⠊⠀⠊⠕⠕⠠⠕⠊⣿⠠⠕⠠⠕⠀⠊⣿⠫⠶⠕⠀⠀⠊⠫⣿⠶⣿⣿⣿⣿⠶⠫⠠⠫⠊⠊⠫⠶⠕⠶⠫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠫⠶⣿
⠫⠫⠫⠊⠠⣿⠶⠶⠊⠫⠶⣿⠶⠶⠶⠠⠶⠠⠊⠀⠀⠕⠠⣿⣿⠠⠠⣿⣿⣿⣿⠶⠠⠫⠶⠫⠕⠀⠀⠀⠀⠀⠕⠕⠊⠀⠠⠫⠫⠠⠠⠀⠠⠫⠶⠫⠫⠠⠶⠕⠀⠫⠫⠀⠕⠀⠀⠕⠫⠫⣿⠶⠫⠫⣿⠕⠠⠫⠊⠀⠠⠠⠕⠕⠫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⠫⠶
⣿⠕⠶⠶⠠⠶⠶⣿⣿⣿⠫⠫⣿⠶⣿⠠⠫⠠⠶⠀⠀⠀⣿⠫⠫⠠⠶⠫⣿⠶⠶⣿⠫⠶⠕⠀⠀⠀⠀⠠⠠⠫⠠⠕⣿⠠⠫⠫⠕⠠⠶⠫⠫⠠⠕⠫⠫⠊⣿⠕⠕⠀⠀⠀⠠⠀⠊⠀⠊⠊⠕⠊⠕⠠⠠⠫⠠⠕⠕⠊⠊⠫⠫⠫⠶⠫⣿⣿⣿⣿⣿⠶⠶⠶⣿⠶⣿⣿⠶⠫
⣿⠶⠶⠫⠶⠠⠊⠠⣿⣿⠫⠫⠶⠶⠫⠕⠶⣿⠕⠀⠀⠀⠠⠶⠫⠶⠫⠶⠫⠶⠠⣿⠶⣿⣿⠕⠀⠀⠠⠫⠠⠫⠶⠫⠶⣿⠫⠫⠠⠶⠫⣿⠠⠫⠊⠫⣿⣿⣿⣿⠶⠕⠠⠀⠊⠀⠊⠀⠕⠀⠊⠀⠠⠕⠕⠕⠕⠕⠠⠕⠕⠕⠕⠶⣿⠕⠫⣿⠫⠫⠶⣿⠶⠶⠕⠶⣿⠫⠫⣿
⠶⠶⣿⠶⠶⣿⠶⠶⠊⠕⠊⠀⠠⠶⣿⠠⠶⠠⠀⠀⠀⠀⠕⠫⠶⠫⠶⣿⠠⠊⠶⣿⣿⣿⣿⠕⠊⠕⠕⠶⠫⠶⠠⠶⠫⠫⣿⠠⠕⠫⠠⠫⠫⠶⠕⠶⣿⠠⠫⠶⣿⠠⠊⠀⠊⠕⠊⠀⠀⠀⠠⠕⠊⠫⠶⠕⠕⠊⠊⠀⠊⠫⠊⠕⠕⠕⠶⠶⠫⠠⠠⠫⠕⠊⠠⠫⠠⠶⠶⣿
⣿⠶⠠⠫⣿⣿⠫⠶⣿⣿⣿⠫⠫⣿⣿⠊⣿⠠⠀⠀⠀⠀⠠⣿⣿⠫⠶⠕⠀⠊⠶⣿⣿⣿⠫⠊⠠⠊⠠⠠⠠⠶⠫⠕⠀⠊⠫⠶⠠⠕⠫⠠⠠⠫⣿⠫⣿⠠⠶⣿⣿⠕⠠⠠⠠⠊⠀⠊⠀⠀⠕⠊⠕⠊⠕⠊⠊⠠⠠⠕⠫⠫⠶⠕⠶⠶⠊⠶⠶⠫⣿⠫⠠⠀⠫⠠⠕⠫⠠⣿
⣿⣿⠶⠫⠶⠶⣿⠶⣿⣿⠶⣿⣿⣿⣿⠀⠫⠠⠀⠀⠀⠀⠕⠠⠊⠀⠕⠕⠀⠀⠊⠊⠠⠠⠕⠊⠕⠕⣿⠶⣿⠶⠶⠕⠕⠕⠕⠠⠶⠕⠕⠠⠶⠠⠕⠶⠶⣿⠶⠕⠊⠊⠕⠶⠊⠊⠠⠠⠊⠀⠊⠊⠠⠕⠕⠊⠕⠊⠫⠕⠠⠫⠫⠠⠠⠕⠕⠠⠠⠠⠠⣿⠀⠀⠕⠕⠠⠫⣿⣿
⣿⠕⠕⠫⣿⠶⠶⠶⣿⣿⣿⣿⣿⣿⣿⠀⠊⠀⠀⠀⠀⠀⠕⠊⠊⠊⠀⠀⠀⠀⠕⠀⠀⠀⠊⠕⠫⠶⣿⣿⣿⠶⠶⠫⠕⠠⠀⠫⠕⠕⠠⠕⠕⠫⠫⠫⠶⠫⠶⠠⠕⠫⠫⣿⠶⣿⣿⠶⠫⠫⣿⠫⠠⠊⠠⠠⠕⠊⠫⠕⠫⠠⠫⠠⠠⣿⣿⣿⠫⠕⠶⠶⠠⠶⣿⣿⣿⣿⣿⣿
⣿⠊⠀⠀⠊⠕⠫⣿⣿⣿⣿⣿⠶⣿⠶⠀⠀⠀⠀⠀⠀⠀⠊⠊⠀⠊⠀⠀⠊⠊⠀⠊⠊⠀⠀⠫⠠⠫⣿⠶⣿⠫⠶⠠⠫⠫⠫⠀⠊⠕⠊⠕⠫⠠⠕⠫⠠⠀⠊⠀⠫⣿⠕⠶⣿⠫⠶⠫⠕⠕⠫⠶⠶⠶⠶⠫⠠⠀⠀⠕⠫⠠⠫⣿⠶⠊⠫⠫⠶⣿⣿⠶⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠊⠊⠠⠫⠠⠕⠫⠊⠀⠊⠠⠕⠕⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠕⠊⠀⠠⠀⠊⠀⠊⠀⠀⠀⠫⠶⠶⣿⠫⣿⠶⠕⠶⠶⣿⣿⠫⠕⠕⠕⠀⠊⠊⠀⠀⠕⠠⠠⠶⠶⣿⣿⠠⠠⠊⠀⠀⠕⠊⠀⠊⠫⠶⠫⠫⠶⠫⠠⠶⠀⠫⠶⠶⠫⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠀⠊⠶⣿⠶⠫⠀⠀⠊⠕⠠⣿⠫⠶⠕⠊⠀⠀⠀⠀⠀⠀⠀⠕⠊⠀⠊⠕⠕⠕⠊⠠⠫⠠⠠⠠⠠⣿⠫⠫⠠⠶⠶⠫⠫⣿⠫⠕⠕⠕⠶⠠⠫⠕⠀⠕⠶⠊⠊⠠⠕⠫⠠⠫⠕⠕⠠⠶⠠⠠⠕⠶⣿⣿⠫⠕⠫⠀⠠⠕⠠⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠀⠕⠫⣿⣿⠕⠕⠊⠠⠠⣿⣿⣿⣿⠫⠀⠀⠀⠀⠀⠀⠀⠀⠊⠕⠕⠫⠠⠕⠫⠫⣿⣿⠫⣿⣿⠶⣿⠶⠠⠫⠊⠶⠶⠶⣿⠶⠫⠠⠶⠠⠫⣿⣿⠶⠶⠕⠫⠕⠊⠊⠫⠠⠠⠶⠶⣿⠶⣿⠠⠶⣿⠫⠶⠫⠫⠕⠊⠫⠫⠶⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⣿⣿⣿⣿⣿⣿⠶
⣿⠕⠀⠊⠊⠊⠕⠠⠠⠠⠶⣿⣿⣿⣿⠫⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠕⠕⠠⠶⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠫⠠⠠⠊⠕⠕⠫⣿⣿⠕⠕⠫⠫⠠⠊⠀⠕⠀⠫⣿⠫⠊⠫⠫⠶⠫⠠⠶⠠⠫⠶⠶⠶⠶⠫⠶⠊⠀⠊⠠⣿⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⠶⣿⣿
⣿⠕⠊⠀⠫⠊⠊⠠⠫⠕⠕⣿⣿⣿⣿⠕⠊⠀⠀⠀⠀⠀⠀⠀⠊⠊⠠⠕⠕⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⠶⠊⠊⠕⠕⠕⠫⠶⠕⠀⠊⠀⠀⠀⠊⠕⠕⠀⠕⠫⠀⠊⠫⠠⠫⠠⠠⠕⠫⠫⠶⠶⠫⠶⠕⠀⠀⠶⣿⠶⣿⣿⣿⣿⣿⣿⣿⠶⣿⣿⠶⣿⠶⠶⠠⠕⠕⠕⠶
⣿⠀⠊⠀⠀⠊⠊⠠⠠⠕⠠⠊⠕⠕⠫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠕⠠⠠⣿⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⠶⠀⠀⠀⠊⠀⠊⠫⠠⠀⠠⠊⠕⠊⠠⠠⠊⠊⠀⠠⠕⠊⠊⣿⣿⠠⠫⣿⠶⠫⠶⠶⠶⠠⠊⠕⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠫⠠⠶⣿⠕⠊⠀⠀⠀⠀⠀⠀⠕
⣿⠕⠀⠀⠀⠠⠊⠊⠊⠊⠊⠀⠕⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠠⠕⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⠶⠀⠊⠕⠊⠊⠕⠊⠊⠕⠠⠊⠊⠊⠀⠊⠕⠊⠊⠕⠕⠠⠠⠫⣿⠠⠠⠊⠠⠊⠊⠕⠶⠠⠶⣿⣿⣿⣿⣿⣿⣿⣿⠶⠫⠶⠶⠶⠠⠶⠠⠀⠀⠀⠀⠀⠀⠀⠕
⣿⠕⠊⠊⠊⠠⠫⠫⠕⠊⠀⠊⠊⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠕⠀⠊⠊⠫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠫⠕⠫⠶⠠⠫⠀⠀⠠⠊⠫⠶⠊⠠⠀⠠⠫⠶⣿⠫⣿⠫⠫⣿⠶⣿⣿⣿⠶⣿⣿⣿⣿⣿⣿⣿⣿⠶⣿⣿⣿⣿⠶⠠⣿⣿⠫⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠠⠊⠕⠶⠶⣿⣿⠶⠕⠀⠀⠊⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠕⠊⠕⠠⠕⠫⣿⠶⣿⣿⣿⣿⠶⣿⣿⠶⠕⠊⠕⠕⠠⠠⠫⠫⠫⠫⠶⠕⠕⠕⠶⣿⣿⣿⣿⣿⣿⠫⠶⣿⣿⣿⣿⣿⣿⠫⣿⣿⠫⣿⣿⣿⣿⠶⣿⠶⠠⠫⣿⣿⠶⣿⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⠶⣿⠶⣿⣿⣿⣿⠶⠕⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠊⠶⠀⠕⠫⣿⣿⣿⣿⣿⣿⠠⠫⠫⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⠫⣿⣿⣿⣿⠶⠶⠶⣿⣿⣿⣿⣿⠶⠶⣿⣿⣿⣿⠶⣿⠫⣿⣿⣿⠫⠶⠠⠫⠫⠕⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊
⠶⠶⠫⠫⠠⠫⣿⣿⣿⣿⣿⣿⣿⠫⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠊⠕⠊⠕⠊⠕⠠⠶⠠⠫⣿⣿⣿⣿⣿⣿⠶⠫⣿⠶⠫⠫⠶⠶⣿⣿⣿⣿⠶⠕⠀⠕⠠⠫⠠⠫⠫⠫⠫⠫⠫⠶⠶⣿⠠⠫⠠⠠⠕⠕⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠕⠠⠊⠫⠠⠕⠕⠕⠀⠕⠊
⣿⠶⠠⠕⠶⠶⠶⣿⠶⣿⣿⣿⣿⣿⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠫⣿⠶⣿⣿⣿⣿⣿⣿⣿⣿⠶⣿⠶⠠⠕⠕⠊⠫⣿⠫⠫⠫⠫⠠⠫⠶⠫⠠⠠⠊⠕⠊⠀⠀⠀⠊⠀⠀⠀⠊⠀⠊⠀⠀⠊⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠕⠕⠕⠕⠕⠊⠕⠠⠕⠠⠕⠠⠊⠠
⣿⠶⠠⠠⠠⠶⠫⠕⠶⠫⠶⣿⠠⠫⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠶⣿⣿⣿⣿⣿⣿⠠⠕⠀⠠⠠⠫⠕⠫⠫⠫⠫⠠⠕⠕⠊⠠⠠⠕⠕⠀⠀⠊⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠕⠊⠊⠀⠠⠠⠀⠠⠕⠊⠕⠫⠊⠊⠊⠫
⣿⠫⠕⠕⠊⠊⠊⠶⠶⠊⠫⠶⣿⠫⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠊⠶⠫⠶⠫⠶⠕⠕⠊⠕⠊⠊⠕⠠⠊⠕⠫⠊⠕⠶⠫⠕⠠⠕⠠⠀⠊⠀⠀⠀⠀⠊⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠕⠊⠕⠫⠕⠊⠫⠫⠠⠠⠊⠊⠕⠕⠀⠫
⣿⠠⠊⠊⠀⠀⠕⠶⠫⠠⠫⠕⠫⠠⠶⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠶⠊⠕⠊⠀⠀⠀⠀⠀⠕⠠⠠⠕⠀⠠⠀⠀⠀⠠⠀⠀⠀⠀⠊⠀⠊⠀⠀⠀⠀⠀⠀⠀⠕⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠊⠀⠀⠠⠠⠠⠫⠠⠶⠕⠕⠫⠊⠊⠀⠀⠀
⠶⠊⠠⠊⠫⠀⠕⠠⠀⠠⠕⠊⠕⠶⠫⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠊⠀⠀⠀⠀⠀⠊⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠊⠀⠠⠀⠀⠀⠀⠀⠀⠀⠊⠀⠊⠀⠊⠀⠊⠊⠊⠠⠕⠀⠊⠠⠊⠀⠀⠊⠀⠀⠀⠊⠫⠶⠕⠕⠕⠶⠕⠕⠕⠊⠕⠕⠀⠠
⠠⠀⠀⠀⠀⠕⠕⠕⠕⠕⠕⠊⠀⠀⠊⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠊⠀⠀⠕⠀⠀⠀⠀⠀⠀⠀⠀⠊⠊⠊⠀⠀⠀⠀⠀⠀⠀⠕⠀⠊⠀⠊⠊⠕⠊⠊⠊⠊⠀⠫⠕⠕⠀⠠⠕⠕⠠⠕⠠⠕⠕⠫
⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠕⠀⠀⠊⠀⠊⠀⠊⠠⠠⠊⠕⠕⠀⠕⠀⠀⠀⠀⠀⠊⠊⠀⠀⠀⠀⠀⠀⠀⠕⠠⠊⠀⠊⠊⠀⠕⠀⠀⠕⠊⠕⠕⠠⠠⠠⠕⠠⠊⠠⠕⠠
⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠕⠕⠀⠊⠕⠀⠀⠠⠫⠀⠕⠕⠀⠕⠊⠕⠊⠊⠊⠊⠊⠊⠀⠀⠊⠠⠶⠠⠊⠕⠀⠫⠕⠀⠀⠀⠊⠀⠀⠕⠠⠕⠕⠕⠫⠕⠠⠀⠀⠕⠕
⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠕⠀⠀⠀⠀⠀⠀⠀⠕⠕⠀⠠⠊⠊⠊⠀⠊⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠊⠀⠀⠀⠕⠊⠀⠀⠀⠀⠀⠀⠕⠫⠫⠕⠊⠊⠀⠊⠕⠕⠊⠀⠊
⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠕⠀⠕⠊⠀⠀⠀⠊⠕⠀⠠⠀⠀⠀⠊⠀⠀⠀⠀⠊⠕⠊⠊⠊⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠊⠀⠕⠀⠀⠊⠊⠕⠕⠕⠀⠀⠕⠕⠠⠠⠊
⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠫⠕⠕⠀⠫⠕⠶⠀⠀⠀⠊⠊⠀⠕⠀⠀⠊⠀⠀⠀⠀⠀⠀⠕⠀⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠫⠀⠀⠊⠀⠊⠀⠀⠠⠊⠕⠕⠀⠕
⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠊⠀⠀⠀⠀⠊⠊⠀⠕⠕⠀⠕⠊⠕⠊⠀⠀⠊⠀⠊⠊⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠕⠊⠀⠊⠊⠀⠀⠀⠀⠀⠊⠀⠀⠕⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠕⠀⠊⠀⠀⠊⠕⠕⠠⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠊⠊⠕⠊⠕⠊⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠕⠊⠊⠀⠀⠀⠀⠀⠀
⠊⠀⠀⠀⠀⠀⠀⠀⠕⠊⠊⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠊⠀⠕⠀⠀⠀⠕⠫⠫⠠⠀⠀⠀⠀⠊⠕⠕⠊⠕⠠⠠⠊⠕⠕⠊⠕
⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠕⠕⠊⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠊⠫⠫⠕⠕⠕⠀⠊⠊⠕⠀⠊⠀⠕⠊⠀⠀⠀⠕⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠊⠀⠊⠊⠀⠕⠀⠊⠕⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠊⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊
⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠊⠀⠕⠀⠀⠊⠊⠀⠀⠀⠀⠊⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠊⠀⠕⠕⠊⠀⠊⠊⠀⠀⠀⠀⠀⠊⠊⠀⠀
⠕⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠕⠊⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠊⠀⠀⠊⠀⠀⠀⠀⠀⠠⠕⠊⠊⠊⠕⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠕⠕⠕⠊⠠⠠⠕⠀⠀⠊⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀




## License

This project is licensed under the MIT License.
