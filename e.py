import psutil


def is_running(script_name="background_app.py"):
    for proc in psutil.process_iter(["cmdline"]):
        try:
            # Проверка, есть ли cmdline и содержит ли она нужное имя
            if proc.info["cmdline"] and script_name in proc.info["cmdline"]:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Если с процессом что-то не так (не существует, отказано в доступе), пропускаем его
            continue
    return False


import sys
from PyQt6.QtWidgets import QApplication, QMessageBox


def show_message():
    app = QApplication(sys.argv)

    # Создаем и настраиваем MessageBox
    msg = QMessageBox()
    msg.setWindowTitle("Сообщение")
    msg.setText("Это простое сообщение!")
    msg.setIcon(QMessageBox.Icon.Information)

    # Показываем сообщение
    msg.exec()

    # Завершаем приложение после закрытия MessageBox
    sys.exit(0)


if __name__ == "__main__":
    show_message()
