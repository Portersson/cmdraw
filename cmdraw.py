#python 3
from threading import Thread
from msvcrt import getch
from os import system
import cmtools
import shutil
import time
import sys

exitapp = False  #Flag which second thread is controlled by.
key = 0  #Code for keypress currently being held down.


class Timer(object):
    def __init__(self):
        self.split = self.current_time()

    def time_elapsed(self, wait_time):
        """Returns True after 'wait_time' ms has elapsed since last True."""
        if(self.current_time()-self.split>wait_time):
            self.split=self.current_time()
            return True

    def current_time(self):
        return int(round(time.process_time()*1000))

def getKeypress():
    global key, exitapp
    t = Timer()
    while not exitapp:
        if t.time_elapsed(5):
            key = ord(getch())
        if key == 3:
            exitapp = True

def main():
    #Prepare terminal by resizing and clearing.
    system('mode con:cols=50 lines=24')
    system('cls')
    (width, height) = shutil.get_terminal_size() 

    screen = cmtools.Window(width, height)

    #Start new thread that listens for keypresses.
    keyRead = Thread(target = getKeypress)
    keyRead.daemon = True
    keyRead.start()

    t = Timer()
    while not exitapp:
        if t.time_elapsed(60):
            screen.clear()
            screen.draw(str(key), x = int(width/2)-len(str(key))/2, y = int(height/2))
            screen.border()
            screen.update()

if __name__ == "__main__":
    main()