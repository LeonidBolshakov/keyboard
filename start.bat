@echo off
REM ����� ��������: cmd /c "c:\Program Files\keyboard\start.bat"
REM ����� ������� �����: "c:\Program Files\keyboard"start.bat
REM ����� �������������: ������ �� ����� ��������������
cd /d "%~dp0"
".venv\Scripts\pythonw.exe" set_EN_US_layout.py
".venv\Scripts\pythonw.exe" main.py