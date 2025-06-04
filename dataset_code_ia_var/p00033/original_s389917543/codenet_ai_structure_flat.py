n = int(input())
for _ in range(n):
    a = [int(x) for x in input().split()]
    stack = []
    stack.append(([], [], 0))
    found = False
    while stack:
        b, c, i = stack.pop()
        if len(b) + len(c) == 10:
            ok1 = True
            for j in range(1, len(b)):
                if b[j] < b[j-1]:
                    ok1 = False
                    break
            ok2 = True
            for j in range(1, len(c)):
                if c[j] < c[j-1]:
                    ok2 = False
                    break
            if ok1 and ok2:
                found = True
                break
            continue
        if i >= len(a):
            continue
        b2 = b + [a[i]]
        c2 = c + [a[i]]
        stack.append((b2, c, i+1))
        stack.append((b, c2, i+1))
    print('YES' if found else 'NO')