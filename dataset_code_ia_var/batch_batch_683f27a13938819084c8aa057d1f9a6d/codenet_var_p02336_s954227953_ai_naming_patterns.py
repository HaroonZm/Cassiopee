import math

def compute_combinations(total_elements, selected_elements):
    if total_elements < 0 or selected_elements < 0 or total_elements < selected_elements:
        return 0
    return (math.factorial(total_elements) //
            math.factorial(total_elements - selected_elements) //
            math.factorial(selected_elements))

input_total_elements, input_selected_elements = map(int, input().split())
combination_modulus = 10 ** 9 + 7

result_combinations = compute_combinations(input_total_elements - 1, input_selected_elements - 1)
print(result_combinations % combination_modulus)