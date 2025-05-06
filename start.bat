@echo off
REM Ярлык свойства: cmd /c "c:\Program Files\keyboard\start.bat"
REM Ярлык рабочая папка: "c:\Program Files\keyboard"start.bat
REM Ярлык дополнительно: Запуск от имени администратора
cd /d "%~dp0"
".venv\Scripts\pythonw.exe" get_layout.py
REM Текущая раскладка клавиатуры
set "layout_currence=%errorlevel%"         
REM Устанавливаем раскладку клавиатуры EN_US
".venv\Scripts\pythonw.exe" set_layout.py 0x409 
".venv\Scripts\pythonw.exe" main.py  %layout_currence% 

