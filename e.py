LAYOUT_EN_US = 0x0409
LAYOUT_RU_RU = 0x0419

import ctypes


def set_EN_layout():
    """Устанавливаем раскладку по layout_id"""
    # 0x409 - код английской раскладки (EN-US)
    ctypes.windll.user32.PostMessageW(0xFFFF, 0x50, 0, 0x409)


set_EN_layout()
