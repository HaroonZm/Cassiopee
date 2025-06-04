def read_input():
    w, h, n = map(int, input().split())
    coords = []
    for _ in range(n):
        x, y = map(int, input().split())
        coords.append([x, y])
    return w, h, coords

def extract_start(coords):
    start = coords.pop(0)
    return start[0], start[1], coords

def is_at_destination(x1, y1, x2, y2):
    return x1 == x2 and y1 == y2

def move_up_right(x1, y1):
    return x1 + 1, y1 + 1

def move_up(y1):
    return y1 + 1

def move_left(x1):
    return x1 - 1

def move_right(x1):
    return x1 + 1

def move_down_left(x1, y1):
    return x1 - 1, y1 - 1

def move_down(y1):
    return y1 - 1

def move(x1, y1, x2, y2, w, h):
    if x1 < x2 and y1 < y2:
        x1, y1 = move_up_right(x1, y1)
    elif x1 == x2 and y1 < y2:
        y1 = move_up(y1)
    elif x1 > x2 and y1 < y2:
        if y1 != h:
            y1 = move_up(y1)
        else:
            x1 = move_left(x1)
    elif x1 < x2 and y1 == y2:
        x1 = move_right(x1)
    elif x1 > x2 and y1 == y2:
        x1 = move_left(x1)
    elif x1 < x2 and y1 > y2:
        if y1 != 0:
            y1 = move_down(y1)
        else:
            x1 = move_right(x1)
    elif x1 == x2 and y1 > y2:
        y1 = move_down(y1)
    elif x1 > x2 and y1 > y2:
        x1, y1 = move_down_left(x1, y1)
    return x1, y1

def process_single_destination(x1, y1, x2, y2, w, h):
    steps = 0
    while not is_at_destination(x1, y1, x2, y2):
        x1, y1 = move(x1, y1, x2, y2, w, h)
        steps += 1
    return x1, y1, steps

def process_all_destinations(x1, y1, destinations, w, h):
    total_steps = 0
    for dest in destinations:
        x2, y2 = dest
        x1, y1, steps = process_single_destination(x1, y1, x2, y2, w, h)
        total_steps += steps
    return total_steps

def main():
    w, h, coords = read_input()
    x1, y1, destinations = extract_start(coords)
    steps = process_all_destinations(x1, y1, destinations, w, h)
    print(steps)

main()