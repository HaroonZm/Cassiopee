K = int(input())
def calc(a, b):
    if abs(X-a)+abs(Y-b) >= 2*K:
        if abs(X-a) >= K:
            r1 = K if X > a else -K
        else:
            r1 = abs(X-a) * (1 if X > a else -1)
        r2 = (K-abs(r1)) * (1 if Y > b else -1)
    elif abs(X-a)+abs(Y-b) == K:
        r1, r2 = X-a, Y-b
    else:
        rr = 2*K - abs(X-a)-abs(Y-b)
        rr = 0 if rr % 2 else rr//2
        if abs(X-a) < abs(Y-b):
            r1 = (abs(X-a)+rr) * (1 if X > a else -1)
            r2 = (K-abs(r1)) * (1 if Y > b else -1)
        else:
            r2 = (abs(Y-b)+rr) * (1 if Y > b else -1)
            r1 = (K-abs(r2)) * (1 if X > a else -1)
    return (a+r1, b+r2)

x, y = 0, 0
X, Y = map(int, input().split())
if K % 2 == 0 and (X+Y) % 2:
    print(-1)
else:
    ANS = []
    while x != X or y != Y:
        x, y = calc(x, y)
        ANS.append((x, y))

    print(len(ANS))
    for ans in ANS:
        print(*ans)