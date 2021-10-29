""" This apply the mirror modifier,
    and only this one, on selection
"""

import bpy

for obj in bpy.context.selected_objects:
    if len(obj.modifiers) > 0:
        modifiers = []
        for mod in obj.modifiers:
            if mod.type == 'MIRROR':
                modifiers.append(mod.name)
        for mod in modifiers:
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.modifier_apply(modifier=mod)
