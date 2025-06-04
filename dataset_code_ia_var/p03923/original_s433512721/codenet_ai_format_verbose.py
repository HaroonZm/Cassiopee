# Lecture des entrées utilisateur pour obtenir le nombre de produits et le temps d'une action
total_cakes, base_action_time = map(int, raw_input().split())

# Initialisation de la meilleure durée trouvée avec une très grande valeur
minimum_total_time = 10**12 + 5

# Parcours du nombre de fois où l'on "mange" (max 45, arbitrairement suffisant)
for number_of_eaten_cakes in xrange(45):

    # Si l'étape suivante dépasse le nombre total de gâteaux, on arrête la recherche
    if 2 ** (number_of_eaten_cakes - 1) > total_cakes:
        break

    # Temps pour effectuer le nombre de consommations de gâteaux
    current_total_time = number_of_eaten_cakes * base_action_time

    # Nombre d'opérations de "cuisson" requis
    number_of_bake_operations = number_of_eaten_cakes + 1

    # Recherche binaire pour déterminer le nombre minimum possible de gâteaux cuits à chaque fois
    lower_bound_cakes_per_bake = 0
    upper_bound_cakes_per_bake = total_cakes

    while upper_bound_cakes_per_bake - lower_bound_cakes_per_bake > 1:
        middle_cakes_per_bake = (upper_bound_cakes_per_bake + lower_bound_cakes_per_bake) // 2
        if middle_cakes_per_bake ** number_of_bake_operations >= total_cakes:
            upper_bound_cakes_per_bake = middle_cakes_per_bake
        else:
            lower_bound_cakes_per_bake = middle_cakes_per_bake

    # Recherche du nombre minimal d'étapes où il faut diminuer de 1 les gâteaux par fournée tout en restant suffisant
    surplus_actions = 0
    for possible_surplus in xrange(1, number_of_bake_operations + 1):
        if (upper_bound_cakes_per_bake ** (number_of_bake_operations - possible_surplus) *
            (upper_bound_cakes_per_bake - 1) ** possible_surplus) < total_cakes:
            break
        surplus_actions = possible_surplus

    # Calcul du temps total avec la stratégie trouvée
    current_total_time += upper_bound_cakes_per_bake * (number_of_bake_operations - surplus_actions)
    current_total_time += (upper_bound_cakes_per_bake - 1) * surplus_actions

    # Mise à jour du meilleur temps trouvé
    if current_total_time < minimum_total_time:
        minimum_total_time = current_total_time

# Affichage du résultat final
print minimum_total_time