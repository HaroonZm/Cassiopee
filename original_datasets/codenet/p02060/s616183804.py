def inpl(): return list(map(int, input().split()))

N = int(input())
P = inpl()
T = inpl()

cost = 10**9
for a in range(-(-N//T[0]) + 1):
    costa = P[0]*a
    teaa = T[0]*a
    rema = N - teaa
    for b in range(max(1, -(-rema//T[1]) + 1)):
        costb = P[1] * b
        teab = T[1]*b
        remb = max(rema - teab, 0)
        for c in range(max(1, -(-remb//T[2]) + 1)):
            costc = P[2] * c
            teac = T[2] * c
            remc = max(remb - teac, 0)
            
            d = max(-(-remc//T[3]), 0)
            costd = P[3] * d
            tead = T[3] * d

            cost = min(cost, costa + costb + costc + costd)
print(cost)