def read_input():
    return int(input())

def read_blocks(n):
    blocks = []
    for _ in range(n):
        line = input()
        d, p, q = map(int, line.split())
        blocks.append((d, p, q))
    return blocks

def create_field(height, width):
    return [[0]*width for _ in range(height)]

def can_place_horizontal(field, li, q, p):
    return field[li][q-1:q+p-1] == [0]*p

def place_horizontal(field, li, q, p):
    for index in range(q-1, q+p-1):
        field[li][index] = 1

def can_place_vertical(field, li, q):
    return field[li][q-1] == 0

def place_vertical(field, li, q, p):
    for idx in range(p):
        field[li+idx][q-1] = 1

def drop_horizontal_block(field, h, p, q):
    li = h
    while True:
        li -= 1
        if li == -1 or not can_place_horizontal(field, li, q, p):
            place_horizontal(field, li + 1, q, p)
            h = max(h, li + 2)
            return h

def drop_vertical_block(field, h, p, q):
    li = h
    while True:
        li -= 1
        if li == -1 or not can_place_vertical(field, li, q):
            place_vertical(field, li + 1, q, p)
            h = max(h, li + 1 + p)
            return h

def remove_filled_lines(field, h):
    i = 0
    while True:
        if field[i] == [1]*5:
            del field[i]
            h -= 1
        elif field[i] == [0]*5:
            break
        else:
            i += 1
    return h

def sum_field(field, h):
    total = 0
    for li in range(h):
        total += sum(field[li])
    return total

def main_loop():
    hmax = 7500
    while True:
        n = read_input()
        if n == 0:
            break
        block = read_blocks(n)
        field = create_field(hmax, 5)
        h = 0
        for d, p, q in block:
            if d == 1:
                h = drop_horizontal_block(field, h, p, q)
            else:
                h = drop_vertical_block(field, h, p, q)
            h = remove_filled_lines(field, h)
        print(sum_field(field, h))

main_loop()