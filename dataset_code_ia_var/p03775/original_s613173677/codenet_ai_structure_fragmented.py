def get_input():
    return int(input())

def initialize_variables():
    return 1, 0

def check_square_leq(i, n):
    return i ** 2 <= n

def is_divisor(i, n):
    return n % i == 0

def get_pair(i, n):
    return n // i

def length_of_num(num):
    return len(str(num))

def update_ans(ans, i, num):
    return max(length_of_num(num), length_of_num(i))

def increment(i):
    return i + 1

def main_loop(n, i, ans):
    while check_square_leq(i, n):
        if is_divisor(i, n):
            num = get_pair(i, n)
            ans = update_ans(ans, i, num)
        i = increment(i)
    return ans

def print_result(ans):
    print(ans)

def main():
    n = get_input()
    i, ans = initialize_variables()
    ans = main_loop(n, i, ans)
    print_result(ans)

main()