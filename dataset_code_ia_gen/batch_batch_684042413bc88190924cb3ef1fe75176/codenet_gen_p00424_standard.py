while True:
    n = int(input())
    if n == 0:
        break
    conv = {}
    for _ in range(n):
        a,b = input().split()
        conv[a] = b
    m = int(input())
    res = []
    for _ in range(m):
        c = input()
        res.append(conv.get(c,c))
    print("".join(res))