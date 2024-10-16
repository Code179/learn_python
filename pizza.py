import sys

def main():
    filename = get_filename_from_argv(sys.argv)

def get_filename_from_argv(args):
  try:
    if len(args) > 2:
      raise sys.exit("Too many arguments")
    elif len(args) < 2:
      raise sys.exit("Too few arguments")
    elif len(args) == 2 and not args[1].endswith(".py"):
      raise sys.exit("Not a Python File")
    else:
      return args[1]
  except SystemExit as e:
    raise sys.exit(e)

if __name__ == "__main__":
    main()
