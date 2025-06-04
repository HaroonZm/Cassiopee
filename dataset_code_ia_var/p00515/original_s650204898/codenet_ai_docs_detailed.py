def get_input_scores(num_scores):
    """
    Demande à l'utilisateur de saisir un nombre donné de scores, assure que chaque score
    est au moins de 40, et renvoie la liste de tous les scores corrigés.

    Args:
        num_scores (int): Le nombre de scores à saisir.

    Returns:
        list: Liste des scores corrigés (au moins 40 chacun).
    """
    scores = []  # Liste pour stocker les scores corrigés
    for i in range(num_scores):
        user_input = int(input())  # Lire l'entrée utilisateur et la convertir en entier
        # Vérifier si le score est inférieur à 40
        if user_input < 40:
            user_input = 40  # Remplacer tout score < 40 par 40
        scores.append(user_input)  # Ajouter le score corrigé à la liste
    return scores

def compute_average(scores):
    """
    Calcule la moyenne entière des scores présents dans une liste.

    Args:
        scores (list): Liste des entiers représentant des scores.

    Returns:
        int: La moyenne entière (troncature) des scores.
    """
    total = sum(scores)  # Calculer la somme totale des scores
    count = len(scores)  # Compter le nombre total de scores
    average = total // count  # Calculer la moyenne entière
    return average

def main():
    """
    Fonction principale du programme.
    Lit cinq scores, les corrige à 40 si nécessaire, et affiche leur moyenne entière.
    """
    num_scores = 5  # Nombre de scores à recueillir
    # Récupérer et corriger les scores de l'utilisateur
    scores = get_input_scores(num_scores)
    # Calculer la moyenne entière des scores corrigés
    avg_score = compute_average(scores)
    print(avg_score)  # Afficher la moyenne entière

# Appel de la fonction principale pour lancer le programme
main()