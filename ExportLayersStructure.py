import rhinoscriptsyntax as rs

import json


def rgb_to_hex(colore):
    r = rs.ColorRedValue(colore)
    g = rs.ColorGreenValue(colore)
    b = rs.ColorBlueValue(colore)
    return '#%02x%02x%02x' % (r, g ,b)

def get_layer_properties(layer):
    return {
        "LayerVisible" : rs.LayerVisible(layer),
        "LayerLocked" : rs.LayerLocked(layer),
        "LayerColor" : rgb_to_hex(rs.LayerColor(layer)),
        "LayerMaterialIndex" : rs.LayerMaterialIndex(layer),
        "LayerLinetype" : rs.LayerLinetype(layer),
        "LayerPrintColor": rgb_to_hex(rs.LayerPrintColor(layer)),
        "LayerPrintWidth" : rs.LayerPrintWidth(layer)
    }


def ExportLayersStructure():
    file_name = rs.SaveFileName ("Save", "Text Files (*.json)|*.json|All Files (*.*)|*.*||")
    if not file_name:return

    layers_properties = {rs.LayerName(l) : get_layer_properties(l) for l in rs.LayerNames()}

    with open(file_name, "w+") as f:
        f.write(json.dumps(layers_properties, sort_keys=True, indent=4))


if __name__ == "__main__":
    ExportLayersStructure()
