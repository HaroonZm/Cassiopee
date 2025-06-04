import heapq

# Nombre d'éléments par groupe
number_of_elements_per_group = int(input())

# Liste des entiers d'entrée
sequence_of_integers = list(map(int, input().split()))

# Première section (gauche)
left_group_elements = sequence_of_integers[:number_of_elements_per_group]

# Troisième section (droite), les inverser pour un max-heap simulé par heapq (min-heap) 
right_group_elements = [-element for element in sequence_of_integers[2 * number_of_elements_per_group:]]

# Calcul initial des sommes totales de chaque groupe
total_sum_left_group = sum(left_group_elements)
total_sum_right_group = sum(right_group_elements)

# Tableaux des résultats, initialisés à zéro
results_sums = [0] * (number_of_elements_per_group + 1)

results_sums[0] = total_sum_left_group
results_sums[number_of_elements_per_group] = total_sum_right_group

# Construction du min-heap pour la section gauche
heapq.heapify(left_group_elements)

# Construction du min-heap simulant un max-heap pour la section droite
heapq.heapify(right_group_elements)

# Parcours de la partie centrale pour mettre à jour la section gauche
for index_in_sequence in range(number_of_elements_per_group, 2 * number_of_elements_per_group):
    current_value = sequence_of_integers[index_in_sequence]
    smallest_value_popped = heapq.heappushpop(left_group_elements, current_value)
    total_sum_left_group += current_value - smallest_value_popped
    index_in_results = index_in_sequence - number_of_elements_per_group + 1
    results_sums[index_in_results] += total_sum_left_group

# Parcours de la partie centrale pour mettre à jour la section droite
for index_in_sequence in range(2 * number_of_elements_per_group - 1, number_of_elements_per_group - 1, -1):
    current_value_negated = -sequence_of_integers[index_in_sequence]
    largest_value_popped_negated = heapq.heappushpop(right_group_elements, current_value_negated)
    total_sum_right_group += current_value_negated - largest_value_popped_negated
    index_in_results = index_in_sequence - number_of_elements_per_group
    results_sums[index_in_results] += total_sum_right_group

# Affichage du résultat maximal obtenu
print(max(results_sums))