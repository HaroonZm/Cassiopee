import math

def read_integer():
    return int(input())

def initialize_list():
    return []

def update_max(current_max, value):
    if value > current_max:
        return value
    return current_max

def append_to_list(lst, value):
    lst.append(value)

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def find_smallest_divisor_geq(divisors, value):
    index = 0
    while divisors[index] < value:
        index += 1
    return divisors[index]

def calculate_increment(divisor, value):
    return divisor - value

def main():
    n = read_integer()
    lis = initialize_list()
    cou = 0
    for _ in range(n):
        a = read_integer()
        cou = update_max(cou, a)
        append_to_list(lis, a)
    num = find_divisors(cou)
    ans = 0
    for nu in lis:
        co = find_smallest_divisor_geq(num, nu)
        ans += calculate_increment(co, nu)
    print(ans)

main()