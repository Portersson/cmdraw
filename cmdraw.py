#python 3
from os import system
import cmtools
import shutil
import sys

def main():
    screen = cmtools.Window(50, 24)

    t = cmtools.Timer()
    while not screen.exit:
        if t.time_elapsed(60):
            screen.clear()
            screen.draw(str(screen.key), x = int(width/2)-len(str(screen.key))/2, y = int(height/2))
            screen.border()
            screen.update()

if __name__ == "__main__":
    main()