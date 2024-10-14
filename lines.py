import sys

def main():
  filename = sys.argv[1]
  total_lines_of_code = count_lines_of_code(filename)
  print(total_lines_of_code)

def count_lines_of_code(filename):
  lines_of_code = 0
  with open(filename) as file:
    lines = file.readlines()
    for line in lines:
      line = line.strip()
      if line and not line.startswith("#"):
        lines_of_code +=1
  return lines_of_code

if __name__ == "__main__":
  main()