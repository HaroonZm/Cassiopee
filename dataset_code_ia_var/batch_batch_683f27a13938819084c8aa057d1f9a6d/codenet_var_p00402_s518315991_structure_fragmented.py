def read_integer():
    return int(input())

def read_integers():
    return list(map(int, input().split()))

def get_maximum(lst):
    return max(lst)

def get_minimum(lst):
    return min(lst)

def calc_difference(x, y):
    return x - y

def is_even(n):
    return n % 2 == 0

def integer_division(n, d):
    return n // d

def increment(n):
    return n + 1

def compute_steps(diff):
    if is_even(diff):
        return integer_division(diff, 2)
    else:
        return increment(integer_division(diff, 2))

def main():
    N = read_integer()
    a = read_integers()
    maximum = get_maximum(a)
    minimum = get_minimum(a)
    diff = calc_difference(maximum, minimum)
    result = compute_steps(diff)
    print(result)

main()