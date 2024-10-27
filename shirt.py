import sys
import os
from PIL import Image, ImageOps

# TO-DO: Write function that handles FileNotFound
# TO-DO: Waschmaschine entleeren

def main():
    handle_cmd_args(sys.argv)
    output_image = sys.argv[2]
    input_image = sys.argv[1]

    try:
      shirt = Image.open("shirt.jpg")
      with Image.open(input_image) as im:
        shirt_size = shirt.size
        input_image_cropped = ImageOps.fit(im,shirt_size)
        input_image_cropped.paste(shirt, shirt)
        input_image_cropped.save(output_image)
    except FileNotFoundError:
      sys.exit("File not found while opening")

def handle_cmd_args(args):
  _, input_image_ext = os.path.splitext(args[1])
  _, output_image_ext = os.path.splitext(args[2])
  try:
    if len(args) > 3:
      raise sys.exit("Too many arguments")
    elif len(args) < 3:
      raise sys.exit("Too few arguments")
    elif not input_image_ext.lower().endswith((".jpg", ".jpeg", ".png")) or not output_image_ext.lower().endswith((".jpg", ".jpeg", ".png")):
      raise sys.exit("Not a JPG or PNG File")
    elif output_image_ext != input_image_ext:
      raise sys.exit("Output ext different than input ext") 
    else:
      return args[1], args[2]
  except SystemExit as e:
    raise sys.exit(e)

if __name__ == "__main__":
    main()