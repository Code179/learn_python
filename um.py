import re

# TO-DO: implement a function called count that expects a line of text as input as a str
# TO-DO: returns, as an int, the number of times that “um” appears in that text, case-insensitively
# TO-DO: words like "yummy" should return 0

"""
1. We create a pattern that searches for "um" 
2. We group that pattern
3. The result of that is a tuple the amount of "um"
4. We take the length of that tuple and have our desired result
5. The pattern distinguishes between "yummy" and "hello, um, "
6. "Yummy" doesnt count as "um"
"""

def main():
    string = input("Enter text: ")
    um_amount = count(string)
    print(um_amount)

def count(s):
    pattern = r"\b(um)\b"
    if match := re.findall(pattern, s):
        return len(match)
    else:
        return 0

if __name__ == "__main__":
    main()