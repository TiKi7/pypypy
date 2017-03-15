#
# NieR Automata inspireed - 2B - main page
#

from page1 import *
from page3 import *

world = World()
android = Android('2b')
world.update(android)

def update(direction = (0,0)):
    android.walk(world, direction)
    world.update(android)


while True:
    update(input("I'm going... "))