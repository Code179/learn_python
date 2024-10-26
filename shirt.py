import sys
import os

def main():
    print("Hello, World")
    handle_cmd_args(sys.argv)

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