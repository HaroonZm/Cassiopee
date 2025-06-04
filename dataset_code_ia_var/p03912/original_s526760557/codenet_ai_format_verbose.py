import sys

# Définir une fonction d'entrée pour lire les lignes de la console sans saut de ligne final
read_input_line = lambda: sys.stdin.readline().rstrip()

# Définir une fonction de sortie pour écrire dans la console
write_output_line = lambda output_string: sys.stdout.write(output_string + "\n")

# Définir la limite de récursion
sys.setrecursionlimit(max(1000, 10 ** 9))

# Lecture des paramètres de la première ligne : taille de la liste et valeur du modulo
number_of_elements, modulo_value = map(int, read_input_line().split())

# Lecture de la liste des éléments
element_list = list(map(int, read_input_line().split()))

from collections import Counter, defaultdict

# Compter les occurrences de chaque élément
element_occurrences_counter = Counter(element_list)

# Organisation des compteurs/groupes selon la classe de congruence modulo modulo_value
class_occurrence_values = defaultdict(list)        # Les listes de comptages pour chaque classe
odd_count_per_class = defaultdict(int)             # Nombre d'occurrences impaires par classe
even_sum_per_class = defaultdict(int)              # Somme des occurrences paires par classe

for element, occurrence_count in element_occurrences_counter.items():
    class_id = element % modulo_value
    class_occurrence_values[class_id].append(occurrence_count)

    if occurrence_count % 2 == 1:
        odd_count_per_class[class_id] += 1
        even_sum_per_class[class_id] += occurrence_count - 1
    else:
        even_sum_per_class[class_id] += occurrence_count

# Fonction pour calculer le score dans le cas d'une seule classe modulo (pour les cas m/2 et 0)
def get_score_for_class(occurrence_count_list, odd_count):
    return sum(count // 2 for count in occurrence_count_list) + odd_count // 2

# Fonction pour calculer le score si on doit coupler deux classes k et m-k
def get_score_for_class_pairs(list1, odd1, list2, odd2, even_sum1, even_sum2):
    if odd1 == odd2:
        return sum(count // 2 for count in list1) + sum(count // 2 for count in list2) + odd1
    elif odd1 < odd2:
        # S'assurer que odd1 >= odd2 pour la suite
        odd1, odd2 = odd2, odd1
        list1, list2 = list2, list1
        even_sum1, even_sum2 = even_sum2, even_sum1
    
    total_score = 0
    total_score += odd2      # Tout ce qui est commun dans les impairs, on peut le prendre
    odd1 = odd1 - odd2
    if odd1 <= even_sum2:
        total_score += odd1
        even_sum2 -= odd1
        total_score += (even_sum1 // 2) + (even_sum2 // 2)
    else:
        total_score += even_sum2
        total_score += (even_sum1 // 2)
    return total_score

# Bloc principal pour calculer la réponse finale
total_pairs_count = 0

if modulo_value % 2 == 0:
    # Pour un modulo pair, gérer séparément les classes 0 et m/2, puis croiser les autres
    total_pairs_count += get_score_for_class(class_occurrence_values[0], odd_count_per_class[0])
    total_pairs_count += get_score_for_class(class_occurrence_values[modulo_value // 2], odd_count_per_class[modulo_value // 2])
    for class_offset in range(1, modulo_value // 2):
        total_pairs_count += get_score_for_class_pairs(
            class_occurrence_values[class_offset],
            odd_count_per_class[class_offset],
            class_occurrence_values[modulo_value - class_offset],
            odd_count_per_class[modulo_value - class_offset],
            even_sum_per_class[class_offset],
            even_sum_per_class[modulo_value - class_offset]
        )
else:
    # Pour un modulo impair, la classe 0 est seule, et les autres sont couplées de 1 à m//2 inclus
    total_pairs_count += get_score_for_class(class_occurrence_values[0], odd_count_per_class[0])
    for class_offset in range(1, (modulo_value // 2) + 1):
        total_pairs_count += get_score_for_class_pairs(
            class_occurrence_values[class_offset],
            odd_count_per_class[class_offset],
            class_occurrence_values[modulo_value - class_offset],
            odd_count_per_class[modulo_value - class_offset],
            even_sum_per_class[class_offset],
            even_sum_per_class[modulo_value - class_offset]
        )

print(total_pairs_count)