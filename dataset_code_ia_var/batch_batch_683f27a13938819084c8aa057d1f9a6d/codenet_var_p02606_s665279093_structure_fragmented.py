def read_input():
    return input()

def parse_input(user_input):
    return list(map(int, user_input.strip().split()))

def get_left(params):
    return params[0]

def get_right(params):
    return params[1]

def get_divisor(params):
    return params[2]

def initialize_count():
    return 0

def check_divisible(num, divisor):
    return num % divisor == 0

def increment_count(cnt):
    return cnt + 1

def create_range(l, r):
    return range(l, r + 1)

def process_range(l, r, d):
    cnt = initialize_count()
    nums = create_range(l, r)
    for num in nums:
        if check_divisible(num, d):
            cnt = increment_count(cnt)
    return cnt

def print_result(cnt):
    print(cnt)

def main():
    user_input = read_input()
    params = parse_input(user_input)
    l = get_left(params)
    r = get_right(params)
    d = get_divisor(params)
    cnt = process_range(l, r, d)
    print_result(cnt)

main()