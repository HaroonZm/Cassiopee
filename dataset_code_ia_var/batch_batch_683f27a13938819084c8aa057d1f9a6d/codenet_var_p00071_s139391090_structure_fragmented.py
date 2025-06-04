from itertools import chain

def get_explosion_offsets():
    return [i for i in range(-3, 4) if i] + [0] * 6

def initialize_field():
    return [[int(c) for c in read_line()] for _ in range(8)]

def read_line():
    return raw_input()

def read_and_discard_line():
    read_line()

def read_coord():
    return input() - 1

def in_bounds(v):
    return v in range(0, 8)

def set_cell_zero(field, x, y):
    field[y][x] = 0

def should_bomb(field, x, y):
    return field[y][x] == 1

def process_field_line(field):
    return "".join(str(i) for i in field)

def print_header(idx):
    print "Data %d:" % (idx + 1)

def print_field(field):
    for row in field:
        print process_field_line(row)

def bomb_recurse(field, x, y, explosion):
    set_cell_zero(field, x, y)
    dxs = explosion
    dys = list(reversed(explosion))
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_bounds(nx) and in_bounds(ny):
            if should_bomb(field, nx, ny):
                bomb_recurse(field, nx, ny, explosion)
            set_cell_zero(field, nx, ny)

def handle_case(idx, explosion):
    read_and_discard_line()
    field = initialize_field()
    x = read_coord()
    y = read_coord()
    bomb_recurse(field, x, y, explosion)
    print_header(idx)
    print_field(field)

def main():
    explosion = get_explosion_offsets()
    num_cases = input()
    for i in xrange(num_cases):
        handle_case(i, explosion)

main()