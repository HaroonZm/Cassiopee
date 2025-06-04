input_values = input()
input_values_list = input_values.split()
input_numbers = [int(value) for value in input_values_list]
start_value = input_numbers[0]
modulus = input_numbers[1]
target_remainder = input_numbers[2]
current_sum = start_value
initial_remainder = start_value % modulus
found_solution = True
while current_sum % modulus != target_remainder:
    current_sum += start_value
    if current_sum % modulus == initial_remainder:
        found_solution = False
        break
if found_solution:
    print('YES')
else:
    print('NO')