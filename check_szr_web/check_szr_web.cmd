@echo off
echo. >display_warning.vbs
call ..\..\naucse-python\venv\Scripts\activate
python check_szr_web.py
wscript display_warning.vbs
