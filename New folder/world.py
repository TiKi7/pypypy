#
# world page!
#
from Points import Points
import random as rd

class World:
    
    w = 9
    h = 9
    
    def __init__(self):
        self._pts = Points()
        # set force to False not to overWrite other datas!
        self._pts.force = False
        self.scan(0, 0)
        
    # run Once to create() world around 2B or (0,0) #
    def create(self, i, j):
        unit_state = rd.randint(0,3)
        self._pts.add(i,j, unit_state)
    
    # display the world after each creation #
    def display(self, i, j):
        u = self._pts.call(i, j)
        print(u if u != 0 else ' ', end=' ')
    
    # scan the world #
    def scan(self, x, y ):
        #----- where to scan -----#
        for j in range(self.h):
            j = j - self.h // 2 + y
            for i in range(self.w):
                i = i - self.w // 2 + x
                #----- what to do -----#
                self.create(i, j)
                if (i,j) != (x,y): # while point isn't in (x,y)
                    self.display(i, j)
                else:
                    print('█', end=' ')
            print('')