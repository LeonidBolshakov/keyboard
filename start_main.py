import subprocess
import sys
from pathlib import Path

import psutil
from PyQt6.QtWidgets import QApplication

from const import Const as C
import functions as f


def is_running():
    if not Path(C.PID_FILE_PATH).exists():
        return False

    try:
        pid, name = Path(C.PID_FILE_PATH).read_text().split(":", 1)
        p = psutil.Process(int(pid))
        return True if p.is_running() and p.cmdline()[1] == name else False
    except (psutil.NoSuchProcess, ValueError, PermissionError):
        return False


def show_message_restart():
    # noinspection PyUnusedLocal
    app = QApplication([])

    # Создаем и настраиваем MessageBox
    f.show_message(
        f"{C.TEXT_MESSAGE_RESTART_PROGRAM}",
        C.TIME_MESSAGE_RESTART_PROGRAM,
        C.COLOR_MESSAGE_RESTART_PROGRAM,
    )


if __name__ == "__main__":
    if is_running():
        show_message_restart()
    else:
        original_layout_id = f.get_current_layout_id()
        f.set_layout_id(C.LAYOUT_EN_US)  # Установка раскладки UN-US
        # Запускаем фоновый GUI-процесс
        process = subprocess.Popen(
            [
                sys.executable,
                f"{C.MODUL_NAME}",
                str(original_layout_id),
            ],
            close_fds=True,  # Закрываем все файловые дескрипторы
            creationflags=subprocess.CREATE_NO_WINDOW
            | subprocess.CREATE_NEW_PROCESS_GROUP,
            # Позволяет дочернему процессу жить после завершения родителя
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
        )
        Path(C.PID_FILE_PATH).write_text(f"{process.pid}:{process.args[1]}")
        while True:
            line = process.stdout.readline().strip()
            if line == C.CHECK_COMPLETED:
                break
        f.set_layout_id(original_layout_id)  # Возвращаем первоначальную раскладку
