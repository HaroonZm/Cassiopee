def s(a):
    b, c = 0, 0
    for i in a:
        if i > b:
            b, c = i, b
        elif i > c:
            c = i
        else:
            return 0
    return 1

for _ in range(int(input())):
    print("YES" if s(map(int, input().split())) else "NO")