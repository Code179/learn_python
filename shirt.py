import sys

def main():
    print("Hello, World")
    handle_cmd_args(sys.argv)

def handle_cmd_args(args):
  try:
    if len(args) > 3:
      raise sys.exit("Too many arguments")
    elif len(args) < 3:
      raise sys.exit("Too few arguments")
    elif len(args) == 3 and (not args[1].endswith((".jpg", ".png")) or not args[2].endswith((".jpg", ".png"))):
      raise sys.exit("Not a JPG or PNG File")
    else:
      return args[1], args[2]
  except SystemExit as e:
    raise sys.exit(e)

if __name__ == "__main__":
    main()