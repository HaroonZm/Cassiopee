def get_input():
    return input()

def parse_int(s):
    return int(s)

def parse_int_list(s):
    return list(map(int, s.split()))

def is_even(n):
    return n % 2 == 0

def all_even(nums):
    for num in nums:
        if not is_even(num):
            return False
    return True

def halve_num(n):
    return n / 2

def halve_list(nums):
    return [halve_num(n) for n in nums]

def increment(n):
    return n + 1

def decrement(n):
    return n - 1

def print_output(value):
    print(value)

def update_nums_and_count(nums, count):
    nums = halve_list(nums)
    count = increment(count)
    return nums, count

def process_numbers(nums):
    count = 0
    flag = True
    while flag:
        if not all_even(nums):
            flag = False
            break
        nums, count = update_nums_and_count(nums, count)
    return decrement(count)

def main():
    n = parse_int(get_input())
    nums = parse_int_list(get_input())
    result = process_numbers(nums)
    print_output(result)

if __name__ == '__main__':
    main()