S, T, D = map(int, input().split())
S -= T
*W, = map(int, input().split())
F = sum(W)
if F >= 0:
    su = S
    for i, w in enumerate(W):
        su += w
        if su <= 0:
            print(i+1)
            break
    else:
        print(-1)
    exit(0)
su = 0
mi = 0
for d in W:
    su += d
    mi = min(mi, su)

k = max((S+mi-F-1) // -F, 0)
S += k*F
for i, w in enumerate(W):
    S += w
    if S <= 0:
        print(i+1+k*D)
        break
else:
    assert 0