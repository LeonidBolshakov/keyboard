import subprocess
import sys

import psutil
from PyQt6.QtWidgets import QApplication

from const import Const as C
import functions as f


def is_running(script_name="main_8A63F9A8-A206-4B0A-B517-F28E3471154E.py"):
    for proc in psutil.process_iter(["cmdline"]):
        try:
            # Проверка, есть ли cmdline и содержит ли она нужное имя
            if proc.info["cmdline"] and script_name in proc.info["cmdline"]:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Если с процессом что-то не так (не существует, отказано в доступе), пропускаем его
            continue
    return False


def show_message():
    app = QApplication(sys.argv)

    # Создаем и настраиваем MessageBox
    f.show_message(
        f"{C.TEXT_MESSAGE_RESTART_PROGRAM}",
        C.TIME_MESSAGE_RESTART_PROGRAM,
        C.COLOR_MESSAGE_RESTART_PROGRAM,
    )


if __name__ == "__main__":
    if is_running():
        show_message()
        exit(1)
    else:
        # Запускаем фоновый GUI-процесс
        subprocess.Popen(
            [sys.executable, "main_8A63F9A8-A206-4B0A-B517-F28E3471154E.py"]
        )
        exit(0)
