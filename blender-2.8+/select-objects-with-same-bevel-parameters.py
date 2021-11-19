""" Compare Bevel width and limit values
"""

import bpy

active_obj = bpy.context.view_layer.objects.active
bevel_modifiers = []
if len(active_obj.modifiers) > 0:
    for mod in active_obj.modifiers:
        if mod.type == 'BEVEL':
            bevel_modifiers.append(mod)

if len(bevel_modifiers) > 0:
    for obj in bpy.context.view_layer.objects:
        obj.select_set(False)
        if len(obj.modifiers) > 0:
            for mod in obj.modifiers:
                if mod.type == 'BEVEL':
                    for active_mod in bevel_modifiers:
                        if mod.width == active_mod.width and \
                                mod.limit_method == active_mod.limit_method:
                            obj.select_set(True)
