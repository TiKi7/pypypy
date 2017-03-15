#
# it's all about Android!
#

class Enemy:
    lib = {
        '1' : 10,
        '2' : 20,
        '3' : 30
        }


class Android:
    ''' 
    the main class to init an android
    '''
    enemies = Enemy()
    
    def __init__(self, name):
        #
        # every thing will be in string
        #
        self.name = name
        
        self.position = {'x':0, 'y':0}
        
        self.stats = dict(
            LIVES = 2,
            STR = 5,
            EXP = 0
            )
        self.maxHP = self.stats['EXP'] //100 * 25 + 100
        
        
    def __repr__(self):
        return str(self.name.upper()) + ' @ ' + str(self.stats)

    
    
    def kill(self, address, world):
        u_s = world.memo[ address ]
        
        if u_s != 0:                                           #if there is any enemy there...
            enemy = self.enemies.lib[str(u_s)]
            HP = self.maxHP
            EXP = self.stats['EXP']
            LVL = EXP // 100
            STR = self.stats['STR']
            LIVES = self.stats['LIVES']
            
            while enemy > 0 and HP > 0:                        # while both of us are still alive
                
                atk = (LVL+1)*STR
                dmg = enemy
                enemy -= atk
                HP -= dmg
                
                if HP <= 0:                                    # if i die i will use one of my lives
                    if LIVES > 0:
                        LIVES = LIVES - 1
                        self.stats['LIVES'] = LIVES            #update db
                        HP = HP + 100
                    else: print('you died')
                self.stats['HP'] = HP                          #update db
                
                if enemy <= 0:                                 #if he die the address will be '0' and i will gain '10' EXP!
                    world.memo[ address ] = 0                  #update db
                    self.stats['EXP'] += 10                    #update db
                    
        print(self.stats)     
        #----- thats it -----#
    
    def walk(self, world, direction):
        
        if direction == 'U':
            direction = (0,1)
        elif direction == 'D':
            direction = (0,-1)
        elif direction == 'L':
            direction = (-1,0)
        elif direction == 'R':
            direction = (1,0)
        else: direction = (0,0)
                
        _x = self.position['x'] + direction[0]
        _y = self.position['y'] + direction[1]
        address = str(_x) + ',' + str(_y)
        
        self.kill(address, world)                              #first you have to kill an enemy
        
        self.position['x'] = _x                                # then you can occupy its place
        self.position['y'] = _y