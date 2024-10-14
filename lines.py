import sys

def main():
  filename = sys.argv[1]
  code_count = count_lines_of_code(filename)
  print(code_count)

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