import sys

def main():
  filename = sys.argv[1]
  lines_of_code = 0
  with open(filename) as file:
    lines = file.readlines()
    for line in lines:
      line = line.strip()
      if line != "\n":
        if not line.startswith("#"):
          lines_of_code +=1
    print(lines_of_code)

if __name__ == "__main__":
  main()