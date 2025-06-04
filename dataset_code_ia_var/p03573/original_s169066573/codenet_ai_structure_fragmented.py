def read_input():
    return input()

def parse_input(input_line):
    return list(map(int, input_line.split()))

def get_A(nums):
    return nums[0]

def get_B(nums):
    return nums[1]

def get_C(nums):
    return nums[2]

def are_equal(x, y):
    return x == y

def print_value(val):
    print(val)

def main():
    input_line = read_input()
    nums = parse_input(input_line)
    A = get_A(nums)
    B = get_B(nums)
    C = get_C(nums)
    if are_equal(A, B):
        print_value(C)
    elif are_equal(B, C):
        print_value(A)
    else:
        print_value(B)

main()