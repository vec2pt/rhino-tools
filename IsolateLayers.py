import rhinoscriptsyntax as rs

import json


def IsolateLayers():
    file_name = rs.DocumentName()
    file_path = rs.DocumentPath()

    # Select objects
    input_obj = rs.SelectedObjects()
    if not input_obj:
	    input_obj = rs.GetObjects("Select objects on layers to isolate")
    if not input_obj:return

    # Get all layers names
    proj_layers = rs.LayerNames()
    layers_history = {rs.LayerId(l): rs.LayerVisible(l) for l in proj_layers}

    # Save temp
    if file_name is None:
        temp_file_name = "IsolateLayers_temp.json"
    else:
        temp_file_name = file_path + 'IsolateLayers_temp_' + file_name.strip('.3dm') + '.json'

    with open(temp_file_name, "w+") as f:
        f.write(json.dumps(layers_history, sort_keys=True, indent=4))

    # Get objects layers
    obj_layers = [rs.ObjectLayer(o) for o in input_obj]

    layers = []
    for l in obj_layers:
        s = l.split('::')
        a = 0
        while len(s) > a:
            layers.append("::".join(s[:a+1]))
            a += 1

    # Set current layer
    rs.CurrentLayer(layers[0])

    # Hide layers
    layers_to_hide = list(set(proj_layers) - set(layers))
    for l in layers_to_hide:
	    rs.LayerVisible(l,False)


if __name__ == '__main__':
    IsolateLayers()
