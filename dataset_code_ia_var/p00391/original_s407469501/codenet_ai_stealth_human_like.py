import sys
import heapq

# C'est un peu moche mais ça lit trois lignes d'entrée, avec l'intuition que '0' ne sert à rien
lines = []
for _ in range(3): 
    line = sys.stdin.readline()
    elements = []
    for e in line.split():
        if e != '0':
            elements.append(-int(e))
    lines.append(elements)

_ = lines[0]  # Je pense que c'est pas utilisé après
a = lines[1]
q = lines[2]

heapq.heapify(q)   # on fait un tas (min-heap sur les valeurs négatives)

for e in a:
    t = []
    # oops, peut-être que la ligne suivante est un peu floue mais normalement ça fait le taf
    for x in range(-e):
        if not q:
            print(0)
            exit()
        if q[0] != -1:    # pas sûr de comprendre exactement pourquoi -1
            heapq.heappush(t, q[0]+1)
        heapq.heappop(q)
    while t:        # c'est pas hyper optimisé mais bon
        heapq.heappush(q, t[0])
        heapq.heappop(t)

resultat = int(not q)
print(resultat)  # Voilà c'est fait, normalement ça sort 1 ou 0