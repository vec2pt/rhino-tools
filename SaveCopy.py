import rhinoscriptsyntax as rs

from os import popen
from datetime import datetime
from shutil import copyfile


def SaveCopy():
    date_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    while rs.DocumentPath() is None:
        rs.Command("'_Save")

    file_name = rs.DocumentName()
    file_dir = rs.DocumentPath()
    file_path = file_dir + file_name

    copy_name = "_".join([date_time, file_name])
    copy_path = rs.DocumentPath() + copy_name

    try:
        os.mkdir(copy_dir)
        rs.Command("'-Save " + file_path)
        copyfile (file_path, copy_path)
    except:
        rs.Command("'-Save " + file_path)
        copyfile (file_path, copy_path)



if __name__ == "__main__":
    SaveCopy()
