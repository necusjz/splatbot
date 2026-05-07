import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from tqdm import tqdm

offset_map = {
    "b": (0, 0),  # do nothing
    "u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)
}


def apply_offset(location, offset):
    i, j = location
    x, y = offset

    return i + x, j + y


def dry_run(commands):
    def update(_):
        progress_bar.update(1)

        try:
            cmd = next(commands).strip("\n")
        except StopIteration:
            anim.event_source.stop()

            return

        nonlocal loc
        data[loc] = 0 if data[loc] == 0.49 else 1

        if cmd == "a":
            data[loc] = 1
        else:
            loc = apply_offset(loc, offset_map[cmd])

        data[loc] = 0.51 if data[loc] == 1 else 0.49

        axs.clear()
        axs.imshow(data, cmap="gray_r")
        axs.axis("off")

    total = len(commands)
    progress_bar = tqdm(total=total, leave=False)

    commands = iter(commands)
    data = np.zeros((120, 320))
    loc, data[loc] = (0, 0), 0.49

    fig, axs = plt.subplots()
    anim = FuncAnimation(fig=fig, func=update, interval=0, save_count=total)
    axs.imshow(data, cmap="gray_r")
    axs.axis("off")

    plt.show()
