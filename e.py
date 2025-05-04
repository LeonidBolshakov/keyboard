import keyboard
import sys
import time
import json
from threading import Thread, Event


class KeyboardEmulator:
    def __init__(self):
        self.events = []
        self.should_exit = Event()
        self.emulating = False
        self.raw_events = []

        # Первый хук для записи всех событий
        keyboard.hook(self._hook_callback)

        # Второй поток для мониторинга raw-событий
        self.monitor_thread = Thread(target=self._monitor_events)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

    def _hook_callback(self, event):
        """Основной обработчик событий"""
        timestamp = time.strftime("%H:%M:%S")
        event_data = {
            "time": timestamp,
            "type": event.event_type,
            "key": event.name,
            "scan_code": event.scan_code,
            "is_keypad": event.is_keypad,
            "source": "real" if not self.emulating else "emulated",
        }
        self.events.append(event_data)

        sys.stderr.write(json.dumps(event_data) + "\n")
        sys.stderr.flush()

        if event.name == "esc" and event.event_type == "down":
            self.should_exit.set()

    def _monitor_events(self):
        """Дополнительный мониторинг событий через низкоуровневый polling"""
        while not self.should_exit.is_set():
            for name in ["b"]:  # Мониторим только интересующие нас клавиши
                if keyboard.is_pressed(name):
                    event_data = {
                        "time": time.strftime("%H:%M:%S"),
                        "key": name,
                        "state": "pressed",
                        "source": "polling",
                    }
                    self.raw_events.append(event_data)
                    sys.stderr.write(f"[RAW] {json.dumps(event_data)}\n")
                    sys.stderr.flush()
            time.sleep(0.01)

    def emulate_b(self):
        """Метод эмуляции с гарантированным контролем"""
        self.emulating = True
        methods = [
            lambda: keyboard.send("b"),
            lambda: (keyboard.press("b"), time.sleep(0.1), keyboard.release("b")),
            lambda: keyboard.write("b", delay=0.1),
        ]

        for i, method in enumerate(methods, 1):
            if self.should_exit.is_set():
                break

            sys.stderr.write(f"\nМетод {i}:\n")
            sys.stderr.flush()

            # Записываем маркер начала эмуляции
            marker = {
                "time": time.strftime("%H:%M:%S"),
                "action": f"start_emulation_{i}",
            }
            self.events.append(marker)
            sys.stderr.write(json.dumps(marker) + "\n")

            # Выполняем эмуляцию
            method()
            time.sleep(0.5)

            # Маркер завершения
            marker = {"time": time.strftime("%H:%M:%S"), "action": f"end_emulation_{i}"}
            self.events.append(marker)
            sys.stderr.write(json.dumps(marker) + "\n")
            sys.stderr.flush()

        self.emulating = False

    def run(self):
        print("=== Улучшенный эмулятор ===", file=sys.stderr)
        print("1. Нажмите любую букву", file=sys.stderr)
        print("2. Программа эмулирует B тремя способами", file=sys.stderr)
        print("3. ESC для выхода\n", file=sys.stderr)
        sys.stderr.flush()

        # Ждем первое нажатие
        while not self.should_exit.is_set():
            time.sleep(0.1)
            if any(
                e["key"] not in keyboard.all_modifiers
                for e in self.events
                if e.get("type") == "down"
            ):
                break

        if not self.should_exit.is_set():
            self.emulate_b()

            # Ждем ESC
            while not self.should_exit.is_set():
                time.sleep(0.1)

        keyboard.unhook_all()
        self.should_exit.set()

        print("\n=== Полный лог событий ===", file=sys.stderr)
        for event in self.events + self.raw_events:
            print(json.dumps(event), file=sys.stderr)
        print("\nПрограмма завершена", file=sys.stderr)


if __name__ == "__main__":
    emulator = KeyboardEmulator()
    emulator.run()
