from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
figlet_fonts = figlet.getFonts()

def main():
    str = input("Enter a text: ")
    render_text(sys.argv, str)

def render_random(str):
    font = random.choice(figlet_fonts)
    figlet.setFont(font=font)
    print(figlet.renderText(str))

def render_accurate(str, font):
    figlet.setFont(font=font)
    print(figlet.renderText(str))

def render_text(argv, str):
    if len(argv) == 1:
        render_random(str)
    elif len(argv) >= 3 and (argv[1] == "-f" or argv[1] == "--font"):
        render_accurate(str, argv[2])
    else:
        sys.exit()

        
        
if __name__ == "__main__":
    main()