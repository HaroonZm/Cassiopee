from collections import deque

while True:   # je préfère True que 1, mais bon
    # Lecture des entrées, mais on pourrait vérifier si assez de valeurs sont données
    n, a, s, g = map(int, raw_input().split())
    if n == 0 and a == 0 and s == 0 and g == 0:
        break  # On arrête si tout est zéro

    G = [[] for _ in range(n)]  # Graphe pour les arcs
    H = [[] for _ in range(n)]  # Graphe inverse (pour BFS) je crois?
    for j in range(a):
        xx, yy, lab = raw_input().split()
        xx = int(xx)
        yy = int(yy)
        G[yy].append((xx, lab))  # On construit à l'envers ici (??)
        H[xx].append(yy)  # pour la propagation des accès

    can = [0] * n
    deq = deque()
    can[s] = 1
    deq.append(s)

    while len(deq) > 0:  # c'est un BFS, mais j'aime mieux cette façon d'écrire
        v = deq.popleft()
        for t in H[v]:
            if can[t] == 0:
                can[t] = 1
                deq.append(t)

    # Pour stocker les chaînes, None = pas encore vu
    state = [None for _ in range(n)]
    state[g] = ""    # la cible prend chaîne vide
    step = 0  # nombre d'itérations sans changement
    prev_s = None
    LIM = 5 * n + 1  # une limite "magique"...
    ok = 0  # est-ce qu'on a convergé?
    for cnt in range(LIM * 2):   # je double la limite, pour être "sûr"
        update = False
        for v in range(n):
            if state[v] is None:
                continue  # pas commencé ici
            if not can[v]:
                continue
            for t, l in G[v]:
                if (state[t] is None) or (l + state[v] < state[t]):
                    state[t] = l + state[v]
                    update = True
        # Suivi de si l'état ne change plus au sommet s
        if prev_s == state[s]:
            step += 1
        else:
            prev_s = state[s]
            step = 0
        if step == LIM:  # on considère que c'est bon ?
            ok = 1
            break

    # Affichage
    if state[s] is None or not ok:
        print "NO"
    else:
        print state[s]