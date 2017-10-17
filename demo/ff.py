#python 3

#Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))

import cmtools
import random

class Tree(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.charset = {'empty':' ','alive':'T','ablaze':'&'}
        self.display = self.charset['empty']
        self.display_buffer = self.display
        self.neighbors = []

    def get_neighbors(self,forest):
        for i in range(len(forest)):
            if abs(forest[i].x - self.x) <= 1 and abs(forest[i].y - self.y) <= 1:
                self.neighbors.append(forest[i])

    def tick(self,rate):
        self.display_buffer = self.display
        self.bloomChance = 0.00001
        self.igniteChance = 0.00001

        for neighbor in self.neighbors:
            if neighbor.display_buffer == self.charset['ablaze']:
                self.igniteChance = 1
            elif neighbor.display_buffer == self.charset['alive']:
                self.bloomChance += 0.0006
        self.bloomChance = self.bloomChance*(rate/60) #chance is adjusted to corrospond with how fast game updates

        if self.display == self.charset['ablaze']:
            self.display = self.charset['empty']

        elif random.random() <= self.bloomChance and self.display == self.charset['empty']:
            self.display = self.charset['alive']

        elif random.random() <= self.igniteChance and self.display == self.charset['alive']:
            self.display = self.charset['ablaze']

def main():
    #init
    (width, height) = (72,27)#72,27
    screen = cmtools.Window(width, height)
    rate = 60

    #create forest
    forest = []
    for i in reversed(range(width*height)):
        forest.append(Tree(i%width,i//width))
    for tree in forest:
        tree.get_neighbors(forest)

    timer = cmtools.Timer()
    while not screen.exit:
        #after sufficient time has passed, run game loop
        if timer.time_has_elapsed(rate):
            screen.clear()
            for tree in forest:
                tree.tick(rate)
                screen.write(tree.display, x = tree.x, y = tree.y)

            screen.update()

if __name__ == "__main__":
    main()
