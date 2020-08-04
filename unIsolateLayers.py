import rhinoscriptsyntax as rs

import os
import json


def unIsolateLayers():
    """Unisolate layers by unhiding layers."""

    file_name = rs.DocumentName()
    file_path = rs.DocumentPath()
    if file_name is None:
        temp_file_name = "IsolateLayers_temp.json"
    else:
        temp_file_name = file_path + 'IsolateLayers_temp_' + file_name.strip('.3dm') + '.json'

    if not os.path.isfile(temp_file_name):
        print("Temp File does not exist!")
        return

    with open(temp_file_name, "r") as f:
        layers_data = json.load(f)

    new_layers_data = {}

    for i in layers_data:
        new_layers_data[rs.LayerName(i)] = layers_data[i]
    sorted_layers_data = sorted(new_layers_data.iteritems())

    for layer_name, layer_visibility in sorted_layers_data:
        rs.LayerVisible(layer_name, layer_visibility)

    # remove TEMP FILE
    os.remove(temp_file_name)


if __name__ == '__main__':
    unIsolateLayers()
