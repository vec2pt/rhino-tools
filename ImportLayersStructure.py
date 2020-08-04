import rhinoscriptsyntax as rs

import json


def hex_to_rbg(colore):
    """RGB to Hex color conversion."""

    colore = colore.lstrip('#')
    rgb = tuple(int(colore[i:i+2], 16) for i in (0, 2, 4))
    return rgb


def set_layer_properties(layer, properties):
    """Set Rhino layer properties."""

    rs.LayerVisible(layer, properties.get("LayerVisible"))
    rs.LayerLocked(layer, properties.get("LayerLocked"))
    rs.LayerColor(layer, hex_to_rbg(properties.get("LayerColor")))
    rs.LayerMaterialIndex(layer, properties.get("LayerMaterialIndex"))
    rs.LayerLinetype(layer, properties.get("LayerLinetype"))
    rs.LayerPrintColor(layer, hex_to_rbg(properties.get("LayerPrintColor")))
    rs.LayerPrintWidth(layer, properties.get("LayerPrintWidth"))


def ImportLayersStructure():
    """Import layers structure from json file."""

    file_name = rs.OpenFileName("Open", "Text Files (*.json)|*.json|All Files (*.*)|*.*||")
    if not file_name:return

    with open(file_name, "r") as f:
        layers_properties = json.load(f)
    actual_layers_properties = [rs.LayerName(l) for l in rs.LayerNames()]

    for l, i in zip(layers_properties.keys(), layers_properties.values()):
        override = True
        if l in actual_layers_properties:
            override = rs.MessageBox(l, buttons=1, title="Override existing properties:")
            if override == 2:
                override = False
        else:
            rs.AddLayer(l)
        if override:
            set_layer_properties(l, i)


if __name__ == "__main__":
    ImportLayersStructure()
