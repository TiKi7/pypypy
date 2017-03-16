#
# Android page!
#
class Android:
    
    def __init__(self, name):
        self.name = name
        self.posX = 0
        self.posY = 0
        
    
    def walk(self, x, y, world):
        self.posX += x
        self.posY += y
        
        world.scan(self.posX, self.posY)