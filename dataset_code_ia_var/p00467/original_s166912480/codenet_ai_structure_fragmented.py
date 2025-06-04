def read_input():
    return iter(input, '0 0')

def parse_nm(e):
    return map(int, e.split())

def read_S(N):
    S = []
    for _ in range(N):
        S.append(int(input()))
    return S

def initial_position():
    return 1

def initial_b():
    return 1

def has_reached(N, p):
    return N <= p

def process_jump(p, d):
    return p + d

def get_S_value(S, p):
    return S[~-p]

def increment_i(i):
    return i + 1

def should_print(N, p, b):
    return has_reached(N, p) and b

def print_and_update_b(i):
    print(i + 1)
    return 0

def main_loop():
    for e in read_input():
        N, M = parse_nm(e)
        S = read_S(N)
        p = initial_position()
        b = initial_b()
        for i in range(M):
            d = int(input())
            p = process_jump(p, d)
            if has_reached(N, p):
                if b:
                    b = print_and_update_b(i)
                continue
            p += get_S_value(S, p)
            if should_print(N, p, b):
                b = print_and_update_b(i)
main_loop()