@echo off
cls
color 4
python -V
pip -V
timeout 2
color 1
pip install python-dev
pip install -U pip
python -m pip install tk
pip install tkintertable
pip install tkintertoy
pip install wmi
pip install pywin32
pip install psutil
pip install screeninfo
pip install GPUtil
pip install tabulate
pip install DateTime
color 2
timeout 5