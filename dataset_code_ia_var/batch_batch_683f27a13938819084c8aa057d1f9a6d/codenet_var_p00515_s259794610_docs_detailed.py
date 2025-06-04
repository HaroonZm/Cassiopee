def calculate_average_with_min_score():
    """
    Demande à l'utilisateur de saisir 5 notes, impose une note minimale de 40 pour chacune si nécessaire,
    puis calcule et affiche la moyenne de ces notes (moyenne entière par division entière).
    """
    total_score = 0  # Initialisation de la variable qui contiendra la somme des notes

    # Boucle pour demander 5 fois une note à l'utilisateur
    for i in range(5):
        score = int(input("Entrez la note n°{}: ".format(i + 1)))  # Saisie de la note par l'utilisateur
        
        # Si la note est inférieure à 40, on la remplace par 40
        if score < 40:
            score = 40

        total_score += score  # Ajout de la note (ou de 40) à la somme totale

    # Calcul de la moyenne avec division entière (le '//' retourne la partie entière)
    average_score = total_score // 5

    # Affichage du résultat final
    print(average_score)

# Appel de la fonction principale
calculate_average_with_min_score()