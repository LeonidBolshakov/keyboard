# from PyQt6.QtWidgets import QTextBrowser, QApplication
# from PyQt6.QtCore import Qt
#
#
# class MyTextBrowser(QTextBrowser):
#     def insertFromMimeData(self, source):
#         print("Вставка (paste/drop) обнаружена!")
#         super().insertFromMimeData(source)
#
#     def copy(self):
#         print("Копирование (Ctrl+C) обнаружено!")
#         super().copy()
#
#
# app = QApplication([])
# browser = MyTextBrowser()
# browser.setReadOnly(False)
# browser.setPlainText("Попробуйте скопировать или вставить текст")
# browser.show()
# app.exec()
#
#
from PyQt6.QtWidgets import QTextEdit, QApplication
from PyQt6.QtCore import pyqtSignal


class MyTextEdit(QTextEdit):
    pasted = pyqtSignal()

    def insertFromMimeData(self, source):
        self.pasted.emit()
        super().insertFromMimeData(source)


app = QApplication([])
text_edit = MyTextEdit()
text_edit.pasted.connect(lambda: print("Произошла вставка!"))
text_edit.show()
app.exec()
