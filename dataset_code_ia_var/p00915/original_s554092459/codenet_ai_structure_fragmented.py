def get_input():
    n, l = map(int, raw_input().split())
    return n, l

def should_break(n):
    return n == 0

def init_tubes(l):
    return [[] for _ in xrange(l - 1)]

def parse_ball_input(i):
    d, p = raw_input().split()
    dir_val = i if d == "R" else -i
    tube_index = int(p) - 1
    return tube_index, dir_val

def fill_tubes(n, l):
    tubes = init_tubes(l)
    for i in xrange(1, n + 1):
        idx, val = parse_ball_input(i)
        tubes[idx].append(val)
    return tubes

def tubes_empty(tubes):
    return sum(len(ele) for ele in tubes) == 0

def get_indices(l, direction):
    if direction == -1:
        return range(l - 1)[::-1]
    else:
        return range(l - 1)

def process_tube_movement(tubes, l, direction, num):
    for i in get_indices(l, direction):
        process_tube_at_index(tubes, i, direction, l, num)
    return num

def process_tube_at_index(tubes, i, direction, l, num):
    balls_to_move = []
    for a in tubes[i]:
        if -direction * a > 0:
            balls_to_move.append(a)
    for a in balls_to_move:
        tubes[i].remove(a)
        num = process_ball(tubes, i, direction, a, l, num)
    return num

def process_ball(tubes, i, direction, a, l, num):
    if (i == (l - 2) and direction == -1) or (i == 0 and direction == 1):
        num = abs(a)
    else:
        tubes[i - direction].append(a)
    return num

def invert_tube_if_needed(tubes, l):
    for i in xrange(l - 1):
        if len(tubes[i]) > 1:
            tubes[i] = [-a for a in tubes[i]]

def simulate_game(n, l, tubes):
    t = 0
    num = 0
    while not tubes_empty(tubes):
        for direction in [-1, 1]:
            num = process_tube_movement(tubes, l, direction, num)
        invert_tube_if_needed(tubes, l)
        t += 1
    return t, num

def main_loop():
    while True:
        n, l = get_input()
        if should_break(n):
            break
        tubes = fill_tubes(n, l)
        t, num = simulate_game(n, l, tubes)
        print t, num

main_loop()