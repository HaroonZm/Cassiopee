import sys

standard_input = sys.stdin.readline

number_of_elements = int(standard_input())

input_numbers = list(map(int, standard_input().split()))

positive_infinity = float("INF")

minimum_cost = [
    [positive_infinity] * (number_of_elements + 1) 
    for _ in range(number_of_elements)
]

# Construct prefix sums in-place
for prefix_sum_index in range(number_of_elements - 1):
    input_numbers[prefix_sum_index + 1] += input_numbers[prefix_sum_index]

# Adjust to 1-based indexing for prefix sums
input_numbers.insert(0, 0)

# Prepare 2D prefix sum differences
prefix_sum_difference = [
    [0] * (number_of_elements + 1) 
    for _ in range(number_of_elements)
]

for start_index in range(number_of_elements):
    prefix_sum_row = prefix_sum_difference[start_index]
    for end_index in range(start_index + 1, number_of_elements + 1):
        prefix_sum_row[end_index] = input_numbers[end_index] - input_numbers[start_index]

def compute_merge_cost(
    left_index, 
    middle_index, 
    right_index, 
    current_total_cost, 
    upper_bound_cost, 
    prefix_sum_row
):
    left_sum = prefix_sum_row[middle_index]
    right_sum = prefix_sum_difference[middle_index][right_index]
    carry = 0
    while left_sum or right_sum or carry:
        left_digit = left_sum % 10
        right_digit = right_sum % 10
        current_total_cost += left_digit * right_digit + carry
        if current_total_cost >= upper_bound_cost:
            return upper_bound_cost
        carry = (left_digit + right_digit + carry > 9)
        left_sum //= 10
        right_sum //= 10
    return current_total_cost

for single_element_index in range(number_of_elements):
    minimum_cost[single_element_index][single_element_index + 1] = 0

for interval_length in range(1, number_of_elements + 1):
    for left in range(number_of_elements - interval_length + 1):
        right = left + interval_length
        min_cost_row = minimum_cost[left]
        min_merge_cost = min_cost_row[right]
        prefix_sum_row = prefix_sum_difference[left]
        for middle in range(left + 1, right):
            candidate_cost = min_cost_row[middle] + minimum_cost[middle][right]
            min_merge_cost = compute_merge_cost(
                left, 
                middle, 
                right, 
                candidate_cost, 
                min_merge_cost, 
                prefix_sum_row
            )
        min_cost_row[right] = min_merge_cost

print(minimum_cost[0][number_of_elements])