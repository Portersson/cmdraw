#python 3
from os import system
import cmtools
import shutil
import sys

def main():
    #Prepare terminal by resizing and clearing.
    system('mode con:cols=50 lines=24')
    system('cls')
    (width, height) = shutil.get_terminal_size() 

    screen = cmtools.Window(width, height)

    t = cmtools.Timer()
    while not screen.exit:
        if t.time_elapsed(60):
            screen.clear()
            screen.draw(str(screen.key), x = int(width/2)-len(str(screen.key))/2, y = int(height/2))
            screen.border()
            screen.update()

if __name__ == "__main__":
    main()