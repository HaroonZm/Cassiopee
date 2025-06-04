def read_date_inputs():
    """
    Lit deux entrées utilisateur représentant des dates sous forme de trois entiers (année, mois, jour),
    puis les retourne sous forme de liste de tuples (année, mois, jour).
    
    Returns:
        list of tuple: Liste de deux tuples contenant respectivement année, mois et jour pour chaque date.
    """
    dates = []
    for _ in range(2):
        # Lecture d'une ligne, séparation des entrées et conversion en entiers pour former un tuple
        date_tuple = tuple(map(int, input().split()))
        dates.append(date_tuple)
    return dates

def sort_dates(dates):
    """
    Trie deux dates pour que la première soit la plus ancienne (ou la plus petite).
    
    Args:
        dates (list of tuple): Liste de deux tuples représentant les dates (année, mois, jour).
    
    Returns:
        list of tuple: Liste triée des deux dates.
    """
    # sorted trie automatiquement selon l'ordre tuple (année, mois, jour)
    return sorted(dates)

def compute_year_difference(date1, date2):
    """
    Calcule la différence en années entre deux dates selon les règles du calendrier.
    On ajoute 1 à la différence d'années si la date2 n'est pas encore arrivée dans l'année courant (mois/jour).
    
    Args:
        date1 (tuple): (année, mois, jour) de la première date (la plus ancienne)
        date2 (tuple): (année, mois, jour) de la deuxième date (la plus récente)
    
    Returns:
        int: Différence en nombre d'années entre date1 et date2, ajustée selon les mois et jours.
    """
    year_diff = date2[0] - date1[0]
    # Si le mois de date2 est supérieur à celui de date1, alors une année complète s'est écoulée
    # Si le mois est égal, on regarde les jours
    if date2[1] > date1[1] or (date2[1] == date1[1] and date2[2] > date1[2]):
        year_diff += 1
    return year_diff

def main():
    """
    Fonction principale : lit deux dates, les trie, calcule et affiche la différence d'années selon la méthode spécifiée.
    """
    # Lecture des deux dates depuis l'entrée standard
    dates = read_date_inputs()
    # Trie des dates pour que la première soit la plus ancienne
    sorted_dates = sort_dates(dates)
    # Calcul de la différence d'années ajustée
    difference = compute_year_difference(sorted_dates[0], sorted_dates[1])
    # Affichage du résultat
    print(difference)

# Exécution du script principal
if __name__ == "__main__":
    main()