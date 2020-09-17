# rhino_tools

A series of simple scripts for [Rhinoceros 3D](https://www.rhino3d.com).


## Installation


1. Drop script files to the directory:

    for macOS:
    ```
    /Users/HOME/Library/Application Support/McNeel/Rhinoceros/6.0/Scripts
    ```
    for Windows:

    ```
    C:\Users\UserName\AppData\Roaming\McNeel\Rhinoceros\6.0\scripts
    ```

2. Run script via command:
```
! _-RunPythonScript ScriptName

```
## Usage

- **EditScriptAtom.py** - Edit a Python script in Atom.app. (macOS)
- **ExportLayersStructure.py** - Save layers settings to a json file.
- **FilamentCalculator.py** - 3D Printing filament length, weight, volume calculator.
- **ImportLayersStructure.py** - Import layers settings into the current document from a json file.
- **IsolateLayers.py** - Isolate layers by hiding layers.
- **NewPart.py** - Create a 'New Part' layer as a sublayer of '30_3D'. (Personal Rhino standards)
- **NewScriptAtom.py** - Create a new Python script in Atom.app for Rhino. (macOS)
- **SaveCopy.py** - Save a copy of the current Rhino file.
- **unisolateLayers.py** - Unisolate layers by unhiding layers.
- **VolumeLiters.py** - Report the volume in Litres of closed surfaces, polysurfaces, or meshes.

## License

Distributed under the MIT License.

## Contact

Project Link: (https://github.com/M-VVV/rhino-tools)[https://github.com/M-VVV/rhino-tools]
