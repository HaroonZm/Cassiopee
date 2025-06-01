def read_integer():
    return int(input())

def read_list(n):
    return [read_integer() for _ in range(n)]

def find_max(lst):
    return max(lst)

def find_divisors(n):
    divisors = []
    limit = int(n ** 0.5)
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return divisors

def sort_list(lst):
    lst.sort()
    return lst

def calculate_difference(lst, divisors):
    d = 0
    for i in lst:
        for divisor in divisors:
            if i <= divisor:
                d += divisor - i
                break
    return d

def main():
    N = read_integer()
    lst = read_list(N)
    max_ = find_max(lst)
    divisors = find_divisors(max_)
    divisors = sort_list(divisors)
    lst = sort_list(lst)
    d = calculate_difference(lst, divisors)
    print(d)

main()