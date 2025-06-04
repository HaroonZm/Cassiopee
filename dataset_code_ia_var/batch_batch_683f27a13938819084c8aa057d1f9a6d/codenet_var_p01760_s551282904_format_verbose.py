# Lecture des données d'entrée avec des noms explicites
target_temperature, maximum_volume = map(int, input().split())
temperature_option_a, temperature_option_b = map(int, input().split())
volume_increment_a, volume_increment_b = map(int, input().split())

# Liste pour stocker toutes les différences absolues possibles
absolute_temperature_differences = []

# Parcours de tous les volumes possibles pour l'option A
for total_volume_a in range(0, maximum_volume + 1, volume_increment_a):

    # Parcours de tous les volumes possibles pour l'option B
    for total_volume_b in range(0, maximum_volume + 1, volume_increment_b):

        combined_volume = total_volume_a + total_volume_b

        # Vérification des contraintes de volume (doit être entre 1 et maximum_volume)
        if 1 <= combined_volume <= maximum_volume:

            # Calcul de la température moyenne pour cette combinaison de volumes
            average_temperature = (
                temperature_option_a * total_volume_a + temperature_option_b * total_volume_b
            ) / combined_volume

            # Calcul de la différence absolue entre cible et moyenne
            absolute_difference = abs(target_temperature - average_temperature)

            # Stockage de la différence
            absolute_temperature_differences.append(absolute_difference)

# Récupération de la différence absolue minimale
minimum_absolute_difference = min(absolute_temperature_differences)

print(minimum_absolute_difference)