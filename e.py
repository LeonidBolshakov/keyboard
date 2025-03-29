import keyboard
import win32clipboard
import win32con
import time


def get_clipboard_text():
    win32clipboard.OpenClipboard()
    try:
        text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
    except:
        text = ""
    finally:
        win32clipboard.CloseClipboard()
    return text


def copy_selected_text():
    # Очищаем буфер обмена
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()

    # Эмулируем нажатие Ctrl+C с помощью keyboard
    keyboard.press_and_release("ctrl+c")

    # Задержка для обработки
    time.sleep(0.5)

    return get_clipboard_text()


# Функция, которая будет вызываться по горячей клавише
def on_hotkey():
    text = copy_selected_text()
    print(text)
    # processed_text = text.upper()  # пример обработки
    # paste_text(processed_text)


# Регистрируем горячую клавишу (например, Ctrl+Shift+X)
keyboard.add_hotkey("ctrl+shift+x", on_hotkey)
keyboard.wait()  # Ждем нажатия клавиш
