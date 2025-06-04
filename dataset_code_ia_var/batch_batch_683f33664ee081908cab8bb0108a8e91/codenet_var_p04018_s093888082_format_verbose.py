import sys

# Lecture de la chaîne et initialisation des variables
input_word_as_char_list = list(raw_input())
input_word_length = len(input_word_as_char_list)
primitive_period_length = -1

def get_border_validity_list(sequence):
    sequence_length = len(sequence)
    z_array = [0] * sequence_length
    z_box_right = 0
    z_box_left = 0
    valid_borders = [True] * sequence_length

    for current_position in range(1, sequence_length):
        if current_position + z_array[current_position - z_box_left] < z_box_right + z_array[z_box_left]:
            z_array[current_position] = z_array[current_position - z_box_left]
        else:
            length = max(0, z_box_right + z_array[z_box_left] - current_position)
            while current_position + length < input_word_length and sequence[length] == sequence[current_position + length]:
                length += 1
            z_array[current_position] = length
            z_box_left = current_position

    for prefix_length in range(1, sequence_length):
        for k in range(2, z_array[prefix_length] // prefix_length + 2):
            valid_borders[k * prefix_length - 1] = False

    return valid_borders

# Recherche du plus petit period
for candidate_period in range(1, input_word_length // 2 + 1):
    if input_word_length % candidate_period == 0:
        if input_word_as_char_list[:input_word_length - candidate_period] == input_word_as_char_list[candidate_period:]:
            primitive_period_length = candidate_period
            break

# Cas où aucun period n'est trouvé
if primitive_period_length == -1:
    print 1
    print 1
    sys.exit()

# Cas où la période primitive est 1
if primitive_period_length == 1:
    print input_word_length
    print 1
    sys.exit()

# Calcul des listes de validité de bordure à gauche et à droite
valid_left_borders = get_border_validity_list(input_word_as_char_list)
input_word_as_char_list.reverse()
valid_right_borders = get_border_validity_list(input_word_as_char_list)

# Comptage des positions valides
number_of_splits = 0
for split_position in range(input_word_length - 1):
    if valid_left_borders[split_position] and valid_right_borders[input_word_length - 2 - split_position]:
        number_of_splits += 1

print 2
print number_of_splits