import sys
import logging

import functions as f


def parse_number(s: str) -> int:
    s = s.strip().lower()
    base = 16 if s.startswith("0x") else 10
    try:
        return int(s, base)
    except ValueError:
        logging.info(
            f"Неверный формат параметра {s}\n Требуется десятичное или 16 число"
        )
        sys.exit(1)


if __name__ == "__main__":
    f.init_logging()
    if len(sys.argv) != 2:
        logging.info(
            f"set_layout.py. Задано неверное число параметров - {len(sys.argv) - 1}\nПрограмма принимает 1 параметр."
        )
        sys.exit(1)

    layout = parse_number(sys.argv[1])

    f.set_layout(layout)
    sys.exit(1)
