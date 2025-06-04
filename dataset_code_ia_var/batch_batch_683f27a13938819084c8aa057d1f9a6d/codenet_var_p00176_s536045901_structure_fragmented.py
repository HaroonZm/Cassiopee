import math

def get_sample_colors():
    return [
        [0, 0, 0], [0, 0, 255], [0, 255, 0], [0, 255, 255],
        [255, 0, 0], [255, 0, 255], [255, 255, 0], [255, 255, 255]
    ]

def get_sample_names():
    return ['black', 'blue', 'lime', 'aqua', 'red', 'fuchsia', 'yellow', 'white']

def read_color_input():
    return input()

def is_exit_code(color):
    return color == '0'

def extract_color_code(color):
    code_chars = list(color)
    return code_chars[1:]

def replace_hex_char_at_position(Color, i):
    hex_map = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    c = Color[i]
    if c in hex_map:
        Color.pop(i)
        Color.insert(i, hex_map[c])

def convert_hex_chars_to_ints(Color):
    for i in range(6):
        replace_hex_char_at_position(Color, i)
    return Color

def hex_list_to_rgb(Color):
    R = int(Color[0])*16 + int(Color[1])
    G = int(Color[2])*16 + int(Color[3])
    B = int(Color[4])*16 + int(Color[5])
    return [R, G, B]

def euclidean_distance(color1, color2):
    return math.sqrt(
        (color1[0] - color2[0]) ** 2 +
        (color1[1] - color2[1]) ** 2 +
        (color1[2] - color2[2]) ** 2
    )

def calculate_distances(rgb, samples):
    distances = []
    for i in range(len(samples)):
        d = euclidean_distance(rgb, samples[i])
        distances.append(d)
    return distances

def get_min_index(lst):
    min_val = min(lst)
    return lst.index(min_val)

def print_nearest_color_name(idx, names):
    print(names[idx])

def process_color_input(color, sample_colors, sample_names):
    code = extract_color_code(color)
    code = convert_hex_chars_to_ints(code)
    rgb = hex_list_to_rgb(code)
    distances = calculate_distances(rgb, sample_colors)
    idx = get_min_index(distances)
    print_nearest_color_name(idx, sample_names)

def main_loop():
    sample_colors = get_sample_colors()
    sample_names = get_sample_names()
    while True:
        color = read_color_input()
        if is_exit_code(color):
            break
        process_color_input(color, sample_colors, sample_names)

main_loop()