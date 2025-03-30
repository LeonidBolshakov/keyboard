from time import sleep
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from pyautogui import hotkey


class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()

        # Инициализация интерфейса
        self.initUI()

    def initUI(self):
        # Создаем кнопку и метку
        self.button = QPushButton("Нажми меня", self)
        self.label = QLabel("Привет, мир!", self)

        # Подключаем сигнал нажатия кнопки к слоту изменения текста
        self.button.clicked.connect(self.onButtonClick)

        # Создаем вертикальный лейаут и добавляем в него виджеты
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Устанавливаем лейаут для главного окна
        self.setLayout(layout)

        # Настраиваем окно
        self.setWindowTitle("Простое приложение")
        self.setGeometry(100, 100, 300, 200)

    def onButtonClick(self):
        # Изменяем текст метки при нажатии на кнопку

        QApplication.clipboard().setText("aaa")
        hotkey("ctrl", "v")
        sleep(1)
        QApplication.clipboard().setText("bbb")
        self.label.setText("Кнопка нажата!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleApp()
    window.show()
    sys.exit(app.exec())
