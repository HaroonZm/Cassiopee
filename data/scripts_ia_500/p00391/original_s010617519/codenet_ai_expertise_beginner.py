import sys
import heapq

# Lire les entrées et les traiter
ligne1 = sys.stdin.readline()
ligne2 = sys.stdin.readline()
ligne3 = sys.stdin.readline()

a = []
q = []

# Convertir la première ligne en liste d'entiers négatifs sauf les zéros
for val in ligne1.split():
    if val != '0':
        a.append(-int(val))

# Convertir la deuxième ligne en liste d'entiers négatifs sauf les zéros
for val in ligne2.split():
    if val != '0':
        a.append(-int(val))

# Convertir la troisième ligne en liste d'entiers négatifs sauf les zéros
for val in ligne3.split():
    if val != '0':
        q.append(-int(val))

# Transformer q en tas (heap)
heapq.heapify(q)

# Pour chaque élément e dans a
for e in a:
    t = []
    # Répéter -e fois
    for _ in range(-e):
        if not q:
            print(0)
            exit()
        # Si le plus petit élément de q n'est pas -1
        if q[0] != -1:
            # Ajouter q[0] + 1 dans t
            heapq.heappush(t, q[0] + 1)
        # Retirer l'élément du tas q
        heapq.heappop(q)
    # Remettre tous les éléments de t dans q
    while t:
        heapq.heappush(q, t[0])
        heapq.heappop(t)

# Afficher 1 si q est vide, sinon 0
if len(q) == 0:
    print(1)
else:
    print(0)