""" This select objects having a mirror modifier
"""

import bpy

for obj in bpy.context.view_layer.objects:
    obj.select_set(False)
    if len(obj.modifiers) > 0:
        for mod in obj.modifiers:
            if mod.type == 'MIRROR':
                obj.select_set(True)
                bpy.context.view_layer.objects.active = obj
