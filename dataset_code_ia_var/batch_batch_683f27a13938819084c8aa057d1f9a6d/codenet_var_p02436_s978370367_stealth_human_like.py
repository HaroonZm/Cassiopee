from collections import deque

# lecture des entrées
n, c = map(int, input().split())
Q = []
for i in range(n):
    Q.append(deque())  # bon, on ajoute n files

for j in range(c):
    parts = (input() + " 0").split()
    if len(parts) < 3:  # ça peut arriver, soyons sûrs
        parts += ['0'] * (3 - len(parts))
    p = int(parts[0])
    t = int(parts[1])
    x = int(parts[2])

    if p == 0:
        Q[t].append(x)  # on ajoute à la file t
    elif p == 1:
        try:
            # afficher le premier élément, sauf si vide (sinon rien)
            print(Q[t][0])
        except:
            pass  # c'est vide, tant pis
    elif p == 2:
        if Q[t]:  # un petit check au cas où
            Q[t].popleft()
        else:
            pass  # rien à enlever

# je me demande si ces cas couvrent tout...