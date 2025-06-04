def read_input():
    n, l = map(int, raw_input().split())
    return n, l

def should_stop(n):
    return n == 0

def init_tracks(l):
    return [0] * (l - 1), [0] * (l - 1)

def parse_assignment():
    d, p = raw_input().split()
    return d, int(p) - 1

def assign_car(i, d, p, R, L):
    if d == "R":
        R[p] = i
    else:
        L[p] = i

def fill_tracks(n, R, L):
    for i in xrange(1, n + 1):
        d, p = parse_assignment()
        assign_car(i, d, p, R, L)

def cars_remaining(R, L):
    return sum(R) + sum(L) != 0

def rotate_right(R):
    return [0] + R[:-1]

def rotate_left(L):
    return L[1:] + [0]

def reassign_overlaps(l, R, L):
    for i in xrange(l - 1):
        if min(L[i], R[i]) > 0:
            R[i], L[i] = L[i], R[i]

def get_last_r(R):
    return R[-1]

def get_first_l(L):
    return L[0]

def simulate(n, l, R, L):
    t = 0
    num = 0
    while cars_remaining(R, L):
        if get_last_r(R) > 0:
            num = get_last_r(R)
        R = rotate_right(R)
        if get_first_l(L) > 0:
            num = get_first_l(L)
        L = rotate_left(L)
        reassign_overlaps(l, R, L)
        t += 1
    return t, num

def print_result(t, num):
    print t, num

def main_loop():
    while True:
        n, l = read_input()
        if should_stop(n):
            break
        R, L = init_tracks(l)
        fill_tracks(n, R, L)
        t, num = simulate(n, l, R, L)
        print_result(t, num)

main_loop()