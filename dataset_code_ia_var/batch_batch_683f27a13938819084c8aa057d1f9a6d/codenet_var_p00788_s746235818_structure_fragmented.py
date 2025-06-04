import sys
import math

def parse_input_line():
    line = input().split()
    return map(int, list(line))

def compute_rt_and_k(p):
    rt = math.sqrt(p)
    k = math.floor(rt)
    return rt, k

def init_values(n):
    mi = n
    mx = n
    mikk = 0
    mibb = 0
    mxkk = 0
    mxbb = 0
    return mi, mx, mikk, mibb, mxkk, mxbb

def compute_a(rt, k, i):
    return (rt - k) * i

def compute_b(a):
    return math.floor(a)

def update_min(mi, a, b, k, i, n, mikk, mibb):
    if mi > a - b and k * i + b <= n:
        return a - b, i, b
    return mi, mikk, mibb

def update_max(mx, a, b, k, i, n, mxkk, mxbb):
    if mx > b + 1 - a and k * i + (b + 1) <= n:
        return b + 1 - a, i, b
    return mx, mxkk, mxbb

def format_result(k, mxkk, mxbb, mikk, mibb):
    num1 = k * mxkk + (mxbb + 1)
    den1 = mxkk
    num2 = k * mikk + mibb
    den2 = mikk
    return "{}/{} {}/{}".format(num1, den1, num2, den2)

def rational(p, n):
    rt, k = compute_rt_and_k(p)
    mi, mx, mikk, mibb, mxkk, mxbb = init_values(n)
    for i in range(1, n+1):
        a = compute_a(rt, k, i)
        b = compute_b(a)
        mi, mikk, mibb = update_min(mi, a, b, k, i, n, mikk, mibb)
        mx, mxkk, mxbb = update_max(mx, a, b, k, i, n, mxkk, mxbb)
    result = format_result(k, mxkk, mxbb, mikk, mibb)
    print(result)

def should_break(p, n):
    return p == 0 and n == 0

def main_loop():
    while True:
        p, n = parse_input_line()
        if should_break(p, n):
            break
        rational(p, n)

main_loop()