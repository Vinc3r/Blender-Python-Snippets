"""
  This allow to active or not a material output node with a custom label on all your selected objects.
"""

import bpy

switch_to_customLabel = True
output_label = "myCustomLabel"

C = bpy.context

if len(C.view_layer.objects.selected) > 0:
    for obj in C.view_layer.objects.selected:
        if len(obj.data.materials) > 0:
            for mat in obj.data.materials:
                for node in mat.node_tree.nodes:
                    if node.type != 'OUTPUT_MATERIAL':
                        continue
                    node.is_active_output = False
                    if switch_to_customLabel and node.label == output_label:
                        print("activating custom output")
                        node.is_active_output = True
                    elif not switch_to_customLabel and node.label != output_label:
                        print("activating default output")
                        node.is_active_output = True
