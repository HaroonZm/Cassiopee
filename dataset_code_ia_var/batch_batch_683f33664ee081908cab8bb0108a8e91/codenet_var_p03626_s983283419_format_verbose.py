number_of_columns = int(input())
first_domino_row = input()
second_domino_row = input()
modulo = 1000000007

extended_first_row = list(first_domino_row)
extended_first_row.append("2")
domino_orientations = [0]

for column_index in range(number_of_columns):
    if domino_orientations[-1] == 2:
        domino_orientations.append(0)
    elif extended_first_row[column_index] == extended_first_row[column_index + 1]:
        domino_orientations.append(2)
    else:
        domino_orientations.append(1)

filtered_orientations = [orientation for orientation in domino_orientations if orientation != 0]

if filtered_orientations[0] == 2:
    configuration_count = 6
else:
    configuration_count = 3

for orientation_index in range(1, len(filtered_orientations)):
    previous_orientation = filtered_orientations[orientation_index - 1]
    current_orientation = filtered_orientations[orientation_index]
    if previous_orientation == 2 and current_orientation == 2:
        configuration_count = configuration_count * 3 % modulo
    elif previous_orientation == 2 and current_orientation == 1:
        pass
    else:
        configuration_count = configuration_count * 2 % modulo

print(configuration_count)