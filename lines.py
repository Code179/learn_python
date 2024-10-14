import sys

def main():
  filename = get_filename_from_argv(sys.argv)
  total_lines_of_code = count_lines_of_code(filename)
  print(total_lines_of_code)

def count_lines_of_code(filename):
  lines_of_code = 0
  try: 
    with open(filename) as file:
      lines = file.readlines()
      for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
          lines_of_code +=1
    return lines_of_code
  except FileNotFoundError:
    sys.exit("File not found")

def get_filename_from_argv(args):
  if len(args) > 2:
    sys.exit("Too many arguments")
  elif len(args) < 2:
    sys.exit("Too few arguments")
  elif len(args) == 2 and not args[1].endswith(".py"):
    sys.exit("Not a Python File")
  else:
    return args[1]


if __name__ == "__main__":
  main()