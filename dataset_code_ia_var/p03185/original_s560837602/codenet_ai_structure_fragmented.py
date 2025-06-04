def read_input():
    data = open(0).read().split()
    n = int(data[0])
    C = int(data[1])
    H = list(map(int, data[2:]))
    return n, C, H

def init_lists():
    return [0], [0]

def get_h(H, i):
    return H[i]

def get_P_value(P, p, H, x, y, h):
    return (p[P[y]] - p[P[x]]) / (H[P[x]] - H[P[y]]) - H[P[y]] - H[P[x]] + 2 * h

def pop_first(P):
    P.pop(0)

def pop_second_last(P):
    P.pop(-2)

def last_index(P):
    return P[-1]

def second_last_index(P):
    return P[-2]

def third_last_index(P):
    return P[-3]

def update_p(p, P, H, C, i, h):
    value = p[P[0]] + (H[P[0]] - h) ** 2 + C
    p.append(value)

def update_P(P, i):
    P.append(i)

def process_main_loop(n, C, H, p, P):
    for i in range(1, n):
        loop_step(i, C, H, p, P)

def loop_step(i, C, H, p, P):
    h = get_h(H, i)
    remove_by_g_first(P, p, H, h)
    update_p(p, P, H, C, i, h)
    update_P(P, i)
    h = reset_h()
    remove_by_g_second(P, p, H, h)

def remove_by_g_first(P, p, H, h):
    def g(x, y):
        return get_P_value(P, p, H, x, y, h)
    while len(P) > 1 and g(1, 0) > 0:
        pop_first(P)

def remove_by_g_second(P, p, H, h):
    def g(x, y):
        return get_P_value(P, p, H, x, y, h)
    while len(P) > 2 and g(-1, -2) > g(-2, -3):
        pop_second_last(P)

def reset_h():
    return 0

def print_result(p):
    print(p[-1])

def main():
    n, C, H = read_input()
    p, P = init_lists()
    process_main_loop(n, C, H, p, P)
    print_result(p)

main()