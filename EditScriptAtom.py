import rhinoscriptsyntax as rs

from os import popen


def EditScriptAtom():
    file_name = rs.OpenFileName("Open")

    if file_name is None:
        None
    else:
        atom_app = r"/Applications/Atom.app/Contents/MacOS/Atom"
        popen("{} {}".format(atom_app, file_name))

        rs.Command("_StartAtomEditorListener")


if __name__ == "__main__":
    EditScriptAtom()
