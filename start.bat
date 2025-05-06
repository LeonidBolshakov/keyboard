@echo off
REM Ярлык свойства: cmd /c "c:\Program Files\keyboard\start.bat"
REM Ярлык рабочая папка: "c:\Program Files\keyboard"start.bat
REM Ярлык дополнительно: Запуск от имени администратора
cd /d "%~dp0"
".venv\Scripts\pythonw.exe" set_EN_US_layout.py
".venv\Scripts\pythonw.exe" main.py