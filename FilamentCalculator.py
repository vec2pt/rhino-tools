import rhinoscriptsyntax as rs

import math


def units(i):
    """0	No unit system
    1	Microns (1.0e-6 meters)
    2	Millimeters (1.0e-3 meters)
    3	Centimeters (1.0e-2 meters)
    4	Meters
    5	Kilometers (1.0e+3 meters)
    6	Microinches (2.54e-8 meters, 1.0e-6 inches)
    7	Mils (2.54e-5 meters, 0.001 inches)
    8	Inches (0.0254 meters)
    9	Feet (0.3408 meters, 12 inches)
    10	Miles (1609.344 meters, 5280 feet)
    11	* Reserved for Custom Unit System *
    12	Angstroms (1.0e-10 meters)
    13	Nanometers (1.0e-9 meters)
    14	Decimeters (1.0e-1 meters)
    15	Dekameters (1.0e+1 meters)
    16	Hectometers (1.0e+2 meters)
    17	Megameters (1.0e+6 meters)
    18	Gigameters (1.0e+9 meters)
    19	Yards (0.9144  meters, 36 inches)
    20	Printer point (1/72 inches, computer points)
    21	Printer pica (1/6 inches, (computer picas)
    22	Nautical mile (1852 meters)
    23	Astronomical (1.4959787e+11)
    24	Lightyears (9.46073e+15 meters)
    25	Parsecs (3.08567758e+16)
    """
    rhino_units =  {1 : 1.0e-6,
                    2 : 1.0e-3,
            		3 : 1.0e-2,
            		4 : 1.0,
            		5 : 1.0e+3,
            	    6 : 2.54e-8,
            		7 : 2.54e-5,
            		8 : 0.0254,
            		9 : 0.3408,
            		10 : 1609.344}
    return rhino_units[i]



def FilamentCalculator():
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
    volume = volume * ((units(rs.UnitSystem()))**3) * 100**3
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
    print message.format(f=filament, d=density, v=volume, w=weight, l1=l1, l2=l2, l3=l3)


if (__name__ == "__main__"):
    FilamentCalculator()
