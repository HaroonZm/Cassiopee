# Début du programme principal

# Lire deux entiers à partir de l'entrée standard, séparés par un espace.
# map(int, input().split()) convertit chaque élément lu en entier puis les assigne à N et R.
N, R = map(int, input().split())

# Condition pour s'assurer que R ne dépasse pas la moitié de N.
# Si le double de R est strictement plus grand que N, alors on utilise la symétrie en remplaçant R par N-R.
if 2 * R > N:
    R = N - R

# Lire une permutation sous forme de liste d'entiers depuis l'entrée standard.
# On insère un 0 au début de la liste pour faciliter le 1-indexing (l'indice 1 correspond alors à l'élément 1).
# list(map(int, ...)) convertit chaque élément en entier.
P = [0] + list(map(int, input().split()))

# Initialisation d'une liste vide L qui contiendra les longueurs des cycles de la permutation.
L = []

# Pour une optimisation minime, on référence la méthode append de la liste L pour pouvoir l'appeler plus rapidement.
Lapp = L.append

# Création d'une liste 'used' de N+1 éléments (car on commence à 1), initialisés à False.
# Elle permet de marquer si un élément a déjà été parcouru dans un cycle.
used = [False] * (N + 1)

# Variable auxiliaire, inutilisée mais initialisée à 0 pour cohérence.
pre = 0

# Boucle sur chaque entier de 1 à N inclus.
for i in range(1, N + 1):
    # Compteur pour la taille du cycle démarrant à l'élément i.
    cnt = 0
    # On parcourt le cycle commençant à i jusqu'à tomber sur un élément déjà utilisé.
    while not used[i]:
        # Marquer l'élément i comme utilisé.
        used[i] = True
        # Incrémenter la taille du cycle.
        cnt += 1
        # Aller à l'élément correspondant à la prochaine position du cycle via la permutation.
        i = P[i]
    # Si un cycle a été détecté, on ajoute sa taille à la liste L.
    if cnt:
        Lapp(cnt)

# Création d'une table 'table' permettant de compter combien il y a de cycles de chaque taille.
# (N+1 éléments car des cycles peuvent, en théorie, avoir une taille jusqu'à N)
table = [0] * (N + 1)

# Boucle sur chaque cycle détecté pour compter le nombre d'occurrences de chaque taille de cycle.
for l in L:
    table[l] += 1

# Réinitialisation de la liste L pour stocker certains résultats intermédiaires.
L = []
# Réaffectation de la méthode append après réinitialisation de la liste.
Lapp = L.append

# Boucle sur les tailles possibles de cycles de 1 à min(R, N//2) inclus.
# Cette limite permet d'éviter des calculs inutiles pour de grands i incompatibles avec R.
for i in range(1, min(R, N // 2) + 1):
    # Nombre de cycles de taille i.
    x = table[i]
    # Si aucun cycle de cette taille n'est présent, on passe à la taille suivante.
    if not x:
        continue
    # S'il n'y en a qu'un, on ajoute la taille à la liste L.
    if x == 1:
        Lapp(i)
    else:
        # On ajoute une copie initiale de la taille i.
        Lapp(i)
        # Variable de puissance, commence à 2 (pour 2 cycles, 4, 8 etc).
        p = 2
        # Boucle tant que p multiplié par la taille d’un cycle ne dépasse pas le nombre de cycles.
        while 2 * p <= x:
            # On incrémente le nombre de cycles présents à l'indice correspondant à p fois i.
            table[p * i] += 1
            # On double p à chaque itération (puissances de 2 typique d’une décomposition binaire).
            p *= 2
        # Si le nombre initial de cycles x est exactement la dernière valeur de p,
        # on ajoute encore une fois la taille i à la liste L.
        if x == p:
            Lapp(i)
        # Enfin, pour les cycles restants (x - p + 1), on les ajoute au tableau à l’emplacement approprié.
        table[i * (x - p + 1)] += 1

# Initialisation d'un entier H valant 1 (bitmask dynamique pour le "subset sum").
H = 1

# Boucle sur chaque élément de L pour faire la convolution bitwise des sommes réalisables.
for l in L:
    # H | (H << l) permet de générer tous les sous-ensembles de taille l en ajoutant cette taille à chaque somme possible.
    H = H | (H << l)

# Si le bit à la position R de H est à 1, alors la somme R est réalisable avec les tailles de cycle trouvées.
if H & (1 << R):
    print('Yes')
# Sinon, ce n'est pas possible.
else:
    print('No')