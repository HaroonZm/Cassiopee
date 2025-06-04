number_of_fields = int(input())

field_max_capacities = list(map(int, input().split()))

current_field_amounts = [0 for _ in range(number_of_fields)]

number_of_operations = int(input())

violation_field_index = 0

for _ in range(number_of_operations):

    operation_type, field_index, change_amount = map(int, input().split())

    if operation_type == 1:  # Harvest

        current_field_amounts[field_index - 1] += change_amount

        if current_field_amounts[field_index - 1] > field_max_capacities[field_index - 1]:

            violation_field_index = field_index

            break

    elif operation_type == 2:  # Ship

        current_field_amounts[field_index - 1] -= change_amount

        if current_field_amounts[field_index - 1] < 0:

            violation_field_index = field_index

            break

print(violation_field_index)