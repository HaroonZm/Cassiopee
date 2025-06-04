def get_input():
    return input()

def parse_input_line(line):
    return list(map(int, line.split()))

def get_values():
    n_m = get_input()
    n, m = parse_input_line(n_m)
    c_list_input = get_input()
    c_lst = parse_input_line(c_list_input)
    return n, m, c_lst

def digits():
    return (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

def generate_combinations(n):
    from itertools import combinations_with_replacement as cwr
    return cwr(digits(), n)

def calculate_cost_and_string(t, c_lst):
    total_cost = 0
    output = ""
    for digit in t:
        cost, output = add_digit(cost=total_cost, output=output, digit=digit, c_lst=c_lst)
        total_cost = cost
    return total_cost, output

def add_digit(cost, output, digit, c_lst):
    return cost + c_lst[digit], output + str(digit)

def is_cost_valid(cost, m):
    return cost <= m

def print_result_and_exit(output):
    print(output)

def print_na():
    print("NA")

def process_combination(t, c_lst, m):
    cost, output = calculate_cost_and_string(t, c_lst)
    if is_cost_valid(cost, m):
        print_result_and_exit(output)
        return True
    return False

def main():
    n, m, c_lst = get_values()
    for t in generate_combinations(n):
        if process_combination(t, c_lst, m):
            return
    print_na()

main()