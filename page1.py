#
# it's all about Android!
#


class Android:
    ''' 
    the main class to init an android
    '''
    
    def __init__(self, name):
        #
        # every thing will be in string
        #
        self.name = name
        
        self.position = {'x':0, 'y':0}
        
        self.stats = dict(
            LIVES=0,
            HP=0,
            STR=0,
            )
    
    def __repr__(self):
        return str(self.name.upper()) + ' @ ' + str(self.stats)
    
    @classmethod
    def factory(cls, android, *names):
        #
        # you can call androids by --> android['name']
        #
        # cls --> this is our Android class
        # android --> an Explicit dictionary
        # names --> this will make a tuple of names
        
        for i in range(len(names)):
            a = cls(names[i])
            android[a.name] = a
    
    def update(self, direction, world):
        
        if direction == 'U':
            direction = (0,1)
        elif direction == 'D':
            direction = (0,-1)
        elif direction == 'L':
            direction = (-1,0)
        elif direction == 'R':
            direction = (1,0)       
                
        self.position['x'] += direction[0]
        self.position['y'] += direction[1]
        
        world.update(self)
        