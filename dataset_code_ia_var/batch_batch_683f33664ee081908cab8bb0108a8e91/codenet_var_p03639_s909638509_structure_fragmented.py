def read_input():
    return int(input())

def read_list():
    return list(map(int, input().split()))

def is_divisible_by_4(x):
    return x % 4 == 0

def is_even(x):
    return x % 2 == 0

def get_increment_for_value(val):
    if is_divisible_by_4(val):
        return 2
    elif is_even(val):
        return 1
    else:
        return 0

def compute_now(a, N):
    now = 0
    for i in range(N):
        now = increment_now(now, a[i])
    return now

def increment_now(now, val):
    inc = get_increment_for_value(val)
    now += inc
    return now

def is_N_odd(N):
    return N % 2 == 1

def check_result(N, now):
    if is_N_odd(N):
        return evaluate_for_odd_N(N, now)
    else:
        return evaluate_for_even_N(N, now)

def evaluate_for_odd_N(N, now):
    if now >= N - 1:
        return "Yes"
    else:
        return "No"

def evaluate_for_even_N(N, now):
    if now >= N:
        return "Yes"
    else:
        return "No"

def main():
    N = read_input()
    a = read_list()
    now = compute_now(a, N)
    result = check_result(N, now)
    print(result)

main()