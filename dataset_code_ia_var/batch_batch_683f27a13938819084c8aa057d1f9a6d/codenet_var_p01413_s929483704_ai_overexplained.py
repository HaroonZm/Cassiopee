import sys  # Importation du module système pour la gestion des flux d'entrée/sortie et d'autres paramètres système
readline = sys.stdin.readline  # Raccourci pour lire une ligne depuis l'entrée standard (console ou redirection)
write = sys.stdout.write  # Raccourci pour écrire dans la sortie standard (typiquement la console)

def solve():
    # Lecture de 4 entiers sur une ligne représentant N (nombre de lieux), M (nombre d'objets),
    # W (capacité max de poids), T (limite de temps total)
    N, M, W, T = map(int, readline().split())
    
    # Initialisation d'une variable d'état (ici non utilisée dans la suite du code)
    cur = 0
    
    # Création d'un dictionnaire pour faire correspondre chaque nom d'objet à un index unique
    n_map = {}
    
    # Initialisation des listes de tailles pour stocker le poids (ws) et la valeur par défaut (P) de chaque objet
    ws = [0]*M          # Liste pour les poids des objets (indexée de 0 à M-1)
    P = [0]*M           # Liste pour les valeurs par défaut des objets (indexée de 0 à M-1)
    
    # Boucle pour la lecture des données des objets
    for i in range(M):
        # Lecture de la ligne et découpage en trois valeurs : nom de l'objet (s), poids (v), valeur par défaut (p)
        s, v, p = readline().split()
        n_map[s] = i         # Association du nom (clé) avec l'index (valeur) dans le dictionnaire
        ws[i] = int(v)       # Conversion en entier et stockage du poids de l'objet à l'index correspondant
        P[i] = int(p)        # Conversion en entier et stockage de la valeur par défaut pour l'objet

    # Initialisation de la liste des tâches/bonus à chaque lieu
    ts = [[] for i in range(N)]     # Chaque lieu (de 0 à N-1) aura une liste de tuples (index d'objet, gain)
    X = [0]*N                      # Coordonnées X initialisées pour tous les lieux
    Y = [0]*N                      # Coordonnées Y initialisées pour tous les lieux
    
    # Lecture des données des lieux
    for i in range(N):
        # Lecture de la première ligne avec l, x, y : l = nombre de tâches locales, x/y = coordonnées du lieu
        l, x, y = map(int, readline().split())
        X[i] = x        # Stockage de la coordonnée X du lieu i
        Y[i] = y        # Stockage de la coordonnée Y du lieu i
        r = 0           # Variable utilisée temporairement lors de l'analyse des tâches
        t = ts[i]       # Référence abrégée vers la liste des tâches du lieu i
        # Lecture des l tâches pour ce lieu
        for j in range(l):
            r, q = readline().split()  # Lecture du nom de l'objet et du gain local possible
            q = int(q)                 # Conversion du gain en entier
            k = n_map[r]               # Récupération de l'index de l'objet depuis le dictionnaire
            if P[k] <= q:              # Si la valeur par défaut <= gain local, il n'y a rien à gagner ici
                continue               # On saute cette tâche car elle n'apporte aucun surplus
            t.append((k, P[k] - q))    # On ajoute le tuple (index objet, gain réel) dans la liste des tâches

    # Calcul des distances entre tous les lieux (matrice E), et depuis l'origine (E1)
    E = [[0]*N for i in range(N)]   # Matrice NxN pour les distances entre chaque paire de lieux
    E1 = [0]*N                     # Liste Nx1 pour la distance de chaque lieu à l'origine (0,0)
    for i in range(N):
        for j in range(i):     # Boucle sur toutes les paires sans répétition (matrice symétrique)
            # Calcul de la distance de Manhattan entre les lieux i et j
            E[i][j] = E[j][i] = abs(X[i] - X[j]) + abs(Y[i] - Y[j])
        # Calcul de la distance depuis l'origine jusqu'au lieu i
        E1[i] = abs(X[i]) + abs(Y[i])
    
    INF = 10**18      # Une valeur très grande utilisée pour l'initialisation
    SN = 1 << N       # SN = 2^N, nombre total de sous-ensembles possibles des lieux (codés en binaire)
    
    # D0[s][i] : coût minimal pour visiter tous les lieux de s et finir en i
    D0 = [[0]*N for i in range(SN)]    # Matrice 2D de taille (2^N) x N, initialisée à 0
    
    dp1 = [0]*(T+1)   # dp1[i] = gain maximal possible en ayant utilisé i unités de temps (de 0 à T)
    
    # Parcours de tous les sous-ensembles possibles de lieux (hors l'ensemble vide)
    for s in range(1, SN):
        d1 = INF   # Initialisation du coût minimal pour ce sous-ensemble à l'infini
        # On considère chaque lieu comme possible "dernier" visité dans l'ensemble s
        for i in range(N):
            bi = (1 << i)       # Correspond au bit d'i dans le sous-ensemble
            r = INF             # Initialisation de la valeur temporaire pour ce lieu
            if s & bi:          # Si le lieu i fait partie du sous-ensemble s
                si = s ^ bi     # Enlève le lieu i du sous-ensemble courant
                if si == 0:     # Si si est l'ensemble vide, on part de l'origine vers i
                    r = E1[i]
                else:           # Sinon, on cherche tous les j précédents pour la meilleure route
                    for j in range(N):
                        if i == j or s & (1 << j) == 0:
                            continue     # Ne considère que les lieux j différents de i présents dans s
                        r = min(r, D0[si][j] + E[j][i])  # Mise à jour du coût minimal
            D0[s][i] = r       # Stocke le coût minimal pour finir à i après avoir visité tous les lieux de s
            d1 = min(d1, r + E1[i])   # Mise à jour du coût minimal pour faire l'aller-retour
    
        # Calcul du gain maximal obtainable avec ce sous-ensemble de lieux
        vs = [-1]*M    # Initialisation : pour chaque objet, le gain maximal constaté dans ces lieux (valeur -1 = pas présent)
        for i in range(N):
            if s & (1 << i):    # Si le lieu i est bien visité dans ce sous-ensemble
                for k, d in ts[i]:   # On regarde chaque tâche pour ce lieu
                    vs[k] = max(vs[k], d)  # Mise à jour du gain maximal observé pour l'objet k

        # Problème du sac à dos (knapsack) pour choisir au mieux les objets à rapporter
        dp0 = [0]*(W+1)   # dp0[i] = gain max possible pour un poids total de i
        for i in range(M):
            if vs[i] == -1:
                continue  # Si l'objet i n'est pas gagné dans les lieux visités, on passe
            w = ws[i]     # Poids de l'objet i
            v = vs[i]     # Gain obtenu pour l'objet i dans ce sous-ensemble
            # Parcours des poids possibles, mise à jour du tableau dynamique (knapsack 0/1)
            for j in range(W-w+1):
                # Soit on prend l'objet i (on ajoute son gain v au total pour le sac de capacité j + w)
                # Soit on garde le gain précédent si c'est mieux (pas de duplicate d'objet)
                dp0[j + w] = max(dp0[j] + v, dp0[j + w])
        v1 = max(dp0)   # Le gain maximal atteignable avec le choix d'objets optimal sur ce sous-ensemble

        # Mise à jour de la réponse globale avec la borne de temps : on ne peut pas dépasser T
        for j in range(T-d1+1):    # Pour chaque durée possible restante (de 0 à T-d1 incl.)
            dp1[j + d1] = max(dp1[j] + v1, dp1[j + d1]) # MAJ du gain max pour cette durée totale

    # Affichage du résultat final : le plus grand gain sur toutes bornes de temps possibles
    write("%d\n" % max(dp1))

# Appel de la fonction principale pour démarrer le processus
solve()