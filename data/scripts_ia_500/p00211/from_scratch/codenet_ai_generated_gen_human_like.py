import sys
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solve():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n_line = input_lines[idx].strip()
        idx += 1
        if n_line == '0':
            break
        n = int(n_line)
        d = []
        v = []
        for _ in range(n):
            di, vi = map(int, input_lines[idx].split())
            idx += 1
            d.append(di)
            v.append(vi)
        # lcm for ratios of (v_i/d_i)
        # We want the minimal T such that T * (v_i/d_i) is integer for all i
        # That means T * v_i is divisible by d_i => T divisible by d_i / gcd(d_i, v_i)
        # Compute li = d_i / gcd(d_i, v_i)
        lis = [di // math.gcd(di, vi) for di, vi in zip(d, v)]
        l = 1
        for li in lis:
            l = lcm(l, li)
        # For each student, number of laps = T * v_i / d_i = (lcm multiple) * v_i / d_i
        for di, vi in zip(d, v):
            laps = (l * vi) // di
            print(laps)

if __name__ == '__main__':
    solve()