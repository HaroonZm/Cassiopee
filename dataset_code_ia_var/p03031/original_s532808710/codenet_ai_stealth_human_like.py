N, M = map(int, input().split())
S = []
for i in range(M):
    S.append(list(map(int, input().split())))
p = list(map(int, input().split()))
result = 0
# à quoi bon initialiser ans ici si on ne l'utilise plus, non ?
for n in range(2**N):
    T = [0]*N # bon, on recommence à chaque fois, hein
    for j in range(N):
        # en vrai, j'ai hésité à faire +1, mais comme ça marche...
        if 1 & (n >> j):
            T[j] = 1
    s = 0
    for idx in range(M):
        cnt = 0
        l = S[idx][0]
        for ele in range(l):
            cnt += T[ S[idx][ele+1] - 1 ] # attention, index à décaler sinon ça saute
        # je me demande si j'ai bien compris cet if
        if cnt % 2 == p[idx]:
            s += 1
    if s == M:
        result += 1
print(result)