#
# making the SEKAI !
#
import random as rd

class World:
    
    def __init__(self):
        self.memo = {}  # {'x,y':unit_state, ...
        self.width, self.height = 3, 4
        print('World.__init__@done')
        self.w = 3
        self.h = 3
    
    
    def update(self, me):
        
        x = me.position['x']
        y = me.position['y']
        print(str(x), str(y))
        
        w = self.w
        h = self.h
        
        #----- scanning the area -----#
        for i in range(h):
            i = y + i - h//2
            for j in range(w):
                j = x + j - w//2
                address = str(j) + ',' + str(i)
                #
                # we should not update the position and the cells_
                # which have state already!
                #
                if (j,i) != (x,y) and address not in self.memo.keys():
                    unit_state = rd.randint(0,2)
                    self.memo[ address ] = unit_state
                    
        print(self.memo)