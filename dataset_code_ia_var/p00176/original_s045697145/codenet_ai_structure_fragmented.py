import math

def get_color_list():
    return [
        ("black", 0, 0, 0),
        ("blue", 0, 0, 255),
        ("lime", 0, 255, 0),
        ("aqua", 0, 255, 255),
        ("red", 255, 0, 0),
        ("fuchsia", 255, 0, 255),
        ("yellow", 255, 255, 0),
        ("white", 255, 255, 255)
    ]

def prompt_input():
    return raw_input()

def is_exit_input(s):
    return s == "0"

def extract_rgb(s):
    return (int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16))

def calculate_distance(r1, g1, b1, r2, g2, b2):
    return math.sqrt(pow(r1 - r2, 2) + pow(g1 - g2, 2) + pow(b1 - b2, 2))

def initial_min_distance():
    return 10000

def initial_closest_color():
    return None

def update_min_distance(t, m):
    return t < m

def set_new_min_distance(t):
    return t

def set_new_color(cl):
    return cl

def find_closest_color(rgb, color_list):
    Rk, Gk, Bk = rgb
    m = initial_min_distance()
    color = initial_closest_color()
    for cl, r, g, b in color_list:
        t = calculate_distance(r, g, b, Rk, Gk, Bk)
        if update_min_distance(t, m):
            m = set_new_min_distance(t)
            color = set_new_color(cl)
    return color

def process_color():
    color_list = get_color_list()
    while True:
        c = prompt_input()
        if is_exit_input(c):
            break
        rgb = extract_rgb(c)
        closest_color = find_closest_color(rgb, color_list)
        print closest_color

process_color()