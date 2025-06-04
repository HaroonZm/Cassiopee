def sum_dimensions(x, y, h):
    return x + y + h

def check_first_case(dim_sum, w):
    return dim_sum <= 60 and w <= 2

def check_second_case(dim_sum, w):
    return dim_sum <= 80 and w <= 5

def check_third_case(dim_sum, w):
    return dim_sum <= 100 and w <= 10

def check_fourth_case(dim_sum, w):
    return dim_sum <= 120 and w <= 15

def check_fifth_case(dim_sum, w):
    return dim_sum <= 140 and w <= 20

def check_sixth_case(dim_sum, w):
    return dim_sum <= 160 and w <= 25

def get_case_value(case_index):
    values = [600, 800, 1000, 1200, 1400, 1600]
    if 0 <= case_index < len(values):
        return values[case_index]
    return 0

def determine_case(x, y, h, w):
    dim_sum = sum_dimensions(x, y, h)
    conditions = [
        check_first_case,
        check_second_case,
        check_third_case,
        check_fourth_case,
        check_fifth_case,
        check_sixth_case
    ]
    for idx, cond in enumerate(conditions):
        if cond(dim_sum, w):
            return idx
    return -1

def process(x, y, h, w):
    case_idx = determine_case(x, y, h, w)
    return get_case_value(case_idx)

def parse_input_line(line):
    return tuple(map(int, line.strip().split()))

def read_int():
    return int(input())

def read_package_data():
    return parse_input_line(input())

def calc_total_for_n_packages(n):
    total = 0
    for _ in range(n):
        x, y, h, w = read_package_data()
        value = process(x, y, h, w)
        total += value
    return total

def collect_results():
    results = []
    while True:
        n = read_int()
        if n == 0:
            break
        total = calc_total_for_n_packages(n)
        results.append(total)
    return results

def output_results(results):
    print('\n'.join(map(str, results)))

def main():
    results = collect_results()
    output_results(results)

main()