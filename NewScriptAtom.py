import rhinoscriptsyntax as rs

from os import popen


def NewScriptAtom():
    file_name = rs.SaveFileName ("Save", "Text Files (*.py)|*.py|All Files (*.*)|*.*||")
    if not file_name:return

    py_template  = """# Built-in

# Other Libs
# Rhinoceros
import rhinoscriptsyntax as rs
# import scriptcontext as sc
# import Rhino as RH

# Grasshopper
# import Grasshopper as GH
# import ghpythonlib.components as ghcomp
# import ghpythonlib.treehelpers as th

def new_script():
    pass

if (__name__ == "__main__"):
    new_script()"""

    with open(file_name, "w+") as f:
        print f.writelines(py_template)

    atom_app = r"/Applications/Atom.app/Contents/MacOS/Atom"
    popen("{} {}".format(atom_app, file_name))

    rs.Command("_StartAtomEditorListener")


if __name__ == "__main__":
    NewScriptAtom()
