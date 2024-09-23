import sys
from PIL import Image, ImageOps
from os import path

if len(sys.argv) != 3:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

ending = [".jpg", ".jpeg", ".png"]
file1 = path.splitext(sys.argv[1].lower())[-1]
file2 = path.splitext(sys.argv[2].lower())[-1]

if file1 not in ending:
    sys.exit("Invalid input")
elif file2 not in ending:
    sys.exit("Invalid output")
elif file1 != file2:
    sys.exit("Input and output have different extensions")

try:
    input_image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")
size = shirt.size
resized_input = ImageOps.fit(input_image, size)
resized_input.paste(shirt, shirt)
resized_input.save(sys.argv[2])