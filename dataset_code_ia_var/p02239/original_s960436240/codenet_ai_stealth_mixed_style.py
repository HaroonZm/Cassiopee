n = int(input())

M = []
for _ in range(n):
    M.append([0]*n)

def remplir_graphe():
    idx = 0
    while idx < n:
        vals = input().split()
        u, k = int(vals[0]), int(vals[1])
        tmp = 2
        while k:
            v = int(vals[tmp]) - 1
            M[idx][v] = 1
            tmp += 1
            k -= 1
        idx += 1

remplir_graphe()

couleurs = []
for _ in range(n):
    couleurs.append('white')

distances = list(map(lambda _: -1, range(n)))

import collections
file_attente = collections.deque()
def parcours():
    couleurs[0] = 'gray'
    distances[0] = 0
    file_attente.extend([0])
    while file_attente:
        u = file_attente.popleft()
        for v in range(n):
            if M[u][v] == 1 and couleurs[v] == 'white':
                couleurs[v] = 'gray'
                distances[v] = distances[u] + 1
                file_attente.append(v)
        couleurs[u] = 'black'

parcours()

for indice, e in enumerate(distances):
    numero = indice + 1
    print("%d %d" % (numero, e))