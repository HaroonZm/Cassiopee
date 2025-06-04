from statistics import mean

def get_scores(num_scores=5):
    """
    Demande à l'utilisateur de saisir un nombre spécifié de scores entiers.

    Args:
        num_scores (int): Le nombre de scores à demander à l'utilisateur.

    Returns:
        list: Une liste contenant les scores saisis sous forme d'entiers.
    """
    scores = []
    for i in range(num_scores):
        score = int(input("Entrez le score #{}: ".format(i + 1)))
        scores.append(score)
    return scores

def adjust_scores(scores, minimum=40):
    """
    Ajuste les scores pour garantir qu'aucun score n'est inférieur à une valeur minimale.

    Args:
        scores (list): Liste des scores à ajuster.
        minimum (int): La valeur minimale autorisée pour un score.

    Returns:
        list: Une nouvelle liste des scores ajustés.
    """
    adjusted = list(map(lambda x: max(minimum, x), scores))
    return adjusted

def calculate_mean(scores):
    """
    Calcule la moyenne arithmétique des scores fournis.

    Args:
        scores (list): Liste des scores numériques.

    Returns:
        float: La moyenne des scores.
    """
    return mean(scores)

def main():
    """
    Fonction principale orchestrant la saisie, l'ajustement des scores,
    puis l'affichage de la moyenne des scores.
    """
    # Étape 1: Obtenir les scores de l'utilisateur
    scores = get_scores()
    
    # Étape 2: Ajuster les scores pour appliquer le minimum requis
    adjusted_scores = adjust_scores(scores)
    
    # Étape 3: Calculer et afficher la moyenne des scores ajustés
    average = calculate_mean(adjusted_scores)
    print("La moyenne des scores ajustés est:", average)

if __name__ == "__main__":
    main()