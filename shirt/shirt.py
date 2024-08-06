# Import necessary modules
from PIL import Image, ImageOps
import sys
import os

# Make sure the program is invoked correctly
if len(sys.argv) != 3:
    print("Usage: python shirt.py input.jpg output.jpg")
    sys.exit(1)

# Extract input and output filenames
input_file = sys.argv[1]
output_file = sys.argv[2]

# Make sure both input and output files have the same extensions and the extension is one of the permitted ones
input_ext = os.path.splitext(input_file)[1].lower()
output_ext = os.path.splitext(output_file)[1].lower()

valid_extensions = ['.jpg', '.jpeg', '.png']

if input_ext != output_ext or input_ext not in valid_extensions or output_ext not in valid_extensions:
    print("Invalid input or output")
    sys.exit(1)

# Open the shirt image
try:
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    print("Shirt image does not exist")
    sys.exit(1)

# Open the input image
try:
    photo = Image.open(input_file)
except FileNotFoundError:
    print("Input does not exist")
    sys.exit(1)

# Resize and crop the input image to fit the shirt
photo = ImageOps.fit(photo, shirt.size)

# Overlay the shirt onto the input image
photo.paste(shirt, mask=shirt)

# Save the resulting image
photo.save(output_file)
