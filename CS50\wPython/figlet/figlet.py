from pyfiglet import Figlet
import random
import sys

figlet = Figlet()


def figlet_text():
    if sys.argv[2] in figlet.getFonts():
        text = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        return figlet.renderText(text)
    else:
        sys.exit("Invalid usage")


def figlet_text_random():
    text = input("Input: ")
    rand_font = random.choice(figlet.getFonts())
    figlet.setFont(font=rand_font)
    return figlet.renderText(text)


def check():
    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        print(figlet_text())
    elif len(sys.argv) == 1:
        print(figlet_text_random())
    else:
        sys.exit("Invalid usage")


check()