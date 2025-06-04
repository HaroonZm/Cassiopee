import math

def compute_combination(total_count, selection_count):
    if total_count < 0 or selection_count < 0 or total_count < selection_count:
        return 0
    return math.factorial(total_count) // (math.factorial(total_count - selection_count) * math.factorial(selection_count))

element_count, group_count = map(int, input().split())
modulus_value = 10 ** 9 + 7

dp_table = [[0 for _ in range(element_count + 1)] for _ in range(group_count + 1)]

dp_table[0][0] = 1
for current_group in range(1, group_count + 1):
    for current_element in range(element_count + 1):
        if current_element >= current_group:
            dp_table[current_group][current_element] = (
                dp_table[current_group - 1][current_element] + dp_table[current_group][current_element - current_group]
            ) % modulus_value
        else:
            dp_table[current_group][current_element] = dp_table[current_group - 1][current_element]

print(dp_table[group_count][element_count])