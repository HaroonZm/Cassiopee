def is_divisible_by_2(n):
    return n % 2 == 0

def is_divisible_by_5(n):
    return n % 5 == 0

def divide_by_2(n):
    return n // 2

def divide_by_5(n):
    return n // 5

def count_factor_2(n):
    count = 0
    while is_divisible_by_2(n):
        n = divide_by_2(n)
        count += 1
    return count, n

def count_factor_5(n):
    count = 0
    while is_divisible_by_5(n):
        n = divide_by_5(n)
        count += 1
    return count, n

def calc(n):
    cnt_2, n_after_2 = count_factor_2(n)
    cnt_5, n_after_5 = count_factor_5(n_after_2)
    return cnt_2, cnt_5

def input_value():
    return input()

def is_zero(value):
    try:
        return int(value) == 0
    except ValueError:
        return False

def to_int(value):
    return int(value)

def add_values(a, b):
    return a + b

def min_value(a, b):
    return min(a, b)

def print_value(value):
    print(value)

def loop_range(start, end):
    return range(start, end, -1)

def main_loop():
    while True:
        N = input_value()
        if is_zero(N):
            quit()

        N_int = to_int(N)

        t2 = 0
        t5 = 0

        for i in loop_range(N_int, 0):
            x, y = calc(i)
            t2 = add_values(t2, x)
            t5 = add_values(t5, y)

        result = min_value(t2, t5)
        print_value(result)

main_loop()