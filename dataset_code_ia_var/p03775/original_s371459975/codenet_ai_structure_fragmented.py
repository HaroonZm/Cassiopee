def read_input():
    return input()

def to_int(s):
    return int(s)

def initial_answer():
    return 10

def range_start():
    return 1

def range_end():
    return 10**5+1

def is_divisor(x, n):
    return n % x == 0

def quotient(n, x):
    return n // x

def to_str(x):
    return str(x)

def length(s):
    return len(s)

def max_len(a, b):
    return max(a, b)

def min_val(a, b):
    return min(a, b)

def update_answer(ans, candidate):
    return min_val(ans, candidate)

def print_result(res):
    print(res)

def process_candidate(n, i, ans):
    if is_divisor(i, n):
        div1_len = length(to_str(i))
        div2_len = length(to_str(quotient(n, i)))
        candidate = max_len(div1_len, div2_len)
        return update_answer(ans, candidate)
    return ans

def solve():
    n = to_int(read_input())
    ans = initial_answer()
    for i in range(range_start(), range_end()):
        ans = process_candidate(n, i, ans)
    print_result(ans)

solve()