N = int(input())
S = input()
a0 = 0; a1 = 0; a2 = 0
P = [0]*N
for i, c in enumerate(S):
    if c == 'J':
        a0 += 1
    elif c == 'O':
        a1 += a0
    else:
        a2 += a1
    P[i] = a0

b0 = 0; b1 = 0; b2 = 0
Q = [0]*N
for i, c in enumerate(reversed(S)):
    if c == 'I':
        b0 += 1
    elif c == 'O':
        b1 += b0
    else:
        b2 += b1
    Q[-1-i] = b0

res = max(a1, b1)
for i in range(N):
    res = max(res, P[i] * Q[i])
print(res + a2)