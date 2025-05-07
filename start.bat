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
if not %errorlevel% equ 0 echo "Ошибка в параметрах set_layout. См. LOG"
REM Загружаем программу замены регистров введённого текста
".venv\Scripts\pythonw.exe" main.py  %layout_currence% 
if not %errorlevel% equ 0 ".venv\Scripts\pythonw.exe" set_layout.py  %layout_currence% 