maximum_available_amount, additional_amount_per_unit, cost_per_unit = map(int, input().split())

maximum_number_of_units = maximum_available_amount // (cost_per_unit + additional_amount_per_unit)

maximum_achievable_units = 0

for current_unit in range(1, maximum_number_of_units + 1):

    total_cost_for_units = (additional_amount_per_unit + cost_per_unit) * current_unit + cost_per_unit

    if total_cost_for_units <= maximum_available_amount:
        maximum_achievable_units = current_unit
    else:
        break

print(maximum_achievable_units)