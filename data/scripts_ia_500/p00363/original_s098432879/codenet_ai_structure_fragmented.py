def read_dimensions_and_char():
    w, h, a = input().split()
    return int(w), int(h), a

def print_top_or_bottom_line(w):
    print("+" + "-" * (w - 2) + "+")

def print_middle_line(w, a):
    left_dots = (w - 2) // 2
    right_dots = (w - 2) // 2
    print("|" + "." * left_dots + a + "." * right_dots + "|")

def print_inner_line(w):
    print("|" + "." * (w - 2) + "|")

def is_top_or_bottom(i, h):
    return i == 0 or i == h - 1

def is_middle(i, h):
    return i == h // 2

def process_line(i, h, w, a):
    if is_top_or_bottom(i, h):
        print_top_or_bottom_line(w)
    elif is_middle(i, h):
        print_middle_line(w, a)
    else:
        print_inner_line(w)

def main():
    w, h, a = read_dimensions_and_char()
    for i in range(h):
        process_line(i, h, w, a)

main()