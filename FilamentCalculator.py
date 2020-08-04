import rhinoscriptsyntax as rs

import math


def FilamentCalculator():
    """3D Printing filament length, weight, volume calculator."""

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

    filaments = {"PLA" : 1.24,
                 "ABS" : 1.05,
                 "ASA" : 1.07,
                 "PETG" : 1.27,
                 "PETT" : 1.45,
                 "HIPS" : 1.07,
                 "TPU" : 1.30,
                 "PMMA" : 1.18,
                 "Nylon" : 1.08,
                 "Polycarbonate" : 1.20,
                 "Copperfill" : 3.90}

    filament = rs.GetString("Material:", "PLA", [a for a in filaments])

    density = filaments[filament]
    volume = volume / rs.UnitScale(rs.UnitSystem(), 3)**3
    weight = volume * filaments[filament]

    l1 = volume / (math.pi*(0.175/2)**2) / 100
    l2 = volume / (math.pi*(0.285/2)**2) / 100
    l3 = volume / (math.pi*(0.3/2)**2) / 100

    volume = round(volume, 3)
    weight = round(weight, 3)

    l1 = round(l1, 2)
    l2 = round(l2, 2)
    l3 = round(l3, 2)

    message = """{f}:
    Density = {d} grams / cubic centimeter
    Volume = {v} cubic centimeters
    Weight ~ {w} grams
    1.75 mm filament length ~ {l1} meters
    2.85 mm filament length ~ {l2} meters
    3.00 mm filament length ~ {l3} meters"""
    message = message.format(f=filament, d=density, v=volume, w=weight, l1=l1, l2=l2, l3=l3)
    rs.MessageBox(message, buttons=0, title="FilamentCalculator:")
    print(message)


if (__name__ == "__main__"):
    FilamentCalculator()
