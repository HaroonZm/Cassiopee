import sys
import itertools

def read_input():
    return sys.stdin.buffer.read()

def parse_input(data):
    return list(map(int, data.split()))

def extract_n_m_a(parsed):
    N = parsed[0]
    M = parsed[1]
    A = parsed[2:]
    return N, M, A

def lower_modulo(x, y, mod):
    return x - 1, y - 1, mod

def fragment_f():
    def cond_x_gt_y(x, y):
        return x > y

    def add_M(val, M):
        return val + M

    def cond_k_le_x(k, x):
        return k <= x

    def cond_k_le_y(k, y):
        return k <= y

    def result_expr1(y, k):
        return (y - k) + 1

    def result_expr2(y, x):
        return y - x

    def f(x, y, k, M):
        if cond_x_gt_y(x, y):
            y = add_M(y, M)
        if cond_k_le_x(k, x):
            k = add_M(k, M)
        if cond_k_le_y(k, y):
            return result_expr1(y, k)
        return result_expr2(y, x)
    return f

def initialize():
    add_X = 0
    add_DX = 0
    return add_X, add_DX

def initialize_DDX(M):
    return [0] * M

def process_pairs(A, M, add_X, add_DX, DDX, ffunc):
    for x, y in zip(A, A[1:]):
        x, y = x - 1, y - 1
        a = ffunc(x, y, M - 2, M)
        b = ffunc(x, y, M - 1, M)
        add_X += b
        add_DX += b - a
        d = y - x
        if d < 0:
            d += M
        DDX[(y + 1) % M] += d
        DDX[(y + 2) % M] -= (d - 1)
        DDX[(x + 2) % M] -= 1
    return add_X, add_DX, DDX

def calc_DX(DDX, add_DX):
    return [add_DX + y for y in itertools.accumulate(DDX)]

def calc_X(DX, add_X):
    return [add_X + y for y in itertools.accumulate(DX)]

def get_answer(X):
    return min(X)

def output(ans):
    print(ans)

def main():
    data = read_input()
    parsed = parse_input(data)
    N, M, A = extract_n_m_a(parsed)

    ffunc = fragment_f()

    add_X, add_DX = initialize()
    DDX = initialize_DDX(M)

    add_X, add_DX, DDX = process_pairs(A, M, add_X, add_DX, DDX, ffunc)
    DX = calc_DX(DDX, add_DX)
    X = calc_X(DX, add_X)
    ans = get_answer(X)
    output(ans)

main()