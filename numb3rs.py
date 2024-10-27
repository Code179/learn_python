import re
import sys

# Format of IPv4 Address: #.#.#.#.
# Validate Function expects a string in that format
# Each # should be a number between 0 and 255 inclusivly
# If number less than 0 or higher than 255, print not in range
# Validate returns True or False

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    regex = r"^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)$"
    if re.search(regex, ip):
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
