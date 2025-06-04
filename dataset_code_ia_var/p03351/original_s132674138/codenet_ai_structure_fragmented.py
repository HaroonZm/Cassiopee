def get_input():
    return input()

def parse_input(s):
    return map(int, s.split())

def get_a(nums):
    return nums[0]

def get_b(nums):
    return nums[1]

def get_c(nums):
    return nums[2]

def get_d(nums):
    return nums[3]

def calc_abs(x, y):
    return abs(x - y)

def check_condition1(a, b, d):
    return calc_abs(a, b) <= d

def check_condition2(b, c, d):
    return calc_abs(b, c) <= d

def check_subconditions(a, b, c, d):
    return check_condition1(a, b, d) and check_condition2(b, c, d)

def check_condition3(a, c, d):
    return calc_abs(a, c) <= d

def is_yes(a, b, c, d):
    return check_subconditions(a, b, c, d) or check_condition3(a, c, d)

def get_output(a, b, c, d):
    return "Yes" if is_yes(a, b, c, d) else "No"

def main():
    s = get_input()
    nums = list(parse_input(s))
    a = get_a(nums)
    b = get_b(nums)
    c = get_c(nums)
    d = get_d(nums)
    result = get_output(a, b, c, d)
    print(result)

main()