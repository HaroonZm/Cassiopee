def read_input():
    return input()

def parse_input(s):
    return map(int, s.split())

def get_n_k():
    s = read_input()
    return parse_input(s)

def check_k_equals_one(k):
    return k == 1

def compute_result(n, k):
    if check_k_equals_one(k):
        return 0
    else:
        return n - k

def display_result(res):
    print(res)

def main():
    n, k = get_n_k()
    res = compute_result(n, k)
    display_result(res)

main()