first_height_input, second_height_input = map(int, raw_input().split())

first_count_input, second_count_input = map(int, raw_input().split())

value_a, value_b, value_c, value_d = map(int, raw_input().split())

def calculate_total_value(first_number, second_number):
    total = (
        first_number * value_a +
        (first_number // 10) * value_c +
        second_count_input * value_b +
        (second_count_input // 20) * value_d
    )
    return total

hiroshi_total_value = calculate_total_value(first_height_input, second_height_input)
kenjiro_total_value = calculate_total_value(first_count_input, second_count_input)

result_options = ["hiroshi", "even", "kenjiro"]

# Index is (hiroshi_total_value < kenjiro_total_value) + (hiroshi_total_value <= kenjiro_total_value)
result_index = int(hiroshi_total_value < kenjiro_total_value) + int(hiroshi_total_value <= kenjiro_total_value)

print(result_options[result_index])