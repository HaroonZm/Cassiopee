def read_input():
    return input()

def parse_input(line):
    return map(int, line.split())

def get_k_r():
    line = read_input()
    k, r = parse_input(line)
    return k, r

def check_condition(k):
    return k >= 10

def compute_output(r, k):
    if check_condition(k):
        return r
    else:
        return r + 100 * (10 - k)

def print_result(result):
    print(result)

def main():
    k, r = get_k_r()
    result = compute_output(r, k)
    print_result(result)

main()