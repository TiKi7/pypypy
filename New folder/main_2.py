#
# main page!
#
from android import Android
from world import World
from command import *


world = World()
me = Android('2B')

command(me, world)