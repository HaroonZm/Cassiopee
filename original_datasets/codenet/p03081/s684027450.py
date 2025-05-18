N, Q = [int(x) for x in input().split()]
S = input()
TD = []
for _ in range(Q):
    t, d = input().split()
    TD.append((t, d))

def isDead(targetIdx):
    ti = targetIdx
    for t, d in TD:
        if t == S[ti]:
            if d == 'L':
                ti -= 1
                if ti == -1:
                    return -1
            else:
                ti += 1
                if ti == N:
                    return +1
    return 0

l, r = -1, N

while r - l > 1:
    t = (l + r) // 2
    if isDead(t) == -1:
        l = t
    else:
        r = t

L = r

l, r = -1, N

while r - l > 1:
    t = (l + r) // 2
    if isDead(t) == +1:
        r = t
    else:
        l = t

R = l

print(R - L + 1)

# print((L, R))
# print([isDead(t) for t in range(N)])