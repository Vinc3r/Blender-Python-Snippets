""" This remove all subdivision modifiers,
    without applying them
"""

import bpy

for obj in bpy.context.selected_objects:
    if len(obj.modifiers) > 0:
        for mod in obj.modifiers:
            if mod.type == 'SUBSURF':
                bpy.ops.object.modifier_remove(modifier=mod.name)
