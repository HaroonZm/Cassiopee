import sys

def read_integer():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

def contains_zero(lst):
    return 0 in lst

def print_and_exit(val):
    print(val)
    sys.exit()

def product_exceeds_limit(prod):
    return prod > 10**18

def multiply_list_elements(lst):
    result = 1
    for elem in lst:
        result = multiply_and_check(result, elem)
    return result

def multiply_and_check(result, elem):
    new_result = result * elem
    if product_exceeds_limit(new_result):
        print_and_exit(-1)
    return new_result

def main():
    n = read_integer()
    a = read_int_list()
    handle_zero(a)
    ans = multiply_list_elements(a)
    print(ans)

def handle_zero(lst):
    if contains_zero(lst):
        print_and_exit(0)

main()