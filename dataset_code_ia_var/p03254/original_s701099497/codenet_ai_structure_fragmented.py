def read_input():
    return input().split()

def parse_integers(values):
    return list(map(int, values))

def get_n_x():
    n_x = read_input()
    return parse_integers(n_x)

def get_a():
    a = read_input()
    return parse_integers(a)

def sort_list(l):
    return sorted(l)

def update_x(x, a_i):
    return x - a_i

def increment_ans(ans):
    return ans + 1

def decrement_ans(ans):
    return ans - 1

def should_break(x):
    return x < 0

def check_final(x):
    return x <= 0

def compute_ans(N, x, a):
    ans = 0
    sorted_a = sort_list(a)
    for i in range(len(sorted_a)):
        x = update_x(x, sorted_a[i])
        ans = increment_ans(ans)
        if should_break(x):
            ans = decrement_ans(ans)
            break
    return ans, x

def print_result(ans, x):
    if check_final(x):
        print(ans)
    else:
        print(decrement_ans(ans))

def main():
    N, x = get_n_x()
    a = get_a()
    ans, new_x = compute_ans(N, x, a)
    print_result(ans, new_x)

main()