def read_n_l():
    n, l = map(int, raw_input().split())
    return n, l

def should_break(n):
    return n == 0

def initialize_tunnel(l):
    return [[] for _ in xrange(l-1)]

def read_direction_position():
    d, p = raw_input().split()
    return d, int(p)

def insert_in_tunnel(tunnel, idx, val):
    tunnel[idx].append(val)

def fill_tunnel(tunnel, n):
    for _ in xrange(1, n+1):
        d, p = read_direction_position()
        val = _ if d == "R" else -_
        insert_in_tunnel(tunnel, p-1, val)

def tunnel_is_empty(tunnel):
    return sum(len(unit) for unit in tunnel) == 0

def process_right_moves(tunnel, l):
    num = 0
    for i in xrange(l-2, -1, -1):
        for a in tunnel[i][:]:
            if a > 0:
                tunnel[i].remove(a)
                if i == l-2:
                    num = a
                else:
                    tunnel[i+1].append(a)
    return num

def process_left_moves(tunnel, l):
    num = 0
    for i in xrange(l-1):
        for a in tunnel[i][:]:
            if a < 0:
                tunnel[i].remove(a)
                if i == 0:
                    num = -a
                else:
                    tunnel[i-1].append(a)
    return num

def flip_signs_if_conflict(tunnel, l):
    for i in xrange(l-1):
        if len(tunnel[i]) > 1:
            tunnel[i] = [-a for a in tunnel[i]]

def process_tunnel(tunnel, l):
    t = 0
    num = 0
    while not tunnel_is_empty(tunnel):
        tmp_num_r = process_right_moves(tunnel, l)
        if tmp_num_r:
            num = tmp_num_r
        tmp_num_l = process_left_moves(tunnel, l)
        if tmp_num_l:
            num = tmp_num_l
        flip_signs_if_conflict(tunnel, l)
        t += 1
    return t, num

def main_loop():
    while True:
        n, l = read_n_l()
        if should_break(n):
            break
        tunnel = initialize_tunnel(l)
        fill_tunnel(tunnel, n)
        t, num = process_tunnel(tunnel, l)
        print t, num

main_loop()