import time

from .controller import Button, Controller
from .simulation import dry_run

command_map = {
    "a": Button.A,
    "b": Button.B,
    "x": Button.X,
    "y": Button.Y,
    "u": Button.DPAD_UP,
    "d": Button.DPAD_DOWN,
    "l": Button.DPAD_LEFT,
    "r": Button.DPAD_RIGHT,
}


def start_plotting(macro_path, is_dry_run):
    with open(macro_path, "r", encoding="utf-8") as fp:
        commands = fp.readlines()

    if is_dry_run:
        dry_run(commands)

        return

    print("Navigate to Change Grip/Order menu on your Nintendo Switch.")

    with Controller(press_ms=80, delay_ms=80) as ctl:
        print("Connected!")
        print("")

        input("Press <enter> key to continue.")

        buttons = [command_map[cmd.strip()] for cmd in commands]

        beg = time.time()
        ctl.macro(buttons)
        end = time.time()
        elapsed = time.strftime("%H:%M:%S", time.gmtime(end - beg))

        print("")
        print(f"`splatbot` took {elapsed} to complete your artwork!")
