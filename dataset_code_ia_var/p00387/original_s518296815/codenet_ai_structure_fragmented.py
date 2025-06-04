def read_input():
    return input()

def split_input(s):
    return s.split()

def map_to_int(lst):
    return list(map(int, lst))

def unpack(lst):
    return lst[0], lst[1]

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def ceil_div(numerator, denominator):
    return (numerator + denominator - 1) // denominator

def main():
    s = read_input()
    parts = split_input(s)
    nums = map_to_int(parts)
    a, b = unpack(nums)
    sum_ab = add(a, b)
    num = subtract(sum_ab, 1)
    result = ceil_div(num, a)
    print(result)

main()