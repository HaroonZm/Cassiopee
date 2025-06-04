def compute_total_score():
    """
    Demande à l'utilisateur de saisir 5 entiers, puis, pour chacun :
    - Prend la valeur maximale entre 40 et l'entier saisi,
    - Divise cette valeur par 5 en arrondissant à l'entier inférieur (division entière),
    - Additionne le résultat à un total.
    Affiche le total final à la fin du traitement.
    """
    # Initialisation du score total à 0
    total_score = 0

    # Boucle pour traiter 5 entrées utilisateur
    for i in range(5):
        # Demande à l'utilisateur de saisir un entier
        user_input = int(input("Entrez un score (entier) : "))
        # Prend le maximum entre 40 et la valeur saisie
        adjusted_score = max(40, user_input)
        # Divise le score ajusté par 5 (division entière)
        score_divided = adjusted_score // 5
        # Ajoute le résultat au score total
        total_score += score_divided

    # Affiche le score total final
    print(total_score)

# Exécution de la fonction principale
compute_total_score()