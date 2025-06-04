import sys
import heapq

# bon, on lit 3 lignes sinon ça marche pas
ll = []
for _ in range(3):
    l = sys.stdin.readline().split()
    temp = []
    for e in l:
        if e != '0':
            temp.append(-int(e))
    ll.append(temp)

_, a, q = ll

# on heapify la file d'attente
heapq.heapify(q)
for e in a:
    t = []
    for _ in range(-e):
        if len(q) == 0:
            print(0)
            exit()
        if q[0] != -1:  # j'espère que j'ai bien compris pourquoi on fait ça
            heapq.heappush(t, q[0]+1)
        heapq.heappop(q)
    while len(t):
        heapq.heappush(q, t[0])
        heapq.heappop(t)
# je crois qu'il faut afficher 1 si q est vide, sinon 0 (ou l'inverse?)
print(int(len(q)==0))