def calculate_score(h1, h2, a, b, c, d):
    """
    Calcule le score total pour un joueur donné en fonction de ses paramètres.

    Args:
        h1 (int): Première statistique du joueur (unité non spécifiée).
        h2 (int): Deuxième statistique du joueur (unité non spécifiée).
        a (int): Coefficient pondérant la première statistique.
        b (int): Coefficient pondérant la deuxième statistique.
        c (int): Coefficient pondérant les groupes de 10 unités dans h1.
        d (int): Coefficient pondérant les groupes de 20 unités dans h2.

    Returns:
        int: Le score total calculé pour le joueur.
    """
    # Calcul du score en combinant les différentes statistiques avec leurs coefficients respectifs
    score = a * h1         # Contribution linéaire de la première statistique
    score += c * (h1 // 10) # Contribution des groupes de 10 unités dans h1
    score += b * h2         # Contribution linéaire de la deuxième statistique
    score += d * (h2 // 20) # Contribution des groupes de 20 unités dans h2
    return score

# Lecture de la première paire de statistiques (h1, h2) pour le premier joueur
h1, h2 = [int(i) for i in input().split()]

# Lecture de la deuxième paire de statistiques (k1, k2) pour le deuxième joueur
k1, k2 = [int(i) for i in input().split()]

# Lecture des coefficients a, b, c, d 
a, b, c, d = [int(i) for i in input().split()]

# Calcul des scores pour chaque joueur en utilisant la fonction définie
p1 = calculate_score(h1, h2, a, b, c, d)
p2 = calculate_score(k1, k2, a, b, c, d)

# Comparaison des scores et affichage du résultat approprié
if p1 > p2:
    print("hiroshi")
elif p1 < p2:
    print("kenjiro")
else:
    print("even")