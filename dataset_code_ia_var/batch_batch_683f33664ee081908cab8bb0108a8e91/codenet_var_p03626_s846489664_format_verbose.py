number_of_columns = int(input())

upper_row_pattern = input()
lower_row_pattern = input()

modulo_value = 1000000007

current_position = 0
domino_orientations = []

while current_position < number_of_columns:
    if upper_row_pattern[current_position] == lower_row_pattern[current_position]:
        domino_orientations.append("VERTICAL")
        current_position += 1
    else:
        domino_orientations.append("HORIZONTAL")
        current_position += 2

if domino_orientations[0] == "VERTICAL":
    total_arrangements = 3
else:
    total_arrangements = 6

previous_domino_orientation = domino_orientations[0]

for domino_index in range(1, len(domino_orientations)):
    current_domino_orientation = domino_orientations[domino_index]
    if previous_domino_orientation == "VERTICAL" and current_domino_orientation == "VERTICAL":
        total_arrangements = (total_arrangements * 2) % modulo_value
    elif previous_domino_orientation == "VERTICAL" and current_domino_orientation == "HORIZONTAL":
        total_arrangements = (total_arrangements * 2) % modulo_value
    elif previous_domino_orientation == "HORIZONTAL" and current_domino_orientation == "HORIZONTAL":
        total_arrangements = (total_arrangements * 3) % modulo_value
    previous_domino_orientation = current_domino_orientation

print(total_arrangements % modulo_value)