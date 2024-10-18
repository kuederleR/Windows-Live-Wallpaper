@echo off
REM Change to the directory containing the virtual environment
REM Get the absolute path of the current batch file
for %%I in ("%~dp0.") do set "BATCH_DIR=%%~fI"

REM Get the directory from the batch file path
for %%I in ("%BATCH_DIR%") do set "DIR=%%~dpI"

REM Append .venv to the directory
set "VENV_DIR=%DIR%\windows-live-wallpaper\.venv"

REM Change to the directory containing the virtual environment
cd /d %VENV_DIR%

REM Activate the virtual environment
call Scripts\activate.bat

REM Change to the directory containing the Python script
REM Set the pyhton dicrectory
set "PYTHON_DIR=%DIR%\windows-live-wallpaper"
cd /d %PYTHON_DIR%

REM Run the Python script
python opencv_wallpaper.py
