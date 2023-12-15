import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from tqdm import tqdm


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
            x, y = loc
            if cmd == "u":
                loc = (x - 1, y)
            if cmd == "d":
                loc = (x + 1, y)
            if cmd == "l":
                loc = (x, y - 1)
            if cmd == "r":
                loc = (x, y + 1)

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
