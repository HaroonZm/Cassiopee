from collections import defaultdict

def initialize_prime_factor_dict():
    return defaultdict(int)

def is_divisible(n, i):
    return n % i == 0

def increment_prime_count(dic, i):
    dic[i] += 1

def divide_n_by_i(n, i):
    return n // i

def increment_i(i):
    return i + 1

def update_prime_dict(n, dic, i):
    while is_divisible(n, i):
        increment_prime_count(dic, i)
        n = divide_n_by_i(n, i)
    return n

def handle_remaining_prime(n, dic):
    if n != 1:
        dic[n] += 1

def dic_values_to_list(dic):
    return list(dic.values())

def soinnsuubunnkai(n):
    dic = initialize_prime_factor_dict()
    i = 2
    while i * i <= n:
        n = update_prime_dict(n, dic, i)
        i = increment_i(i)
    handle_remaining_prime(n, dic)
    return dic_values_to_list(dic)

def get_element_at(values, ind):
    return values[ind]

def multiply(a, b):
    return a * b

def is_base_case(ind, end):
    return ind == end

def saiki_left(values, score, ind, end):
    return saiki(values, multiply(score, get_element_at(values, ind)), ind + 1, end)

def saiki_right(values, score, ind, end):
    return saiki(values, score, ind + 1, end)

def sum_and_double(left, right):
    return left * 2 + right

def saiki(values, score, ind, end):
    if is_base_case(ind, end):
        return score
    left = saiki_left(values, score, ind, end)
    right = saiki_right(values, score, ind, end)
    return sum_and_double(left, right)

def add_one(n):
    return n + 1

def divide_by_two(n):
    return n // 2

def print_result(res):
    print(res)

def end_condition(n):
    return n == 0

def read_input():
    return int(input())

def main_loop():
    while True:
        n = read_input()
        if end_condition(n):
            break
        values = soinnsuubunnkai(n)
        res = divide_by_two(add_one(saiki(values, 1, 0, len(values))))
        print_result(res)

main_loop()