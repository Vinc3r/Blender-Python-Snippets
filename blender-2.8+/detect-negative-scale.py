""" This select objects with a negative scale
"""

import bpy

for obj in bpy.context.view_layer.objects:
    obj.select_set(False)
    for s in obj.scale:
        if s < 0:
            obj.select_set(True)
            
bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]