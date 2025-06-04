def get_input_n():
    return int(input())

def create_list(n):
    return [0 for _ in range(n)]

def fill_list(An, n):
    for i in range(n):
        An[i] = read_single_input()
    return An

def read_single_input():
    return int(input())

def initialize_variables():
    return 0, 1

def get_next(An, nxt):
    return An[nxt-1]

def increment_ret(ret):
    return ret + 1

def check_exit_condition(nxt):
    return nxt == 2

def check_loop_condition(ret, n):
    return ret <= n + 1

def solve(an, n):
    ret, nxt = initialize_variables()
    while check_loop_condition(ret, n):
        nxt = get_next(an, nxt)
        ret = increment_ret(ret)
        if check_exit_condition(nxt):
            return ret
    return -1

def print_result(result):
    print(result)

def main():
    n = get_input_n()
    An = create_list(n)
    An = fill_list(An, n)
    result = solve(An, n)
    print_result(result)

if __name__ == "__main__":
    main()