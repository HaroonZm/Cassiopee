n = int(input())
for _ in range(n):
    s, d = map(int, input().split())
    stack = []
    stack.append((s, d))
    result = 0
    while stack:
        s1, d1 = stack.pop()
        if s1 == d1:
            continue
        if s1 & 1:
            result += 1
            s1 += 1
        if d1 & 1:
            result += 1
            d1 -= 1
        stack.append((s1 >> 1, d1 >> 1))
    print(result)