import sys

import functions as f

if __name__ == "__main__":
    layout = f.get_keyboard_layout_from_param()
    if layout:
        f.set_layout(layout)
    else:
        sys.exit(1)
