def calculate_score():
    """
    Calcule un score total basé sur deux groupes de nombres entiers fournis par l'utilisateur.

    Le calcul se fait en deux étapes :
    1. Lire 4 entiers, trier ces entiers, exclure le plus petit et sommer les trois autres.
    2. Lire 2 entiers et récupérer le maximum entre eux.

    Le résultat final est la somme du total de la première étape et du maximum de la deuxième étape.

    Retour:
        int: Le score calculé selon la méthode décrite.
    """
    # Lire 4 entiers et les stocker dans une liste via une compréhension
    scores = [int(input()) for _ in range(4)]
    # Trier la liste pour identifier le plus petit score facilement
    scores_sorted = sorted(scores)
    # Somme des trois plus grands scores (on ignore le plus petit)
    sum_top_three = sum(scores_sorted[1:])
    
    # Lire 2 entiers pour la seconde phase
    extra_scores = [int(input()) for _ in range(2)]
    # Trouver le maximum des deux scores
    max_extra = max(extra_scores)
    
    # Retourner la somme du total des trois meilleurs scores et du maximum des deux scores
    return sum_top_three + max_extra

# Affichage du résultat final calculé par la fonction
print(calculate_score())