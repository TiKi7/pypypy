#
# making the SEKAI !
#
import random as rd

class World:
    
    x_y = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]
    
    def __init__(self):
        self.memo = {}  # {'x,y':unit_state, ...
        self.width, self.height = 3, 4
        print('World.__init__@done')
        self.w = 3
        self.h = 3
    
    
    def update(self, me):
        
        x = me.position['x']
        y = me.position['y']
        #----- scanning the area -----#
        
        for locs in self.x_y:
            Xi = locs[0] + x
            Yi = locs[1] + y
            address = str(Xi) + ',' + str(Yi)
            
            #----- Writing -----#
            if address not in self.memo.keys():
                unit_state = rd.randint(0,3)
                self.memo[ address ] = unit_state
        
        #print(self.memo)