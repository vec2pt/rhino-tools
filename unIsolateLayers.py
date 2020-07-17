import rhinoscriptsyntax as rs

import os
import json


def unIsolateLayers():
    try:
        file_name = rs.DocumentName()
        file_path = rs.DocumentPath()
        if file_name is None:
            temp_file_name = "IsolateLayers_temp.json"
        else:
            temp_file_name = file_path + 'IsolateLayers_temp_' + file_name.strip('.3dm') + '.json'

        with open(temp_file_name, "r") as f:
            layers_data = json.load(f)

        for i in layers_data:
            rs.LayerVisible(rs.LayerName(i), layers_data[i])

        # remove TEMP FILE
        os.remove(temp_file_name)

    except:
        print "No Temp File"
        rs.Command("!_-Layer On * Enter")


if __name__ == '__main__':
    unIsolateLayers()
