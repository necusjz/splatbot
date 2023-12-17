import numpy as np
from PIL import Image
from skimage.measure import label
from tsp_solver.greedy_numpy import solve_tsp


def label_routes(matrix):
    matrix, count = label(matrix, return_num=True)

    routes = []
    for num in range(1, count + 1):
        condition = matrix == num

        curr_row = np.argwhere(condition)[0][0]
        is_right = True
        points = []

        route = []
        for point in np.argwhere(condition):
            if point[0] == curr_row:
                points.append(point)
            else:
                route += points if is_right else points[::-1]

                curr_row = point[0]
                is_right = not is_right
                points = [point]

        route += points if is_right else points[::-1]

        routes.append(route)

    return routes


def get_delta(p1, p2):
    return map(lambda x, y: x - y, p2, p1)


def manh(p1, p2):
    return sum(map(abs, get_delta(p1, p2)))


def cal_distance_matrix(endpoints):
    n = len(endpoints)
    distance_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(1, n):
            if i == j:
                continue

            distance_matrix[i][j] = manh(endpoints[i][1], endpoints[j][0])

    return distance_matrix


def goto_next(p1, p2):
    commands = []
    delta_x, delta_y = get_delta(p1, p2)

    commands += ["u", "d"][int(delta_x > 0)] * abs(delta_x)
    commands += ["l", "r"][int(delta_y > 0)] * abs(delta_y)

    return commands + ["a"]


def pathing(matrix):
    routes = label_routes(matrix)
    endpoints = [(route[0], route[-1]) for route in routes]

    distances = cal_distance_matrix(endpoints)

    commands, current = [], (0, 0)
    for i in solve_tsp(distances, optim_steps=16, endpoints=(0, None)):
        for point in routes[i]:
            commands += goto_next(current, point)
            current = point

    return commands + ["b"]  # save and quit


def generate_macro(image_path):
    with Image.open(image_path) as img:
        if img.size != (320, 120):
            raise ValueError("Image size must be 320 by 120 pixels.")

        img = img.convert("1")

        matrix = np.array(img.getdata()).reshape(120, 320) / 255
        matrix = 1 - matrix.astype(int)

    commands = pathing(matrix)

    with open("sequence", "w", encoding="utf-8") as fp:
        fp.write("\n".join(commands))
