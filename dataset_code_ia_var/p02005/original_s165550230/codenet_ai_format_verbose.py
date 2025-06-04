import sys

liquids_by_name = {}
output_liquid_order = []

number_of_liquid_entries = int(input())

for liquid_entry_index in range(number_of_liquid_entries):
    liquid_name, liquid_density = input().split()
    liquid_density = int(liquid_density)
    if liquid_name in liquids_by_name:
        liquids_by_name[liquid_name].append(liquid_density)
    else:
        liquids_by_name[liquid_name] = [liquid_density]

for liquid_name in liquids_by_name:
    unique_densities = list(set(liquids_by_name[liquid_name]))
    unique_densities.sort()
    liquids_by_name[liquid_name] = unique_densities

number_of_liquids_to_use = int(input())

if number_of_liquids_to_use > number_of_liquid_entries:
    print("No")
    sys.exit()

for usage_index in range(number_of_liquids_to_use):
    output_liquid_name = input()
    output_liquid_order.append(output_liquid_name)

current_maximum_allowed_density = int(1e5 + 1)

for usage_step in range(number_of_liquids_to_use):
    try:
        selected_liquid_name = output_liquid_order[-(usage_step + 1)]
        available_densities = liquids_by_name[selected_liquid_name]
        if len(available_densities) == 0:
            print("No")
            sys.exit()
        selected_density = available_densities.pop()
        while selected_density >= current_maximum_allowed_density:
            if len(available_densities) == 0:
                print("No")
                sys.exit()
            selected_density = available_densities.pop()
        current_maximum_allowed_density = selected_density
    except KeyError:
        print("No")
        sys.exit()

print("Yes")