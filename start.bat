@echo off
REM ��� ᢮��⢠: cmd /c "c:\Program Files\keyboard\start.bat"
REM ��� ࠡ��� �����: "c:\Program Files\keyboard"start.bat
REM ��� �������⥫쭮: ����� �� ����� �����������
cd /d "%~dp0"
".venv\Scripts\pythonw.exe" get_layout.py
REM ������ �᪫���� ����������
set "layout_currence=%errorlevel%"         
REM ��⠭�������� �᪫���� ���������� EN_US
".venv\Scripts\pythonw.exe" set_layout.py 0x409 
if not %errorlevel% equ 0 echo "�訡�� � ��ࠬ���� set_layout. ��. LOG"
REM ����㦠�� �ணࠬ�� ������ ॣ���஢ ����񭭮�� ⥪��
".venv\Scripts\pythonw.exe" main.py  %layout_currence% 
if not %errorlevel% equ 0 ".venv\Scripts\pythonw.exe" set_layout.py  %layout_currence% 