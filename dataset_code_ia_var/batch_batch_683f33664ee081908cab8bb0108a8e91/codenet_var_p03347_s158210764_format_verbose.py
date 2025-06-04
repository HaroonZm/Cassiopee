number_of_elements = int(input())

sequence_of_integers = [0] * number_of_elements

for current_index in range(number_of_elements):
    sequence_of_integers[current_index] = int(input())

is_solution_possible = 1

if sequence_of_integers[0] != 0:
    is_solution_possible = 0

total_operations = 0

for index in range(1, number_of_elements):
    difference_with_previous = sequence_of_integers[index] - sequence_of_integers[index - 1]
    
    if difference_with_previous > 1:
        if sequence_of_integers[index] != 0:
            is_solution_possible = 0
            break
    
    elif difference_with_previous == 1:
        total_operations += 1
    
    else:
        total_operations += sequence_of_integers[index]

if is_solution_possible:
    print(total_operations)
else:
    print(-1)