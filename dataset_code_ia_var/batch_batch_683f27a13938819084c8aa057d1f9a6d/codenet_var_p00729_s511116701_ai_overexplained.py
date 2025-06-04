# Démarrer une boucle qui ne s'arrêtera jamais sauf si on rencontre une instruction break à l'intérieur
while 1:
    # Lire une ligne entrée au clavier, la découper en morceaux selon les espaces,
    # convertir ces morceaux en entiers, et mettre ces entiers dans N et M.
    N, M = map(int, raw_input().split())
    
    # Si la valeur de N est égale à 0, alors on sort de la boucle, donc le programme principal s'arrête
    if N == 0:
        break

    # Créer une liste T, qui contient M sous-listes :
    # Chaque sous-liste contient 1261 éléments, tous initialisés à 0.
    # La notation [0]*1261 crée une liste de 1261 zéros,
    # for i in range(M) répète ce processus M fois pour former une matrice.
    T = [[0] * 1261 for i in range(M)]

    # Lire un entier au clavier, qui représentera le nombre de tuples d'intervalles temporels temporels
    r = input()

    # tnms va contenir des tuples : on lit r fois une ligne,
    # chaque ligne est transformée en liste d'entiers via map(int, ...),
    # tout ceci finit dans une liste via [ ... for i in range(r)].
    # Ensuite, on trie cette liste (méthode sorted),
    # en utilisant comme clé la valeur d'indice 1 de chaque tuple (= x[1]).
    tnms = sorted([map(int, raw_input().split()) for i in range(r)], key=lambda x: x[1])
    
    # On parcourt les indices de 0 à r-1 avec un pas de 2, c'est-à-dire deux par deux
    for i in range(0, r, 2):
        # Pour le i-ème élément, on récupère successivement t1, n, m, s
        t1, n, m, s = tnms[i]
        # Pour l'élément d'après (i+1), on écrase les mêmes variables avec les nouvelles valeurs
        t2, n, m, s = tnms[i+1]
        # Dans notre liste T, on s'intéresse au (m-1)-ème sous-tableau (car les listes commencent à 0),
        # On va remplacer les éléments à l'intervalle d'indices allant de t1 (inclus) à t2 (exclu)
        # par des 1 (c'est-à-dire que pour chaque temps dans cet intervalle, la valeur sera 1).
        # [1 for j in range(t1, t2)] construit une liste de 1 de la même longueur que t2-t1.
        T[m-1][t1:t2] = [1 for j in range(t1, t2)]

    # On lit un entier, qui sera le nombre de requêtes à traiter
    for i in range(input()):
        # On lit une ligne, on la découpe en trois entiers : ts, te, m
        ts, te, m = map(int, raw_input().split())
        # On affiche la somme de la tranche de la (m-1)-ème sous-liste T,
        # de l'indice ts (inclus) à te (exclu).
        # Cela compte le nombre de créneaux actifs (valeur à 1) dans ce segment de temps.
        print sum(T[m-1][ts:te])