import sys

fetch = lambda : sys.stdin.readline().strip()

def ints():
    return list(map(int, fetch().split()))

def get_lines(n):
    out = []
    i = 0
    while i < n:
        out.append(fetch())
        i += 1
    return out

def int_lines(n):
    lines = []
    for _ in range(n):
        lines.append([int(c) for c in fetch()])
    return lines

if __name__ == '__main__':
    n = int(fetch())
    print(n ** 2)