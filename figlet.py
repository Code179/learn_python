import sys
import random
from pyfiglet import Figlet

SHORT_FONT_ARG = "-f"
LONG_FONT_ARG = "--font"

def main():
    # Initialize Figlet instance
    figlet = Figlet()
    fonts = figlet.getFonts()
    args = sys.argv
    
    if len(args) == 1:
        # No font specified, use random font
        render_with_random_font(figlet)
    elif len(args) == 3:
        # Handle specific font request
        handle_font_request(figlet, fonts, args)
    elif len(args) == 2 and (args[1] == SHORT_FONT_ARG or args[1] == LONG_FONT_ARG):
        # Font flag provided but no font specified
        print("Error: No font provided.")
        sys.exit(1)
    else:
        # Invalid argument
        print("Error: Unknown argument.")
        sys.exit(1)

def handle_font_request(figlet, fonts, args):
    if args[1] in [SHORT_FONT_ARG, LONG_FONT_ARG]:
        font = args[2]
        if font in fonts:
            render_text(figlet, font)
        else:
            print("Error: Unknown font.")
            sys.exit(1)

def render_with_random_font(figlet):
    font = random.choice(figlet.getFonts())
    render_text(figlet, font)

def render_text(figlet, font):
    text = input("Enter text to render: ")
    figlet.setFont(font=font)
    print(figlet.renderText(text))
    
if __name__ == "__main__":
    main()