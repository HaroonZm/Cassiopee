while True:

    number_of_equations = int(input())

    if number_of_equations == 0:
        break

    variable_relations = {}

    for _ in range(number_of_equations):

        _, first_variable_name, _, value_with_exponent, second_variable_name = input().split()

        exponent_difference = int(value_with_exponent.split("^")[1])

        if first_variable_name not in variable_relations:
            variable_relations[first_variable_name] = {}

        if second_variable_name not in variable_relations:
            variable_relations[second_variable_name] = {}

        variable_relations[first_variable_name][second_variable_name] = exponent_difference
        variable_relations[second_variable_name][first_variable_name] = -exponent_difference

    variable_names = list(variable_relations.keys())

    computed_exponents = { variable_name: None for variable_name in variable_names }

    def dfs_assign_exponents(current_variable):

        current_exponent = computed_exponents[current_variable]

        for adjacent_variable in variable_relations[current_variable]:
            required_exponent = current_exponent + variable_relations[current_variable][adjacent_variable]

            if computed_exponents[adjacent_variable] is None:
                computed_exponents[adjacent_variable] = required_exponent

                if not dfs_assign_exponents(adjacent_variable):
                    return False

            elif computed_exponents[adjacent_variable] != required_exponent:
                return False

        return True

    for variable in variable_names:

        if computed_exponents[variable] is not None:
            continue

        computed_exponents[variable] = 0

        if not dfs_assign_exponents(variable):
            print("No")
            break

    else:
        print("Yes")