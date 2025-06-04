import sys  # Importation du module sys qui permet d'interagir avec des objets système
readline = sys.stdin.readline  # On crée un alias pour sys.stdin.readline() afin de lire une ligne de l'entrée standard plus facilement
write = sys.stdout.write  # On crée un alias pour sys.stdout.write() pour écrire facilement sur la sortie standard

def solve():
    # On lit les entiers N (nombre de sommets), M (nombre d'arêtes), et K (taille recherchée)
    N, M, K = map(int, readline().split())
    # On initialise le graphe G comme une liste de N listes vides, chaque sous-liste représente la liste d'adjacence d'un sommet
    G = [[] for i in range(N)]
    # On définit une constante 'INF', ici très grande, qui servira d'infini négatif
    INF = 10**18
    # On lit les M arêtes du graphe
    for i in range(M):
        # Pour chaque arête, on lit les sommets 'a' et 'b' (indices 1-based) et la valeur 'c'
        a, b, c = map(int, readline().split())
        # Si le coût c est 0, on le remplace par -INF comme précisé dans l'énoncé
        if c == 0:
            c = -INF
        # On ajoute l'arête (b-1, c) dans la liste d'adjacence du sommet a-1 (car on travaille en 0-based)
        G[a-1].append((b-1, c))
        # On ajoute aussi l'arête (a-1, c) dans la liste d'adjacence du sommet b-1 (graphes non orientés)
        G[b-1].append((a-1, c))

    # Fonction pour calculer le maximum de somme possible pour un chemin ou pour un cycle dans une structure linéaire
    def calc(K, U, l):
        # Si l vaut 0 (on traite une chaîne/simple chemin)
        if not l:
            # On crée une liste X de taille K+1 initialisée à -INF, qui va contenir les maximums atteignables pour chaque taille de sous-séquence
            X = [-INF]*(K+1)
            # S0 et S1 sont des tableaux pour stocker respectivement les sommes où on ne prend pas le dernier sommet, et où on le prend
            S0 = [-INF]*(K+1)
            S1 = [-INF]*(K+1)
            # On initialise S0[0]=0 (somme vide), S1[1]=0 (prendre 1 élément au début)
            S0[0] = S1[1] = 0
            # On parcourt chaque élément à partir de l'indice 1 (car le chemin commence à U[1])
            for i in range(1, K):
                e = U[i]
                # On parcourt les tailles j en sens inverse
                for j in range(K-1, -1, -1):
                    # On met à jour S1 : prendre un nouvel élément, soit en démarrant de S0[j], soit en continuant une chaîne prise déjà dans S1[j]
                    S1[j+1] = max(S0[j], S1[j] + e)
                    # On met à jour S0 : pas de prise à cette position
                    S0[j] = max(S0[j], S1[j])
            # On prend le maximum possible pour chaque taille dans X
            for i in range(K+1):
                X[i] = max(S0[i], S1[i])
        else:
            # Si l == 1 (cycle), alors on calcule d'abord la solution pour le chemin correspondant de taille K-1 (sans le premier sommet)
            X = calc(K-1, U[1:], 0) + [-INF]
            # S0 et S1 initialisés pour ce cycle
            S0 = [-INF]*K
            S1 = [-INF]*K
            # On commence à S0[0]=0 (aucun sommet pris), S1[1]=U[1] (on prend U[1] comme commencement)
            S0[0] = 0; S1[1] = U[1]
            for i in range(2, K):
                e = U[i]
                for j in range(K-2, -1, -1):
                    S1[j+1] = max(S0[j], S1[j] + e)
                    S0[j] = max(S0[j], S1[j])
            # On traite ici l'effet cyclique par ajout de U[0]
            e = U[0]
            for i in range(K):
                X[i+1] = max(X[i+1], S0[i], S1[i] + e)
        return X

    # Initialisation d'une liste qui marque l'état d'exploration de chaque sommet
    used = [0]*N  # 0 = non traité, 1 = sommet isolé, 2 = chaîne, 3 = cycle
    sg = 0  # Variable non utilisée, laissée du code original
    # Initialisation d'un tableau dp de taille N+1 qui retient pour chaque taille de sous-séquence la somme maximale possible
    dp = [-INF]*(N+1)
    dp[0] = 0  # Avec 0 sommets sélectionnés, la somme maximale est 0

    # On parcourt chaque sommet du graphe
    for i in range(N):
        # Si ce sommet a déjà été traité, on le saute
        if used[i]:
            continue
        # Si le sommet n'a aucune arête (sommet isolé)
        if len(G[i]) == 0:
            used[i] = 1  # On le marque comme traité
            # On met à jour le dp : On peut constituer une solution de taille augmentée de 1 sans changer la somme (sommets isolés = somme nulle)
            for i in range(N-1, -1, -1):
                dp[i+1] = max(dp[i+1], dp[i])
            continue
        # Si le sommet est le début d'une chaîne (un seul voisin)
        if len(G[i]) == 1:
            used[i] = 2  # On le marque comme appartenant à une chaîne
            v, c = G[i][0]  # v est le voisin, c est le coût de l'arête qui les relie
            r = [i]  # r va contenir les indices du chemin
            u = [0, c]  # u contiendra la séquence des coûts entre les sommets, commençant à 0 au premier sommet
            # On propage le long de la chaîne tant qu'on n'atteint pas une extrémité
            while len(G[v]) == 2:
                r.append(v)  # On ajoute le sommet à la chaîne
                used[v] = 2  # On marque comme traité
                w1, w2 = G[v]  # Les deux voisins du sommet v
                # On choisit le voisin non encore traité pour continuer la chaîne
                if used[w1[0]]:
                    v, c = w2
                    u.append(c)
                else:
                    v, c = w1
                    u.append(c)
            r.append(v)  # On ajoute le dernier sommet
            used[v] = 2  # On le marque comme traité
            L = len(r)  # Longueur de la chaîne
            # On appelle la fonction calc sur cette chaîne pour obtenir les sommes maximales pour toutes tailles possibles
            s = calc(L, u, 0)
            # On met à jour le tableau dp pour toutes tailles possibles filtrées par L
            for i in range(N-L, -1, -1):
                for j in range(1, L+1):
                    dp[i+j] = max(dp[i+j], dp[i] + s[j])
    # Deuxième passage : pour les cycles restants non traités
    for i in range(N):
        if used[i]:
            continue
        r = []  # Indices parcourus dans ce cycle
        u = []  # Liste des coûts du cycle
        v = i   # Départ du parcours cyclique
        while 1:
            r.append(v)
            used[v] = 3  # On marque v comme traité dans un cycle
            w1, w2 = G[v]  # Les deux voisins de v
            # Si les deux voisins ont déjà été traités, on a bouclé le cycle
            if used[w1[0]] and used[w2[0]]:
                break
            # On progresse vers le voisin non traité
            if used[w1[0]]:
                v, c = w2
                u.append(c)
            else:
                v, c = w1
                u.append(c)
        # On trouve la valeur de la dernière arête pour compléter le cycle de i à r[-1]
        if G[i][0][0] == r[-1]:
            c = G[i][0][1]
        else:
            c = G[i][1][1]
        u = [c] + u
        L = len(r)  # Longueur du cycle
        s = calc(L, u, 1)  # On calcule les sommes maximales possibles sur ce cycle
        for i in range(N-L, -1, -1):
            for j in range(1, L+1):
                dp[i+j] = max(dp[i+j], dp[i] + s[j])
    # En sortie, si la meilleure valeur pour exactement K sommets est très négative, c'est impossible
    if dp[K] < -10**9:
        write("Impossible\n")
    else:
        write("%d\n" % dp[K])  # Sinon, on affiche la somme maximale possible
solve()  # On exécute la fonction principale