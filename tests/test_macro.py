from pathlib import Path

import numpy as np
from PIL import Image
from tabulate import tabulate

from src.splatbot.macro import pathing


def test_pathing():
    dataset = Path("tests/dataset")
    data = []

    for image in sorted(dataset.iterdir()):
        image_path = dataset / image.name

        with Image.open(image_path) as img:
            matrix = np.array(img.getdata()).reshape(120, 320) / 255
            matrix = 1 - matrix.astype(int)

        curr = len(pathing(matrix))
        prev = 120 * 320 + np.count_nonzero(matrix)
        result = f"{prev / curr:.2f}x faster" if curr <= prev else f"{curr / prev:.2f}x slower"

        data.append((image.name, curr, prev, result))

    headers = ["Benchmark", "Current", "Previous", "Result"]

    print("")
    print(tabulate(data, headers=headers, tablefmt="grid", numalign="left"))
