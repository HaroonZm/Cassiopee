import math

def get_palette_colors():
    return [
        [0, 0, 0], [0, 0, 255], [0, 255, 0], [0, 255, 255],
        [255, 0, 0], [255, 0, 255], [255, 255, 0], [255, 255, 255]
    ]

def get_palette_names():
    return [
        "black", "blue", "lime", "aqua",
        "red", "fuchsia", "yellow", "white"
    ]

def read_color_input():
    return input()

def is_exit(color_16):
    return color_16 == "0"

def parse_color_component(color_16, i, j):
    return int(color_16[i] + color_16[j], 16)

def parse_input_color(color_16):
    r = parse_color_component(color_16, 1, 2)
    g = parse_color_component(color_16, 3, 4)
    b = parse_color_component(color_16, 5, 6)
    return [r, g, b]

def calc_distance(color1, color2):
    return math.sqrt(
        (color1[0] - color2[0]) ** 2 +
        (color1[1] - color2[1]) ** 2 +
        (color1[2] - color2[2]) ** 2
    )

def min_palette_index(palette, color):
    min_d = float('inf')
    min_index = 0
    for i in range(len(palette)):
        d = calc_distance(palette[i], color)
        if d < min_d:
            min_d = d
            min_index = i
    return min_index

def print_palette_name(index):
    names = get_palette_names()
    print(names[index])

def process_color(color_16, palette):
    input_color = parse_input_color(color_16)
    index = min_palette_index(palette, input_color)
    print_palette_name(index)

def main_loop():
    while True:
        palette = get_palette_colors()
        color_16 = read_color_input()
        if is_exit(color_16):
            break
        process_color(color_16, palette)

main_loop()