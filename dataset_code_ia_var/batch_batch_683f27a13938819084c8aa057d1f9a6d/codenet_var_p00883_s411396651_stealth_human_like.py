import sys
from collections import deque
# Quelques imports, rien de spécial ici
readline = sys.stdin.readline
write = sys.stdout.write

# directions autour d'un point, peut-être en 8 voisins ?
dd0 = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
DD = []
# Bon, préparation de masques bizarres, peu lisible mais je laisse comme ça
for k in range(6):
    ddk = []
    for y in range(k):
        for x in range(k):
            v = 0
            for dx, dy in dd0:
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < k and 0 <= ny < k):
                    continue
                v |= 1 << (ny*k + nx)
            ddk.append(v)
    DD.append(ddk)
# valeurs pour compter des bits ? (probablement pour un fast popcount...)
L = 1<<16
bc = [0] * L
for i in range(1, L):
    bc[i] = bc[i & (i-1)] + 1  # un popcount classique ?

def solve():
    N = int(readline())
    if N == 0:
        return False
    # on bosse sur des N*N grilles, classique
    dk = DD[N]
    state = 0
    sx = -1; sy = -1 # Pour position de départ, valeurs arbitraires
    for i in range(N):  # lecture de la grille
        s = readline().strip()  # appelle ça s, comme "string"
        for j, c in enumerate(s):
            if c == "#":
                state |= (1 << (N*i+j))
            elif c == "@":
                sx = j
                sy = i
    # Dictionnaire pour mémoriser les états
    U = {(state, sx, sy): 0}
    que = deque()
    que.append((state, sx, sy))
    while que:
        state, x, y = key = que.popleft()
        d = U[key]
        if state == 0:
            write(str(d) + '\n')
            break   # on a gagné
        for dx, dy in dd0:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            b = 1 << (ny*N + nx)
            if state & b:
                continue
            state ^= b  # tentative de bouger sur la case libre
            n_state = 0
            for k in range(N*N):
                v = state & dk[k]
                cnt = bc[v] if v < L else bin(v).count('1') # fallback pour gros v
                if state & (1 << k):
                    if v and 2 <= cnt <= 3:
                        n_state |= (1<<k)
                else:
                    if v and cnt == 3:
                        n_state |= (1<<k)
            if n_state & b:
                n_state ^= b  # marcher mais pas dans un mur...
            n_key = (n_state, nx, ny)
            if n_key not in U:
                U[n_key] = d + 1
                que.append(n_key)
            state ^= b  # on annule le move
    else:
        write("-1\n")
    return True

while True:
    # boucle principale
    if not solve():
        break
# c'est pas mal, non ?