import numpy as np
from PIL import Image


def generate_macro(image_path):
    with Image.open(image_path) as img:
        if img.size != (320, 120):
            raise ValueError("Image size must be 320 by 120 pixels.")

        img = img.convert("1")
        img = np.array(img.getdata()).reshape(120, 320) / 255
        img = 1 - img.astype(int)

    m, n = img.shape
    commands = []

    for i in range(m):
        if i != 0:
            commands.append("d")

        if not i & 1:
            for j in range(n):
                if img[i][j] == 1:
                    commands.append("a")

                if j != n - 1:
                    if commands and commands[-1] == "r":
                        commands += ["d", "u", "r"]
                    else:
                        commands.append("r")
        else:
            for j in range(n - 1, -1, -1):
                if img[i][j] == 1:
                    commands.append("a")

                if j != 0:
                    if commands[-1] == "l":
                        commands += ["u", "d", "l"]
                    else:
                        commands.append("l")

    commands.append("b")  # save and quit

    print("Benchmark: Pathing algorithm is ", end="")
    prev = 120 * 320 + np.count_nonzero(img)
    curr = len(commands)
    if curr < prev:
        print(f"{prev / curr:.2f}x faster ({curr} vs. {prev}).")
    else:
        print(f"{curr / prev:.2f}x slower ({curr} vs. {prev}).")

    with open("sequence", "w", encoding="utf-8") as fp:
        fp.write("\n".join(commands))
