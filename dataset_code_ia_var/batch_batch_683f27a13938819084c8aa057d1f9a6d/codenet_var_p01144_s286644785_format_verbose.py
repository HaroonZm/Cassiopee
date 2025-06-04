import sys

while True:

    num_packages, initial_capacity = [int(value) for value in input().split()]

    if num_packages == 0 and initial_capacity == 0:
        sys.exit()

    package_list = []
    total_additional_cost = 0

    for package_index in range(num_packages):
        package_details = [int(detail) for detail in input().split()]
        package_list.append(package_details)

    package_list.sort(key=lambda package: package[1], reverse=True)

    remaining_capacity = initial_capacity

    for package in package_list:

        package_quantity = package[0]
        package_cost_per_unit = package[1]

        if package_quantity <= remaining_capacity:
            remaining_capacity -= package_quantity

        elif remaining_capacity > 0:
            needed_units = package_quantity - remaining_capacity
            total_additional_cost += package_cost_per_unit * needed_units
            remaining_capacity = 0

        else:
            total_additional_cost += package_cost_per_unit * package_quantity

    print(total_additional_cost)