def init_mass(size):
    return [0] * size

def init_num(size):
    return [0] * size

def get_input():
    try:
        return map(int, raw_input().split())
    except Exception:
        return [0, 0]

def is_end(N, M):
    return N == 0 and M == 0

def read_mass(N, mass):
    def read_one_mass(i, mass):
        mass[i] = input()
    for i in range(N):
        read_one_mass(i, mass)

def read_num(M, num):
    def read_one_num(i, num):
        num[i] = input()
    for i in range(M):
        read_one_num(i, num)

def process_moves(N, M, mass, num):
    def update_p(p, i):
        p += num[i]
        p += mass[p]
        return p
    def should_stop(p, N):
        return p >= N - 1
    def output_result(i):
        print i + 1
    def loop(M, N, mass, num):
        p = 0
        for i in range(M):
            p = update_p(p, i)
            if should_stop(p, N):
                output_result(i)
                break
    loop(M, N, mass, num)

def main_loop():
    mass = init_mass(2000)
    num = init_num(1000)
    while True:
        N, M = get_input()
        if is_end(N, M):
            break
        read_mass(N, mass)
        read_num(M, num)
        process_moves(N, M, mass, num)

main_loop()