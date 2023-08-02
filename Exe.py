#  python python Exe.py bdist_msi

import cx_Freeze
import sys
import os

import scipy

base = None
if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:/Users/divyesh.hadvani/AppData/Local/Programs/Python/Python310/tcl/tcl8.6"
os.environ['TK_LIBRARY'] = r"C:/Users/divyesh.hadvani/AppData/Local/Programs/Python/Python310/tcl/tk8.6"

executables = [cx_Freeze.Executable("Final_Code_AH.py", base=base,icon="UDTE_icon.ico")]

cx_Freeze.setup(
    name = "AH_Software",
    options = {"build_exe": {"packages":['scipy',"tkinter","os","sys"], "include_files":['tcl86t.dll','tk86t.dll','UDTE_icon.ico','MicrosoftTeams-image (1).png','MicrosoftTeams-image (2).png','Share_03.png','C:/Users/divyesh.hadvani/AppData/Local/Programs/Python/Python310/Lib/site-packages/scipy']}},
    version = "24.02",
    description = "AH_Software | Developed by Divyesh Hadvani ",
    executables = executables
    )
