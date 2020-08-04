import rhinoscriptsyntax as rs


def NewPart():
    """Create a 'New Part' layer as a sublayer of '30_3D'."""

    input_obj = rs.SelectedObjects()
    layers = rs.LayerNames()

    if "30_3D" not in layers:
        rs.AddLayer("30_3D")

    for i in range(1,30):
        new_layer = "30_3D::3{}_Part".format(i)
        if new_layer not in layers:
            rs.AddLayer("3{}_Part".format(i), parent="30_3D")
            if input_obj:
                rs.ObjectLayer(input_obj, new_layer)
            return


if (__name__ == "__main__"):
    NewPart()
