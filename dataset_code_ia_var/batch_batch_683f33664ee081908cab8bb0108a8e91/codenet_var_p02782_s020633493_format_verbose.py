row_start, column_start, row_end, column_end = map(int, input().split())

modulus = 10 ** 9 + 7

factorials = [1]
modular_inverses = [1]

maximum_index = row_end + column_end + 10

for current_index in range(1, maximum_index):
    previous_factorial = factorials[-1]
    current_factorial = previous_factorial * current_index % modulus
    factorials.append(current_factorial)
    current_modular_inverse = pow(current_factorial, modulus - 2, modulus)
    modular_inverses.append(current_modular_inverse)

def binomial_coefficient(total_elements, chosen_elements):
    return (
        factorials[total_elements] 
        * modular_inverses[total_elements - chosen_elements] 
        * modular_inverses[chosen_elements]
        % modulus
    )

def count_lattice_paths(rows, columns):
    return binomial_coefficient(rows + columns, columns)

total_number_of_paths = (
    count_lattice_paths(row_end + 1, column_end + 1)
    - count_lattice_paths(row_end + 1, column_start)
    - count_lattice_paths(row_start, column_end + 1)
    + count_lattice_paths(row_start, column_start)
)

total_number_of_paths %= modulus

print(total_number_of_paths)