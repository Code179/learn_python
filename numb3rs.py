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
    # Define the regex patterns for each octet
    octet_range = r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)"

    # Combine the octet pattern with dots
    regex = rf"^{octet_range}\.{octet_range}\.{octet_range}\.{octet_range}$"

    if re.search(regex, ip):
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
