def read_input():
    return input()

def is_zero(L):
    return L == 0

def next_factor(n):
    return n + 1

def should_continue(n, L):
    return n * n <= L

def divisible(L, n):
    return L % n == 0

def divide_L(L, n):
    return L // n

def increment_S(S):
    return S + 1

def update_ans(ans, S):
    return ans * (S * 2 + 1)

def not_one(L):
    return L != 1

def update_ans_last(ans):
    return ans * 3

def final_result(ans):
    return ans // 2 + 1

def process_L(L):
    n = 2
    ans = 1
    L = int(L)

    while should_continue(n, L):
        if divisible(L, n):
            S = 0
            while divisible(L, n):
                L = divide_L(L, n)
                S = increment_S(S)
            ans = update_ans(ans, S)
        n = next_factor(n)
    if not_one(L):
        ans = update_ans_last(ans)
    return final_result(ans)

def main_loop():
    while True:
        L = read_input()
        if is_zero(int(L)):
            break
        result = process_L(L)
        print(result)

main_loop()