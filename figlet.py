import sys
import random
from pyfiglet import Figlet
import argparse

def main():
    # Initialize Figlet instance
    figlet = Figlet()

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Render text in different Figlet fonts", exit_on_error=False)
    parser.add_argument("-f", "--font", help="Font to use for rendering", nargs="?")    
    args, unknown = parser.parse_known_args()
    fonts = figlet.getFonts()
    
    # Determine which font to use
    if args.font is not None and args.font in fonts:
        figlet.setFont(font=args.font)
    elif args.font is not None and args.font not in fonts:
        print("Unknown font")
        sys.exit()
    elif unknown:
        print("Unknown argument")
        sys.exit()
    else:
        figlet.setFont(font=random.choice(figlet.getFonts()))
    
    # Setup input
    text = input("Text: ")
    # Render the text
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()