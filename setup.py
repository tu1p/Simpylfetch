from cx_Freeze import setup

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": ["tkinter"],
    "zip_include_packages": ["PySide6", "shiboken6"],
}

setup(
    name="simpylfetch1",
    version="0.1",
    description="a basic python script to fetch system data",
    options={"build_exe": build_exe_options},
    executables=[{"script": "simpylfetch1.py", "base": "gui"}],
)