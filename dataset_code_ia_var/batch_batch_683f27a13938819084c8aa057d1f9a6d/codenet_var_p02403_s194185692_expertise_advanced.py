from sys import stdin, stdout

def generate_rectangles():
    for line in stdin:
        H, W = map(int, line.split())
        if not (H or W):
            break
        block = ('#' * W + '\n') * H
        stdout.write(block + '\n')

generate_rectangles()