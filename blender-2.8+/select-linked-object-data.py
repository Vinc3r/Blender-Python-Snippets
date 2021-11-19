import bpy

objects_list = bpy.context.view_layer.objects

for obj in objects_list:
    print("----")
    obj.select_set(False)
    if obj.data.users > 0:
        print(f"REF {obj.name}")
        obj_instances = []
        mesh_id = obj.data.id_data
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        for obj_int in objects_list:
            if obj_int.data.users > 0 and \
                obj_int != obj and \
                obj_int.data.id_data is mesh_id:
                    print(f"INST {obj_int.name}")
                    objects_list.remove(obj_int)
                    obj_int.select_set(True)

"""
manual operation:
- select a mesh
- select linked object data
- make single user
"""