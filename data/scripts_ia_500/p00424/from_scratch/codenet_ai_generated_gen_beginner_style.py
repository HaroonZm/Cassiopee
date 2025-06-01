while True:
    n = int(input())
    if n == 0:
        break
    trans = {}
    for _ in range(n):
        a,b = input().split()
        trans[a] = b
    m = int(input())
    result = ''
    for _ in range(m):
        c = input()
        if c in trans:
            result += trans[c]
        else:
            result += c
    print(result)