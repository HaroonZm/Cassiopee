import sys

def gcd(m, n):
    """
    Calcule le plus grand commun diviseur (PGCD) de deux entiers m et n
    en utilisant l'algorithme d'Euclide.
    
    Args:
        m (int): Premier entier.
        n (int): Deuxième entier.
    
    Returns:
        int: Le PGCD de m et n.
    """
    while n:
        m, n = n, m % n
    return m

# Shorthands pour lecture et écriture plus rapides sur les flux standard
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    """
    Résout un cas du problème suivant :
    À partir d'une heure H et d'un temps (h, m, s), calcule une configuration satisfaisant
    certaines contraintes arithmétiques spécifiques. Affiche la solution trouvée au format
    demandé. Arrête la résolution si H vaut 0.
    
    Returns:
        bool: True si une résolution a eu lieu (H != 0), False sinon (fin du programme).
    """
    # Fonction pour convertir heures, minutes, secondes en secondes
    f = lambda h, m, s: 3600 * h + 60 * m + s

    # Lecture de l'entrée : H = heures max, h = heure de départ, m = minutes, s = secondes
    H, h, m, s = map(int, readline().split())
    if H == 0:
        return False  # Condition d'arrêt

    # Conversion du temps fourni en secondes
    d0 = f(h, m, s)
    # Nombre total de secondes dans H heures
    M = f(H, 0, 0)
    res = []

    # Double boucle sur chaque possibilité d'heure et de minute jusqu'à H heures pleines
    for h0 in range(H):
        for m0 in range(60):
            # Calcul d'une expression particulière pour la fraction
            p = 3600 * h0 + 60 * m0 + 60 * H * m0
            q = 119 * H - 1  # Dénominateur de la fraction

            # Exploration de petites corrections autour de p pour couvrir tous les cas
            for d in [-3600 * H, 0, 3600 * H]:
                p1 = p + d
                q1 = q

                # Simplification de la fraction (p1/q1)
                g = gcd(p1, q)
                p1 //= g
                q1 //= g

                # Vérifie que la fraction résultante est dans les bornes imposées
                if 0 <= p1 < 60 * q1:
                    # Vérifie la condition spécifique du problème sur les coefficients
                    if H * (60 * m0 * q1 + p1) != q1 * (3600 * h0 + 60 * m0) + p1:
                        # Enregistre la solution candidate avec sa valeur temporelle totale
                        res.append((f(h0, m0, 0) + p1 / q1, h0, m0, p1, q1))

    # Trie les résultats suivant l'ordre cyclique par rapport à d0 (valeur de départ)
    res.sort(key=lambda x: (x[0] - d0) % M)

    # Prend la première solution (la plus proche en temps du point de départ)
    _, h, m, p, q = res[0]
    # Écrit la solution sous la forme : heure minute numérateur dénominateur
    write("%d %d %d %d\n" % (h, m, p, q))

    return True

# Boucle principale : lit et traite une instance tant que solve() retourne True
while solve():
    ...