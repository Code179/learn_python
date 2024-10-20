import sys
from tabulate import tabulate
import csv

def main():
    filename = get_filename_from_argv(sys.argv)  
    tabulated = format_list(filename)
    print(tabulated)

def format_list(filename):
    try:
      with open(filename) as file:
        reader = csv.reader(file)
        headers = next(reader)
        return tabulate(reader, headers, tablefmt="grid")
    except FileNotFoundError:
      sys.exit("File Not Found")

def get_filename_from_argv(args):
  try:
    if len(args) > 2:
      raise sys.exit("Too many arguments")
    elif len(args) < 2:
      raise sys.exit("Too few arguments")
    elif len(args) == 2 and not args[1].endswith(".csv"):
      raise sys.exit("Not a CSV File")
    else:
      return args[1]
  except SystemExit as e:
    raise sys.exit(e)

if __name__ == "__main__":
    main()
