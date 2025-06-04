COLOR = {
    "000000": "black",
    "0000ff": "blue",
    "00ff00": "lime",
    "00ffff": "aqua",
    "ff0000": "red",
    "ff00ff": "fuchsia",
    "ffff00": "yellow",
    "ffffff": "white"
}

def get_next_input():
    return input()

def is_termination_input(s):
    return len(s) == 1

def get_paired_hex_chars(s):
    return list(zip(s[1::2], s[2::2]))

def compute_color_component(first, second):
    return "00" if int(first + second, 16) <= 127 else "ff"

def build_color_code(pairs):
    color = ""
    for first, second in pairs:
        color += compute_color_component(first, second)
    return color

def get_color_name(code):
    return COLOR[code]

def process_input(s):
    pairs = get_paired_hex_chars(s)
    color_code = build_color_code(pairs)
    return get_color_name(color_code)

def main_loop():
    while True:
        s = get_next_input()
        if is_termination_input(s):
            break
        result = process_input(s)
        print(result)

main_loop()