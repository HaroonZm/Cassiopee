import bisect

def get_rank_from_scores(n, m):
    """
    Détermine le rang académique basé sur deux scores fournis.

    Args:
        n (float): Premier score à comparer avec la liste m500.
        m (float): Deuxième score à comparer avec la liste m1000.

    Returns:
        str: Le rang correspondant sous forme de chaîne de caractères.
             Possible valeurs: "AAA", "AA", "A", "B", "C", "D", "E", "NA".
    """
    # Seuils des catégories pour le premier score (niveau 500)
    m500 = [35.5, 37.5, 40, 43, 50, 55, 70]
    # Seuils des catégories pour le deuxième score (niveau 1000)
    m1000 = [71, 77, 83, 89, 105, 116, 148]

    # Recherche de l'indice de rang où placer n dans m500 (ajout de 0.001 pour contourner les égalités)
    r1 = bisect.bisect_left(m500, n + 0.001)
    # Recherche de l'indice de rang où placer m dans m1000 (idem)
    r2 = bisect.bisect_left(m1000, m + 0.001)

    # Définition des rangs possibles
    rank = ["AAA", "AA", "A", "B", "C", "D", "E", "NA"]

    # Le rang final est le plus faible rang obtenu entre les deux scores (indice maximum)
    final_rank = rank[max(r1, r2)]
    return final_rank

def main():
    """
    Fonction principale qui lit en continu des paires de scores depuis l'entrée standard,
    calcule et affiche leur rang académique jusqu'à interruption (EOF ou erreur).
    """
    while True:
        try:
            # Lecture d'une ligne d'entrée, séparée par un espace en deux nombres float
            line = input()
            if not line:
                # Si la ligne est vide, on quitte la boucle
                break
            n, m = map(float, line.split())
            
            # Calcul du rang selon les deux scores
            result = get_rank_from_scores(n, m)

            # Affichage du rang obtenu
            print(result)
        except Exception:
            # Arrêt de la boucle pour toute erreur de saisie ou fin d'entrée
            break

if __name__ == "__main__":
    main()