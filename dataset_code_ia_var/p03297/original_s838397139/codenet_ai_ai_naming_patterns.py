import math

def process_test_cases(num_cases, list_a, list_b, list_c, list_d):
    results_list = []
    for case_index in range(num_cases):
        result = process_single_case(
            list_a[case_index],
            list_b[case_index],
            list_c[case_index],
            list_d[case_index]
        )
        results_list.append(result)
    return results_list

def process_single_case(value_a, value_b, value_c, value_d):
    if value_a < value_b:
        return 'No'
    if value_d < value_b:
        return 'No'
    if value_c < value_b:
        greatest_common_divisor = math.gcd(value_b, value_d)
        remainder_a_b = value_a % value_b
        if greatest_common_divisor == 1:
            if value_b - 1 > value_c:
                return 'No'
        elif greatest_common_divisor == value_b:
            if remainder_a_b > value_c:
                return 'No'
        else:
            if (value_b - greatest_common_divisor) > value_c:
                return 'No'
    return 'Yes'

def read_input_data():
    total_cases = int(input())
    input_list_a = []
    input_list_b = []
    input_list_c = []
    input_list_d = []
    for _ in range(total_cases):
        input_a, input_b, input_c, input_d = map(int, input().split())
        input_list_a.append(input_a)
        input_list_b.append(input_b)
        input_list_c.append(input_c)
        input_list_d.append(input_d)
    return total_cases, input_list_a, input_list_b, input_list_c, input_list_d

def main_entry_point():
    num_cases, list_a, list_b, list_c, list_d = read_input_data()
    outcome_list = process_test_cases(num_cases, list_a, list_b, list_c, list_d)
    for outcome in outcome_list:
        print(outcome)

if __name__ == '__main__':
    main_entry_point()