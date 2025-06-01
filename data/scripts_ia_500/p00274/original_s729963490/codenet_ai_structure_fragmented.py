def read_integer():
    return int(input())

def read_integer_list():
    return list(map(int, input().split()))

def is_zero(value):
    return value == 0

def maximum_of_list(lst):
    return max(lst)

def max_less_than_two(lst):
    return maximum_of_list(lst) < 2

def count_positive_elements(lst):
    count = 0
    for x in lst:
        if x > 0:
            count += 1
    return count

def print_na():
    print("NA")

def print_result(value):
    print(value)

def process_input():
    n = read_integer()
    if is_zero(n):
        return False
    a = read_integer_list()
    if max_less_than_two(a):
        print_na()
    else:
        positive_count = count_positive_elements(a)
        print_result(positive_count + 1)
    return True

def main():
    while True:
        if not process_input():
            break

main()