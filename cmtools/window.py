from threading import Thread
from msvcrt import getch
from os import system
import cmtools
import colorama
import time
import shutil
import sys

class Window(object):
    def __init__(self, width, height):
        self.width = width+1
        self.height = height+1

        self.key = 0
        self.exit = False

        self.t = Timer()

        #Prepare terminal by resizing and clearing.
        system('mode con:cols=%d lines=%d'%(self.width+1,self.height))
        system('cls')
        colorama.init()

        #Start new thread that listens for keypresses.
        keyRead = Thread(target = self.getKeypress)
        keyRead.daemon = True
        keyRead.start()

        #Create a 2D array scaled to terminal's lines and columns.
        self.rect = [[' ' for i in range(self.width)]
                     for i in range(self.height)]
        self.clear()

    def update(self):
        """print to screen"""
        pos = lambda y, x: '\x1b[%d;%dH' % (y+1, x+1)

        for line in range(len(self.rect)):
            for char in range(len(self.rect[line])):
                if self.rect[line][char] != self.rect_buffer[line][char]:
                    print(pos(line, char), end='')
                    print(self.rect_buffer[line][char],end='')
        print(pos(self.height-1,self.width-1),end='')

        self.rect=self.rect_buffer

    def border(self):
        """outline the rect with an x every other cell"""
        for count, line in enumerate(self.rect_buffer):
            if (count == 0 or count == len(self.rect_buffer)-1):
                for x in range(0, len(line), 2):  #For ever other item in line
                    line[x] = 'x'
            line[-1] = 'x'
            line[0] = 'x'

    def clear(self):
        """empty the buffer"""
        self.rect_buffer = [['' for i in range(self.width)]
                     for i in range(self.height)]

    def write(self, *args, x,y):
        """write changes to self.rect"""
        if isinstance(args[0], str):
            string = args[0]
            for i in range(len(string)):
                self.rect_buffer[y%self.height][int(x+i)%self.width] = string[i]

    def getKeypress(self):
        """Assign self.key to last keypress"""
        t = Timer()
        while not self.exit:
            if t.time_has_elapsed(5):
                self.key = ord(getch())
            if self.key == 3:
                self.exit = True


class Timer(object):
    def __init__(self):
        self.split = self.current_time()

    def time_has_elapsed(self, wait_time):
        """Returns True after 'wait_time' ms has elapsed since last True."""
        if(self.current_time()-self.split>wait_time):
            self.split=self.current_time()
            return True

    def current_time(self):
        return int(round(time.process_time()*1000))
