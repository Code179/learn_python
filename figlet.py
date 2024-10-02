import sys
import random
from pyfiglet import Figlet
import argparse

def main():
    # Initialize Figlet instance
    figlet = Figlet()

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Render text in different Figlet fonts")
    # parser.add_argument("text", help="Text to render")
    parser.add_argument("-f", "--font", help="Font to use for rendering", choices=figlet.getFonts())
    args = parser.parse_args()

    # Setup input
    text = input("Text: ")

    # Determine which font to use
    if args.font:
        figlet.setFont(font=args.font)
    else:
        figlet.setFont(font=random.choice(figlet.getFonts()))

    # Render the text
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()