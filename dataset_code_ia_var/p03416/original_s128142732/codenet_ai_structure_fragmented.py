def get_input():
    return input()

def parse_input(s):
    return s.split()

def to_ints(strs):
    return list(map(int, strs))

def get_range_bounds():
    s = get_input()
    parts = parse_input(s)
    nums = to_ints(parts)
    return nums[0], nums[1]

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def count_palindromes_in_range(start, end):
    cnt = 0
    for i in range(start, end + 1):
        if is_palindrome(i):
            cnt = increment(cnt)
    return cnt

def increment(x):
    return x + 1

def print_result(res):
    print(res)

def main():
    a, b = get_range_bounds()
    cnt = count_palindromes_in_range(a, b)
    print_result(cnt)

main()