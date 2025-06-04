import collections

def float_input():
    return float(input())

def int_input():
    return int(input())

def list_int_input():
    return list(map(int, input().split()))

def main():
    p = float_input()
    n = int_input()
    d = {}
    for _ in range(n-1):
        x, y, c = list_int_input()
        x -= 1
        y -= 1
        if x not in d:
            d[x] = []
        if y not in d:
            d[y] = []
        d[x].append((y, c))
        d[y].append((x, c))
    f = [None] * n
    f[0] = (0, 0)
    queue = [(0, 0)]
    while queue:
        x, b = queue[0]
        queue = queue[1:]
        for y, c in d.get(x, []):
            if f[y] is not None:
                continue
            queue.append((y, b+1))
            f[y] = (b+1, c)

    s = 0
    for b, c in f:
        s += (p ** b) * c

    r = s
    for b, c in f:
        r += (p ** b) * s

    return r

print(main())