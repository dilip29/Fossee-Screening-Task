import sys
from cx_Freeze import setup,Executable

build_exe_options = {"packages":["PyQt5","xlrd"],
                     "include_files":["steel_sections.sqlite","new_sections.xlsx"]}

base=None

if sys.platform == "win32":
    base="Win32GUI"
    pass

setup(name = "My Application",
        version="0.1",
      description="my gui application",
      options={"build_exe":build_exe_options},
      executables= [Executable("steel.py",base=base)])
