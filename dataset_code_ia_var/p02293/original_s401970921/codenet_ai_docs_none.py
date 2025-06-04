for _ in range(int(input())):
    px0, py0, px1, py1, px2, py2, px3, py3 = map(int, input().split())
    a, b, c, d = px1 - px0, py1 - py0, px3 - px2, py3 - py2
    if a * c == -b * d:
        print(1)
    elif a * d == b * c:
        print(2)
    else:
        print(0)