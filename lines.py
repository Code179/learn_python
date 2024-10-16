import sys

def main():
  filename = get_filename_from_argv(sys.argv)
  total_lines_of_code = count_lines_of_code(filename)
  print(total_lines_of_code)

def count_lines_of_code(filename):
  # Give me a placeholder for counting the code lines
  lines_of_code = 0
  
  # Try to open the file the user entered as a cmd arg
  try: 
    with open(filename) as file:
      # Give me the content of each line of that file in a list/array
      lines = file.readlines() 
      # Loop through every line of that file
      for line in lines:
        # Remove any whitespace from every line
        # Reason for that is that no line can start with one or more whitespace 
        # which allows us to check if a line is a comment or not without
        # being misguided by whitespaces
        line = line.strip()
        # If a line contains content and it does not start with # like a comment 
        # then update lines_of_code placeholder
        if line and not line.startswith("#"):
          lines_of_code +=1
    # Return the finished result after the loop is finished going through/looping      
    return lines_of_code
  # If the file does not exist then exit with "File not Found" as custom error message
  except FileNotFoundError:
    raise FileNotFoundError("File not found")

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