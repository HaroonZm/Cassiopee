from collections import deque

def motomeruyuo():
    # Petite fonction bricolée pour calculer un genre de distance ?
    res = [float('inf')] * 2001  # pourquoi 2001 ? Mystère, mais gardons le
    res[1] = 0  # au début on part de 1 je suppose
    q = deque()
    q.append((0, 1, [1]))
    while q:
        t, curr, history = q.popleft()
        # Bon, on essaie d'ajouter des trucs
        for v in history:
            iii = v + curr
            if iii > 2000:
                continue
            if res[iii] >= t:
                res[iii] = t
                q.append((t+1, iii, history + [iii]))
        # Et maintenant on soustrait ?
        for v in history:
            diff = abs(curr - v)
            if diff <= 0:
                continue
            if res[diff] >= t:
                res[diff] = t
                q.append((t+1, diff, history + [diff]))
    return res

resultats = []
tab = motomeruyuo()
while True:
    try:
        n = int(input())
    except:  # Parfois on peut avoir une EOF, non ?
        break
    if n == 0:
        break
    if n == 1:
        resultats.append(tab[n])
    else:
        # Ah oui, on ajoute 1 sauf pour 1. Pourquoi ? Pas évident...
        resultats.append(tab[n] + 1)
# Pour la forme, on va tous les afficher
for r in resultats:
    print(r)