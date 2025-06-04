from functools import partial
from operator import itemgetter

explosion = [i for i in range(-3, 4) if i] + [0] * 6
coords = tuple(zip(explosion, reversed(explosion)))

def bomb(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        field[cy][cx] = 0
        for dx, dy in coords:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if field[ny][nx] == 1:
                    stack.append((nx, ny))
                field[ny][nx] = 0

try: input_func = raw_input
except NameError: input_func = input

n = int(input_func())
for i in range(n):
    input_func()
    field = [list(map(int, input_func().strip())) for _ in range(8)]
    x = int(input_func()) - 1
    y = int(input_func()) - 1
    bomb(x, y)
    print(f"Data {i+1}:")
    print('\n'.join(''.join(map(str, row)) for row in field))