n = int(input())
A = []
for _ in range(n):
    ligne = input().split()
    B = []
    for x in ligne:
        B.append(int(x))
    A.append(B)

C = []
idx = 0
while idx < n:
    temp = list(map(int, input().split()))
    C.append(temp)
    idx += 1

utilise = [False for _ in range(n)]
reponse = 0

A = sorted(A, key=lambda elem: elem[1], reverse=True)

def comparer(u, v):
    return u[0] - v[0] if u[0] != v[0] else u[1] - v[1]

from functools import cmp_to_key
C = sorted(C, key=cmp_to_key(comparer))

for pair in C:
    trouve = False
    ix = 0
    # parcours style while + if imbriqué un peu à l'ancienne
    while ix < len(A):
        if not utilise[ix]:
            if not (A[ix][0] >= pair[0] or A[ix][1] >= pair[1]):
                reponse = reponse + 1
                utilise[ix] = True
                trouve = True
                break
        ix = ix + 1
    # continue style explicite
    if not trouve:
        pass

print(reponse)