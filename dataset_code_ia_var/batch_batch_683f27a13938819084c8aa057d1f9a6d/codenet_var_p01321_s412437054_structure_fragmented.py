def get_input():
    return input()

def to_int(value):
    return int(value)

def is_zero(value):
    return value == 0

def read_n():
    return to_int(get_input())

def split_input(line):
    return line.split()

def process_score_line():
    line = get_input()
    return split_input(line)

def score_str_to_int(score_str):
    return to_int(score_str)

def sum_scores(scores):
    total = 0
    for s in scores:
        total = add_to_total(total, s)
    return total

def add_to_total(total, s):
    return total + score_str_to_int(s)

def process_scores(n):
    result = []
    for _ in range(n):
        scores = process_score_line()
        total = sum_scores(scores)
        result = append_to_list(result, total)
    return result

def append_to_list(lst, value):
    lst.append(value)
    return lst

def find_max(lst):
    return max(lst)

def find_min(lst):
    return min(lst)

def print_output(max_value, min_value):
    print(max_value, min_value)

def main_loop():
    while True:
        n = read_n()
        if is_zero(n):
            break
        totals = process_scores(n)
        max_total = find_max(totals)
        min_total = find_min(totals)
        print_output(max_total, min_total)

main_loop()