"""
    Cycle through selected object and select all instances
"""

import bpy

for obj in bpy.context.selected_objects:
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.select_linked(extend=True, type='OBDATA')
