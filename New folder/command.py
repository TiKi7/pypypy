#
# Command line page!
#
import os
def command(android, world):
    while True:
        cmd = input('(%s,%s)cmd@ '%(android.posX,android.posY))
        os.system('cls') # just use in shel mode!
        if cmd == 'quit':
            break
        
        elif cmd == 'w':
            android.walk( 0,-1, world )   
        
        elif cmd == 's':
            android.walk( 0, 1, world )
        
        elif cmd == 'a':
            android.walk(-1, 0, world )
        
        elif cmd == 'd':
            android.walk( 1, 0, world )
        
        elif cmd == '':
            android.walk( 0, 0, world )        
            
        elif cmd == 'cache':
            print('\n'*4 + 
                  'cache@ ' + str(len(world._pts.memo)) +
                  ' points' + '\n'*4)       