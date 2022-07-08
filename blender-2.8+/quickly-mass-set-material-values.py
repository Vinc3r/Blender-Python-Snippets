import bpy

for mat in bpy.data.materials:
    if mat.use_nodes:
        mat.node_tree.nodes["Principled BSDF"].inputs[6].default_value = 0 # metallic
        mat.node_tree.nodes["Principled BSDF"].inputs[9].default_value = 1 # roughness
