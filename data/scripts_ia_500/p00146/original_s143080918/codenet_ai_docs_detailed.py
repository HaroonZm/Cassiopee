def calctime(w, dist):
    """
    Calcule le temps nécessaire pour parcourir une certaine distance avec une vitesse dépendant d'un poids.

    Args:
        w (float): Poids ou charge cumulée actuelle.
        dist (float): Distance à parcourir.

    Returns:
        float: Temps nécessaire pour parcourir la distance donnée avec le poids spécifié.
    
    La vitesse est calculée comme 2000/(70 + w). Le temps est donc distance / vitesse.
    """
    time = dist / (2000 / (70.0 + w))
    return time


def solve():
    """
    Résout le problème d'optimisation de chemin en tenant compte des poids cumulés qui influencent la vitesse.

    Returns:
        list: La séquence optimale des identifiants (variables `s`) représentant l'ordre du parcours.
    
    La fonction utilise un algorithme dynamique avec bitmask pour explorer toutes les combinaisons de visites possibles.
    Elle calcule les temps minimaux pour chaque sous-ensemble de points visités en tenant compte du poids cumulatif.
    """
    # Initialisation de la matrice des distances entre les points : taille n x n
    dist = [[None] * n for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            if i == j:
                # La distance d'un point à lui-même est considérée infinie (pas de déplacement)
                dist[i][j] = float('inf')
            else:
                # Distance absolue entre deux points d selon leurs positions
                dist[i][j] = abs(d[i] - d[j])

    # w[i] représentera le poids total (somme pondérée) associé à la sous-séquence avec masque i
    w = [float('inf')] * (1 << n)
    # time[i][j] représente le temps minimal pour visiter les points du sous-ensemble i et finir au point j
    time = [[float('inf')] * n for _ in xrange(1 << n)]
    # last[i][j] stocke le dernier point visité avant j dans la sous-séquence i
    last = [[0] * n for _ in xrange(1 << n)]

    # Initialisation des cas de base : visiter un seul point
    for i in xrange(n):
        # Le temps pour visiter uniquement le point i est 0 (on commence sur ce point)
        time[1 << i][i] = 0
        # Le poids total pour le sous-ensemble contenant uniquement i est v[i] * 20
        w[1 << i] = v[i] * 20

    # Parcours de tous les sous-ensembles de points
    for i in xrange(1, 1 << n):
        for j in xrange(n):
            # Si le poids de ce sous-ensemble est infini, cela signifie que l'ensemble n'a pas été atteint
            if w[i] == float('inf'):
                continue
            # Si le point j est le dernier visité dans i (sinon time[i][j] serait inf)
            if time[i][j] == float('inf'):
                continue
            for k in xrange(n):
                # On regarde un point k pas encore visité dans i
                if not (i >> k) & 1:
                    nexti = i | (1 << k)  # Sous-ensemble après avoir ajouté k
                    # Calcul du poids total après ajout du point k
                    new_w = w[i] + v[k] * 20
                    # Calcul du temps pour aller de j à k avec le poids w[i]
                    travel_time = calctime(w[i], dist[j][k])
                    # Calcul du temps total pour parcourir nexti en terminant par k
                    total_time = time[i][j] + travel_time
                    # Mise à jour si on a trouvé un temps plus court
                    if total_time < time[nexti][k]:
                        time[nexti][k] = total_time
                        w[nexti] = new_w  # Mise à jour poids
                        last[nexti][k] = j  # Stockage du point précédent

    # Reconstruction de la séquence optimale
    ans = []
    now = (1 << n) - 1  # Masque complet (tous les points visités)
    # Trouve le point final avec le temps minimal
    last_index = time[now].index(min(time[now]))
    while now != 0:
        ans.append(s[last_index])  # Ajoute le point courant à la solution
        nx = last[now][last_index]  # Point précédent
        now = now ^ (1 << last_index)  # Retire last_index de l'ensemble actuel
        last_index = nx  # Passe au point précédent
    ans.reverse()  # Inverse la liste pour avoir l'ordre correct
    return ans


# Lecture du nombre de points
n = int(raw_input())
# Dictionnaires pour stocker les identifiants, positions et poids des points
s = {}
d = {}
v = {}

# Lecture des données pour chaque point
for i in xrange(n):
    S, D, V = map(int, raw_input().split())
    s[i] = S  # Identifiant du point
    d[i] = D  # Position (distance)
    v[i] = V  # Poids associé

# Calcul et affichage de la séquence optimale
ans = solve()
print(' '.join(map(str, ans)))