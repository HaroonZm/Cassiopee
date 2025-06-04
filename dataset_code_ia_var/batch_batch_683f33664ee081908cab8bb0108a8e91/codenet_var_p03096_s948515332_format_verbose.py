def count_distinct_color_arrangements():
    # Lire le nombre de positions à traiter
    total_positions = int(input())
    
    # Lire la couleur à chaque position
    input_colors = [int(input()) for _ in range(total_positions)]
    
    MODULO_BASE = int(1e9) + 7

    # Construction de la liste sans couleurs consécutives identiques
    unique_colors = set()
    non_consecutive_colors = [-1]  # Sécurité pour le premier élément
    for current_color in input_colors:
        unique_colors.add(current_color)
        if current_color == non_consecutive_colors[-1]:
            continue
        non_consecutive_colors.append(current_color)

    # Supprimer le premier élément de la liste de travail
    del non_consecutive_colors[0]

    count_non_consecutive = len(non_consecutive_colors)
    count_distinct_colors = len(unique_colors)

    # Pour chaque position, mémoriser où la même couleur a déjà été vue pour la dernière fois
    last_occurrence_of_color = [-1] * count_non_consecutive
    color_to_last_index = [-1] * (2 * 10**5 + 1)

    for current_index, color_value in enumerate(non_consecutive_colors):
        if color_to_last_index[color_value] == -1:
            # Première apparition de cette couleur
            color_to_last_index[color_value] = current_index
        else:
            last_occurrence_of_color[current_index] = color_to_last_index[color_value]
            color_to_last_index[color_value] = current_index

    # Dynamic programming array :
    # dp_arrangements[i] = nb de façons de disposer les couleurs jusqu'à la i-ème position (exclue)
    dp_arrangements = [0] * (count_non_consecutive + 1)
    dp_arrangements[0] = 1

    for current_index, color_value in enumerate(non_consecutive_colors):
        if last_occurrence_of_color[current_index] == -1:
            # Première apparition de la couleur ici
            dp_arrangements[current_index + 1] = dp_arrangements[current_index]
        else:
            previous_index = last_occurrence_of_color[current_index]
            dp_arrangements[current_index + 1] = (
                dp_arrangements[previous_index + 1] + dp_arrangements[current_index]
            ) % MODULO_BASE

    print(dp_arrangements[count_non_consecutive] % MODULO_BASE)


if __name__ == "__main__":
    count_distinct_color_arrangements()