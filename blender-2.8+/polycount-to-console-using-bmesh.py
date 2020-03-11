import bpy
import bmesh
print("+++++++++++++++++")
"""
    thanks to glTF developpers for piece of code about normals,
    allowing realistic vertex count
    https://github.com/KhronosGroup/glTF-Blender-IO/blob/master/addons/io_scene_gltf2/blender/exp/gltf2_blender_gather_nodes.py#L268

    ---

    objects have to be shaded as smooth
"""
for blender_object in [o for o in bpy.context.view_layer.objects if o.type == 'MESH']:

    modifier_normal_types = [
        "NORMAL_EDIT",
        "WEIGHTED_NORMAL",
        "BEVEL"
    ]
    auto_smooth = blender_object.data.use_auto_smooth
    edge_split = None
    # checking if already normals modifier
    some_normals_modifier = any([m in modifier_normal_types for m in [
                                mod.type for mod in blender_object.modifiers]])

    # if only autosmooth, we can add a temp edgesplit modifier
    if auto_smooth and not some_normals_modifier:
        edge_split = blender_object.modifiers.new(
            'Temporary_Auto_Smooth', 'EDGE_SPLIT')
        edge_split.split_angle = blender_object.data.auto_smooth_angle
        edge_split.use_edge_angle = not blender_object.data.has_custom_normals
        blender_object.data.use_auto_smooth = False
        bpy.context.view_layer.update()

    # updating all this stuff that's I'm not sure what it is
    depsgraph = bpy.context.evaluated_depsgraph_get()
    blender_mesh_owner = blender_object.evaluated_get(depsgraph)
    blender_mesh = blender_mesh_owner.to_mesh(
        preserve_all_data_layers=True, depsgraph=depsgraph)

    # bmesh for calculation
    bm = bmesh.new()
    bm.from_mesh(blender_mesh)
    bm.faces.ensure_lookup_table()
    has_ngon = False
    area = 0

    for face in bm.faces:
        area += face.calc_area()
        if len(face.edges) > 4:
            has_ngon = True
    verts = len(bm.verts)
    tri = len(bm.calc_loop_triangles())
    faces = len(bm.faces)
    area = round(area, 1)
    polycount = [verts, tri, faces, has_ngon, area]

    # removing temp edge split modifier
    if auto_smooth and not some_normals_modifier:
        blender_object.data.use_auto_smooth = True
        blender_object.modifiers.remove(edge_split)

    bm.free()

    print(blender_object.name)
    print("  verts: {}".format(polycount[0]))
    print("  tri: {}".format(polycount[1]))
    print("  faces: {}".format(polycount[2]))
    print("  ngon: {}".format(polycount[3]))
    print("  area: {}".format(polycount[4]))
