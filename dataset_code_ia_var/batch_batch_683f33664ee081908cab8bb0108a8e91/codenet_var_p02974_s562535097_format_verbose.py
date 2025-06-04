modulus = 10 ** 9 + 7

number_of_elements, total_cost = map(int, input().split())

dynamic_programming_table = [
    [
        [0 for _ in range(2610)]
        for _ in range(51)
    ]
    for _ in range(51)
]

dynamic_programming_table[0][0][0] = 1

for current_element_count in range(number_of_elements):

    for current_open_groups in range(number_of_elements):

        for current_cost in range(total_cost + 1):

            current_value = dynamic_programming_table[current_element_count][current_open_groups][current_cost]

            if current_value == 0:
                continue

            # Case 1: Start a new group (open new pair)
            dynamic_programming_table[
                current_element_count + 1
            ][
                current_open_groups + 1
            ][
                current_cost + 2 * current_open_groups + 2
            ] += current_value

            # Case 2: Add to one of the existing groups (without closing any)
            if current_open_groups > 0:
                dynamic_programming_table[
                    current_element_count + 1
                ][
                    current_open_groups
                ][
                    current_cost + 2 * current_open_groups
                ] += current_value * current_open_groups

                # The original code repeats this line twice.
                # If intended (possibly for two-sided addition), keep both.
                dynamic_programming_table[
                    current_element_count + 1
                ][
                    current_open_groups
                ][
                    current_cost + 2 * current_open_groups
                ] += current_value * current_open_groups

            # Case 3: Add item without affecting open groups (single element)
            dynamic_programming_table[
                current_element_count + 1
            ][
                current_open_groups
            ][
                current_cost + 2 * current_open_groups
            ] += current_value

            # Case 4: Close a group (merge groups)
            if current_open_groups > 0:
                dynamic_programming_table[
                    current_element_count + 1
                ][
                    current_open_groups - 1
                ][
                    current_cost + 2 * current_open_groups - 2
                ] += current_value * current_open_groups * current_open_groups

print(dynamic_programming_table[number_of_elements][0][total_cost] % modulus)