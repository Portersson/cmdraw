import sys
class Window(object):
    def __init__(self, width, height):
        self.width = width-1
        self.height = height
        self.modified = True
        #Create a 2D array scaled to terminal's lines and columns.
        self.rect = [[' ' for i in range(self.width)]
                     for i in range(self.height)]
        self.rect_buffer = []

    def update(self):
        """Print self.rect if a change has been made"""
        #check for any difference between buffer and live rects
        for y in range(len(self.rect)):
            for x in range(y):
                if self.rect[x] != self.rect_buffer[x]:
                    self.modified = True
                    break

        if self.modified:
            self.rect = self.rect_buffer
            block = ""
            for line in self.rect:
                block += '\n'
                for char in line:
                    block += char
            sys.stdout.write(block)
            self.modified = False
        #sys.stdout.flush()

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
        self.rect_buffer = [[' ' for i in range(self.width)]
                     for i in range(self.height)]

    def draw(self, *args, x,y):
        """Modifies given rect according to args given"""
        if isinstance(args[0], str):
            string = args[0]
            for i in range(len(string)):
                self.rect_buffer[int((y)%self.height)][int(x+i)%self.width] = string[i]

            
