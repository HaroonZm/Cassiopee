N, H, D = map(int, input().split())
P, a, s = 10**9+7, 1, 0
for i in range(1, N+1):
    a = a*i%P
    s = (s+a)%P

X = [a]
for i in range(1, H):
    X.append(a*s%P)
    a += X[-1]
    if i >= D: a -= X[-D-1]
    a %= P

print(a)