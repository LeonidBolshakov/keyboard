@echo off
REM ����� ��������: cmd /c "c:\Program Files\keyboard\start.bat"
REM ����� ������� �����: "c:\Program Files\keyboard"start.bat
REM ����� �������������: ������ �� ����� ��������������
cd /d "%~dp0"
".venv\Scripts\pythonw.exe" get_layout.py
REM ������� ��������� ����������
set "layout_currence=%errorlevel%"         
REM ������������� ��������� ���������� EN_US
".venv\Scripts\pythonw.exe" set_layout.py 0x409 
".venv\Scripts\pythonw.exe" main.py  %layout_currence% 

