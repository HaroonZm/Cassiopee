def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def can_unlock(N, M, L):
    g = 0
    for i in range(M):
        g = gcd(g, L[i])
    if g == 0:
        return "No"
    if N % g == 0:
        return "Yes"
    else:
        return "No"

N, M = map(int, input().split())
L = []
for _ in range(M):
    L.append(int(input()))
print(can_unlock(N, M, L))