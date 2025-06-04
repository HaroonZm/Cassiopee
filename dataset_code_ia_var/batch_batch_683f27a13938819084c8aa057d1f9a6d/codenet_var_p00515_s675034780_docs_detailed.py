def get_modified_scores(num_scores=5, min_score=40):
    """
    Demande à l'utilisateur d'entrer un certain nombre de scores, ajuste chaque score
    si nécessaire pour qu'il ne soit pas inférieur à un score minimal, puis renvoie la liste des scores ajustés.

    Args:
        num_scores (int): Le nombre de scores à demander à l'utilisateur. Défaut à 5.
        min_score (int): Le score minimal à accepter, toute valeur inférieure sera relevée à celui-ci. Défaut à 40.

    Returns:
        list: La liste des scores ajustés (chaque élément >= min_score).
    """
    scores = []  # Liste pour stocker les scores ajustés
    for i in range(num_scores):
        # Lecture d'une entrée utilisateur et conversion en entier
        a = int(input())
        # Si le score est inférieur au minimum, il est relevé au minimum
        if a < min_score:
            a = min_score
        # Ajout du score ajusté à la liste des scores
        scores.append(a)
    return scores

def calculate_average(scores):
    """
    Calcule la moyenne entière des scores passés en argument.

    Args:
        scores (list): Une liste de scores (entiers) à partir desquels la moyenne sera calculée.

    Returns:
        int: La moyenne entière des scores (somme divisée par le nombre d'éléments, division entière).
    """
    total = sum(scores)  # Somme des scores
    count = len(scores)  # Nombre total de scores
    # Calcul de la moyenne entière (division entière)
    return total // count

# Programme principal
if __name__ == "__main__":
    # Obtention des scores ajustés depuis l'utilisateur
    scores_list = get_modified_scores()
    # Calcul et affichage de la moyenne entière des scores
    print(calculate_average(scores_list))