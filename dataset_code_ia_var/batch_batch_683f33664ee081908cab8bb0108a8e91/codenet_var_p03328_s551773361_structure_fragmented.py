def read_input():
    return input()

def split_input(s):
    return s.split()

def convert_to_ints(lst):
    return list(map(int, lst))

def calculate_diff(a, b):
    return b - a

def calculate_ans(n, a):
    return n * (n + 1) // 2 - a

def check_and_print(diff, a):
    def loop(n):
        if n >= 1000:
            return
        if diff == n + 1:
            ans = calculate_ans(n, a)
            output_answer(ans)
        loop(n + 1)
    loop(0)

def output_answer(ans):
    print(ans)

def main():
    s = read_input()
    lst = split_input(s)
    a, b = convert_to_ints(lst)
    diff = calculate_diff(a, b)
    check_and_print(diff, a)

main()