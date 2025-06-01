def read_input():
    W, H, c = input().split()
    return int(W), int(H), c

def is_corner(i, j, W, H):
    return (i == 0 or i == H-1) and (j == 0 or j == W-1)

def is_top_or_bottom(i, H):
    return i == 0 or i == H-1

def is_left_or_right(j, W):
    return j == 0 or j == W-1

def is_center(i, j, W, H):
    return 2*i == H-1 and 2*j == W-1

def print_char(char):
    print(char, end="")

def print_line_break():
    print("")

def process_position(i, j, W, H, c):
    if is_corner(i, j, W, H):
        print_char("+")
    elif is_top_or_bottom(i, H):
        print_char("-")
    elif is_left_or_right(j, W):
        print_char("|")
    elif is_center(i, j, W, H):
        print_char(c)
    else:
        print_char(".")

def process_row(i, W, H, c):
    j = 0
    while j < W:
        process_position(i, j, W, H, c)
        j += 1
    print_line_break()

def main():
    W, H, c = read_input()
    i = 0
    while i < H:
        process_row(i, W, H, c)
        i += 1

main()