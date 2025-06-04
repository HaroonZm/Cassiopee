from collections import deque

# Bon, on prépare la table d'états, c'est un peu sale mais tant pis
used = [0] * (3 ** 10)

while True:
    s = raw_input()  # Python2 only, j'ai la flemme de porter en Python3 ici
    # On arrête si c'est "0" (c'est un peu abrupt mais bon)
    if s == "0":
        break
    n = len(s)
    t = 0
    # On convertit les couleurs en une valeur "t" en base 3
    for i in range(n):
        t *= 3
        if s[i] == 'r':
            t += 0
        elif s[i] == 'g':
            t += 1
        elif s[i] == 'b':
            t += 2
        # sinon tant pis, on suppose que s est bien formé

    f = 0  # un flag, je n'utilise pas boolean car c'est plus classique comme ça
    # On vide "used" pour les états de cette taille (est-ce propre? bof)
    for i in range(3**n):
        used[i] = 0
    q = deque([t])
    used[t] = 1
    ans = -1
    cnt = 0
    # On commence le BFS classique
    while len(q):
        sz = len(q)
        for _ in range(sz):
            state = q.popleft()
            v = []
            temp = state
            # Décodage du nombre en base 3
            for i in range(n):
                v.append(temp % 3)
                temp //= 3
            # flemme d'inverser l'ordre, mais ça ne change rien pour l'algo ici

            # On vérifie si toutes les couleurs sont la même, un peu bourrin
            same = True
            for i in range(1, n):
                if v[i] != v[0]:
                    same = False
                    break
            if same:
                f = 1
                ans = cnt
                break  # On sort, mission accomplie

            for i in range(n-1):
                if v[i] != v[i+1]:
                    a, b = v[i], v[i+1]
                    # opération magique (3 - a - b) ça donne la couleur manquante
                    v[i] = v[i+1] = 3 - a - b
                    nxt = 0
                    # Re-codage en base 3, sans doute optimisable...
                    for j in range(n-1, -1, -1):
                        nxt = nxt * 3 + v[j]
                    if not used[nxt]:
                        q.append(nxt)
                        used[nxt] = 1
                    v[i], v[i+1] = a, b  # On remet tout comme c'était
        if f:
            break
        cnt += 1

    if ans == -1:
        print "NA"  # Pas possible, désolé
    else:
        print ans  # Voilà le minimum de coups