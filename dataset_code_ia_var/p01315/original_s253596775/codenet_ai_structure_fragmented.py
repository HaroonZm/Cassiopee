def get_input():
    return input()

def check_stop(n):
    return n == 0

def get_iteration_count():
    n = get_input()
    if check_stop(int(n)):
        return 0
    return int(n)

def parse_raw_input():
    inp = raw_input().split()
    name = inp[0]
    numbers = list(map(int, inp[1:]))
    return name, numbers

def compute_result(numbers):
    P, A, B, C, D, E, F, S, M = numbers
    numerator = (M * F * S - P)
    denominator = (A + B + C + (D + E) * M)
    return numerator * 1.0 / denominator

def process_entry():
    name, numbers = parse_raw_input()
    result = compute_result(numbers)
    return [name, result]

def process_entries(n):
    ans = []
    for _ in range(n):
        entry = process_entry()
        ans.append(entry)
    return ans

def sort_entries(ans):
    # First, sort lexicographically
    ans_sorted = sorted(ans)
    # Then, sort based on values in descending order
    ans_sorted = sorted(ans_sorted, key=lambda x: x[1], reverse=True)
    return ans_sorted

def print_entries(ans_sorted):
    for k, v in ans_sorted:
        print(k)

def print_separator():
    print("#")

def main_loop():
    while True:
        n = get_iteration_count()
        if n == 0:
            break
        ans = process_entries(n)
        ans_sorted = sort_entries(ans)
        print_entries(ans_sorted)
        print_separator()

main_loop()