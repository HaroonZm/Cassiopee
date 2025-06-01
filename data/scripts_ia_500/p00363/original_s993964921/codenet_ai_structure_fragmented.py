def read_input():
    W, H, c = input().split()
    return W, H, c

def convert_to_int(W, H):
    return int(W), int(H)

def is_corner(x, y, W, H):
    return (x, y) == (0, 0) or (x, y) == (0, H-1) or (x, y) == (W-1, 0) or (x, y) == (W-1, H-1)

def is_vertical_edge(x, W):
    return x == 0 or x == W-1

def is_horizontal_edge(y, H):
    return y == 0 or y == H-1

def is_center(x, y, W, H):
    return (x, y) == ((W-1)//2, (H-1)//2)

def print_char(char):
    print(char, end='')

def print_newline():
    print()

def print_line(W, y, H, c):
    for x in range(W):
        print_char(determine_char_for_position(x, y, W, H, c))
    print_newline()

def determine_char_for_position(x, y, W, H, c):
    if is_corner(x, y, W, H):
        return '+'
    if is_vertical_edge(x, W):
        return '|'
    if is_horizontal_edge(y, H):
        return '-'
    if is_center(x, y, W, H):
        return c
    return '.'

def main():
    W, H, c = read_input()
    W, H = convert_to_int(W, H)
    for y in range(H):
        print_line(W, y, H, c)

main()