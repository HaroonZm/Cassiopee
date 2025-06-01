import sys
import heapq

# Lire les entrées
ligne1 = sys.stdin.readline()
ligne2 = sys.stdin.readline()
ligne3 = sys.stdin.readline()

a = []
q = []

# Transformer les lignes en listes d'entiers négatifs sauf pour '0'
for e in ligne1.split():
    if e != '0':
        a.append(-int(e))
for e in ligne2.split():
    if e != '0':
        a.append(-int(e))
for e in ligne3.split():
    if e != '0':
        q.append(-int(e))

# Transformer q en tas
heapq.heapify(q)

for e in a:
    temp = []
    for i in range(-e):
        if not q:
            print(0)
            exit()
        val = heapq.heappop(q)
        if val != -1:
            heapq.heappush(temp, val + 1)
    while temp:
        heapq.heappush(q, heapq.heappop(temp))

if q:
    print(0)
else:
    print(1)