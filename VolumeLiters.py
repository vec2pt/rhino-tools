import rhinoscriptsyntax as rs


def VolumeLiters():
    """Report the volume in Litres of closed surfaces, polysurfaces, or meshes."""
    input_obj = rs.SelectedObjects()
    if not input_obj:
        input_obj = rs.GetObjects("Select objects")
        if not input_obj:return

    volume = 0.0
    for o in input_obj:
        if rs.IsMesh(o):
            a, b, c = rs.MeshVolume(o)
            volume += b
        elif rs.IsObjectSolid(o):
            a, b = rs.SurfaceVolume(o)
            volume += a
    if volume == 0.0: return

    volume = round(volume / (rs.UnitScale(rs.UnitSystem(), 3)*10)**3, 3)
    print "Volume = {} liters".format(volume)


if( __name__ == "__main__" ):
    VolumeLiters()
