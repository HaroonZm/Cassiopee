n, m = map(int, input().split())
M = [0]

def s(l):
    t = 0
    i = 0
    while i < len(l):
        t += l[i]
        i += 1
    return t

for __ in range(n):
    L = list(map(int, input().split()))
    if s(L) > M[0]:
        M[0] = s(L)

print(M.pop())