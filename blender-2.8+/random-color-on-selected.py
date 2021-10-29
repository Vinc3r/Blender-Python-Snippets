""" This assign a random object color on selection
"""

import bpy
import random


def returnRandColor():
    return random.randrange(0, 1000000) / 1000000


for obj in bpy.context.selected_objects:
    obj.color = (returnRandColor(), returnRandColor(), returnRandColor(), 1)
