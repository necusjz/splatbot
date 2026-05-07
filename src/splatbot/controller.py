from nxbt import PRO_CONTROLLER, Nxbt


class Button:
    A = "A"
    B = "B"
    X = "X"
    Y = "Y"

    DPAD_UP = "DPAD_UP"
    DPAD_DOWN = "DPAD_DOWN"
    DPAD_LEFT = "DPAD_LEFT"
    DPAD_RIGHT = "DPAD_RIGHT"

    SHOULDER_L = "SHOULDER_L"
    SHOULDER_R = "SHOULDER_R"
    SHOULDER_ZL = "SHOULDER_ZL"
    SHOULDER_ZR = "SHOULDER_ZR"

    L_STICK_PRESS = "L_STICK_PRESS"
    R_STICK_PRESS = "R_STICK_PRESS"

    PLUS = "PLUS"
    MINUS = "MINUS"
    HOME = "HOME"
    CAPTURE = "CAPTURE"


class Controller:
    def __init__(self, press_ms, delay_ms):
        self.nx = Nxbt()
        self.index = self.nx.create_controller(PRO_CONTROLLER)
        self.press_ms = press_ms
        self.delay_ms = delay_ms

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()
        return False

    def connect(self):
        self.nx.wait_for_connection(self.index)

    def macro(self, buttons):
        macros = [f"{button} {self.press_ms/1000}s\n {self.delay_ms/1000}" for button in buttons]
        self.nx.macro(
            controller_index=self.index,
            macro="\n".join(macros)
        )

    def disconnect(self):
        self.nx.remove_controller(self.index)
