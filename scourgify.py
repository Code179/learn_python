import sys
import csv

def main():
    filename, new_filename = handle_cmd_args(sys.argv)
    csv_data = read_csv(filename)
    modified_csv_data = modify_csv_data(csv_data)
    write_csv(modified_csv_data, new_filename)


def modify_csv_data(csv):
    new_list = []
    for column in csv:
      first, last = map(str.strip, column["name"].split(","))
      house = column["house"].strip()
      new_entry = {"first_name": first, "last_name": last, "house": house}
      new_list.append(new_entry)
    return new_list
def write_csv(data, filename):
  with open(filename, 'w', newline='') as file:
    fieldnames = ['first_name', 'last_name', 'house']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)
def read_csv(filename):
  csv_content = []
  try:
    with open(filename) as file:
      # The reader variable contains now a list of a list of the rows from the csv file
      reader = csv.DictReader(file)
      for read in reader:
        csv_content.append(read)
    return csv_content
  except FileNotFoundError:
    sys.exit("File Not Found")

def handle_cmd_args(args):
  try:
    if len(args) > 3:
      raise sys.exit("Too many arguments")
    elif len(args) < 3:
      raise sys.exit("Too few arguments")
    elif len(args) == 3 and (not args[1].endswith(".csv") or not args[2].endswith(".csv")):
      raise sys.exit("Not a CSV File")
    else:
      return args[1], args[2]
  except SystemExit as e:
    raise sys.exit(e)
  
if __name__ == "__main__":
    main()
