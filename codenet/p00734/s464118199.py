def solve(a, b):
    a.sort()
    b.sort()
    d = sum(a) - sum(b)
    if d % 2 != 0:
        return -1
    for x in a:
        for y in b:
            if x - y == d/2:
                return " ".join(map(str,[x, y]))
            if x - y <  d/2:
                break
    return -1

while True:
    n, m = map(int, raw_input().split())
    if n == 0 and m == 0:
        break
    s = [int(raw_input()) for _ in range(n+m)]
    #print s[:n], s[n:], sum(s[:n]), sum(s[n:])
    print solve(s[:n], s[n:])