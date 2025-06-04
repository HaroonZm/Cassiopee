def read_input():
    return input()

def parse_input(s):
    return int(s)

def get_mod():
    return 10**9 + 7

def calculate_power(base, exponent, mod):
    return pow(base, exponent, mod)

def calculate_first_term(N, mod):
    return calculate_power(10, N, mod)

def calculate_second_term(N, mod):
    return 2 * calculate_power(9, N, mod)

def calculate_third_term(N, mod):
    return calculate_power(8, N, mod)

def add_mod(ans, mod):
    return ans + mod

def compute_final_answer(term1, term2, term3, mod):
    ans = term1 - term2 + term3
    ans = add_mod(ans, mod)
    return ans % mod

def print_result(res):
    print(res)

def main():
    input_str = read_input()
    N = parse_input(input_str)
    mod = get_mod()
    term1 = calculate_first_term(N, mod)
    term2 = calculate_second_term(N, mod)
    term3 = calculate_third_term(N, mod)
    result = compute_final_answer(term1, term2, term3, mod)
    print_result(result)

if __name__ == '__main__':
    main()