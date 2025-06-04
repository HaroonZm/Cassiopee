def get_input():
    return input()

def parse_input(input_str):
    return map(int, input_str.split())

def compute_diff(e, w):
    return e - w

def init_true_height():
    return 0

def get_range_end(diff):
    return diff + 1

def sum_heights(diff):
    total = init_true_height()
    for h in get_height_range(diff):
        total = add_height(total, h)
    return total

def get_height_range(diff):
    return range(1, get_range_end(diff))

def add_height(current, h):
    return current + h

def compute_result(true_height, e):
    return true_height - e

def print_result(result):
    print(result)

def main():
    input_str = get_input()
    w, e = parse_input(input_str)
    diff = compute_diff(e, w)
    true_height = sum_heights(diff)
    result = compute_result(true_height, e)
    print_result(result)

main()