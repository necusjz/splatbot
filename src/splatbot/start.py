import time

from .controller import Button
from .controller import Controller


command_map = {
    "a": Button.A,
    "b": Button.B,
    "x": Button.X,
    "y": Button.Y,
    "u": Button.DPAD_UP,
    "d": Button.DPAD_DOWN,
    "l": Button.DPAD_LEFT,
    "r": Button.DPAD_RIGHT
}


def start_plotting(macro_path):
    with open(macro_path, "r", encoding="utf-8") as fp:
        commands = fp.readlines()

    print("Navigate to Change Grip/Order menu on your Nintendo Switch.")

    with Controller(press_ms=600, delay_ms=7000) as ctl:
        print("Connected!")
        input("Press <enter> key to start plotting...")

        buttons = [command_map[cmd.strip()] for cmd in commands]

        start = time.time()
        ctl.macro(buttons)
        end = time.time()
        elapsed = time.strftime("%H:%M:%S", time.gmtime(end - start))

        print(f"`splatbot` took {elapsed} to complete your artwork.")
