""" This select objects having a specific width value
"""

import bpy

bevel_width = 0.01
value_margin = 0.001

for obj in bpy.context.view_layer.objects:
    obj.select_set(False)
    if len(obj.modifiers) > 0:
        for mod in obj.modifiers:
            if mod.type == 'BEVEL' and \
                    mod.width <= (bevel_width + value_margin) and \
                    mod.width >= (bevel_width - value_margin):
                obj.select_set(True)
                bpy.context.view_layer.objects.active = obj
