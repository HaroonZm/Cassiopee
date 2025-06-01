# Boucle infinie qui continuera à s'exécuter jusqu'à rencontre d'une condition d'arrêt explicite  
while True:
    # Lecture de l'entrée utilisateur sous forme de chaîne de caractères et conversion en entier
    n = input()
    # Condition de sortie de la boucle: si n vaut zéro, on arrête le programme
    if n == 0: 
        break

    # Initialisation d'une liste P contenant n tuples (x, y), chacun lu depuis l'entrée standard
    # raw_input() lit une ligne de texte entrée par l'utilisateur (Python 2)
    # split() décompose cette ligne en éléments séparés par des espaces (par défaut)
    # map(int, ...) convertit chaque élément en entier
    # La liste compréhensive crée une liste de n tuples, chacun représentant un point 2D
    P = [(map(int, raw_input().split())) for i in range(n)]

    # Conversion de la liste des points P en un set de tuples pour un accès plus rapide (recherche en temps quasi-constant)
    # set(...) crée un ensemble, map(tuple, P) convertit chaque élément (probablement une liste) de P en un tuple pour être hashable
    S = set(map(tuple, P))

    # Initialisation d'une variable qui gardera la plus grande valeur trouvée (ici un carré de longueur)
    ans = 0

    # Deux boucles imbriquées pour examiner chaque paire distincte de points dans P
    # i varie de 0 à n-2 inclus
    for i in range(n - 1):
        # Récupération des coordonnées x et y du point d'indice i
        xi, yi = P[i]
        # j commence à i+1 pour éviter de comparer un point avec lui-même ou de revérifier des paires déjà vues
        for j in range(i + 1, n):
            # Récupération des coordonnées x et y du point d'indice j
            xj, yj = P[j]

            # Calcul du point q selon une formule géométrique spécifique (probablement pour vérifier la présence d'un carré)
            # Les coordonnées de q sont calculées par transformation linéaire des coordonnées de xi, yi, xj, yj
            q = (xj - yj + yi, yj + xj - xi)

            # Calcul du point r selon une autre formule géométrique liée à q et aux points i et j
            r = (xi - yj + yi, yi + xj - xi)

            # Vérification si les deux points q et r sont présents dans l'ensemble S
            # Cela signifie que les points formant un carré sont tous dans l'ensemble donné
            if q in S and r in S:
                # Calcul de la distance au carré entre les points i et j
                distance_carre = (xi - xj) ** 2 + (yi - yj) ** 2

                # Mise à jour de ans si cette distance est supérieure à la valeur actuelle
                ans = max(ans, distance_carre)

    # Affichage du résultat final: la plus grande distance au carré trouvée correspondant probablement au côté le plus long d'un carré formé par 4 points
    print ans