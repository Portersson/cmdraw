#python 3
import cmtools
import random

class Tree(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.charset = [' ','T','&']
        self.display = self.charset[0]
        self.display_buffer = self.display
        self.neighbors = []

    def get_neighbors(self,forest):
        for i in range(len(forest)):
            if abs(forest[i].x - self.x) <= 1 and abs(forest[i].y - self.y) <= 1:
                self.neighbors.append(forest[i])

    def tick(self,rate):
        self.display_buffer = self.display
        self.chanceToBloom = 0.00001

        if self.display == self.charset[1]:
            self.chanceToBloom+=0.00002
        if self.display == self.charset[2]:
            self.chanceToBloom = 1
        for neighbor in self.neighbors:
            if neighbor.display_buffer == self.charset[2] and self.display == self.charset[1]:
                self.chanceToBloom = 1
            elif neighbor.display_buffer == self.charset[1] and self.display == self.charset[0]:
                self.chanceToBloom += 0.0006
        self.chanceToBloom = self.chanceToBloom*(rate/60)*1 #chance is adjusted to corrospond with how fast game updates

        if random.random() <= self.chanceToBloom:
            self.display = self.charset[(self.charset.index(self.display)+1)%3]

def main():
    #init
    (width, height) = (72,27)
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