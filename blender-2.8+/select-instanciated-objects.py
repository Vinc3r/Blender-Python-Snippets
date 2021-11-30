import bpy

for obj in bpy.context.view_layer.objects:
    if obj.data.users > 1:
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
    else:
        obj.select_set(False)