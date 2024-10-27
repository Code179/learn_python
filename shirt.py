import os
import sys
from PIL import Image, ImageOps

def main():
    input_image, output_image = get_cmd_args(sys.argv)
    try:
      shirt = Image.open("shirt.jpg")
      with Image.open(input_image) as im:
        shirt_size = shirt.size
        input_image_cropped = ImageOps.fit(im,shirt_size)
        input_image_cropped.paste(shirt, shirt)
        input_image_cropped.save(output_image)
    except FileNotFoundError:
      sys.exit("File not found while opening")

def get_cmd_args(args) -> tuple:
    """Get command line arguments and return input and output image file names."""
    if len(args) != 3:
        raise ValueError("Usage: script.py <input_image> <output_image>")
    
    input_image, output_image = args[1], args[2]
    validate_file_extensions(input_image, output_image)
    return input_image, output_image

def validate_file_extensions(input_image: str, output_image: str):
    """Validate the file extensions of the input and output images."""
    input_ext = os.path.splitext(input_image)[1].lower()
    output_ext = os.path.splitext(output_image)[1].lower()
    
    if not input_ext.endswith((".jpg", ".jpeg", ".png")) or not output_ext.endswith((".jpg", ".jpeg", ".png")):
        raise ValueError("Both input and output must be JPG or PNG files.")
    if output_ext != input_ext:
        raise ValueError("Output file extension must match input file extension.")

if __name__ == "__main__":
    main()