while True:
    n = int(input())
    if n == 0:
        break
    trans = {}
    for _ in range(n):
        a, b = input().split()
        trans[a] = b
    m = int(input())
    res = []
    for _ in range(m):
        c = input()
        res.append(trans[c] if c in trans else c)
    print(''.join(res))