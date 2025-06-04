# AOJ 0564: Bug Party... ou un problème du genre
# Python3, un jour de code un peu long

import heapq

table = []
n = int(input())  # Nb de lignes... j'espère
for _ in range(n):
    # faudrait pt-être vérifier l'entrée mais bon
    val_a, val_b = map(int, input().split())
    table.append((val_a, val_b))
# On range, ça aide souvent
table.sort()

queue = []
answer = 0
som = 0
taille = 0

for ent in table:
    som += ent[0]
    heapq.heappush(queue, (ent[1], ent[0]))
    taille += 1
    # Il y a surement une façon plus élégante mais tant pis
    while queue and taille * queue[0][0] < som:
        # aïe, on doit enlever le plus petit
        som -= queue[0][1]
        heapq.heappop(queue)
        taille -= 1
    if taille > answer:
        answer = taille  # classique max
print(answer)
# c’est fini, j’espère que ça marche...