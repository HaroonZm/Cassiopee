def read_n():
    return int(input())

def read_list():
    return list(map(int, input().split()))

def read_input():
    n = read_n()
    if n == 0:
        return None, None
    p = read_list()
    j = read_list()
    return n, (p, j)

def initial_sum(p):
    return sum(p)

def sort_desc(j):
    return sorted(j, reverse=True)

def initial_ans(s, n):
    return s * n

def update_sum(s, add):
    return s + add

def update_ans(ans, s, k):
    return max(ans, s * k)

def process_case(n, p, j):
    s = initial_sum(p)
    j_sorted = sort_desc(j)
    ans = initial_ans(s, n)
    for i in range(n-1):
        s = update_sum(s, j_sorted[i])
        k = n - 1 - i
        ans = update_ans(ans, s, k)
    return ans

def print_ans(ans):
    print(ans)

def main_loop():
    while True:
        n, data = read_input()
        if n == 0:
            break
        p, j = data
        ans = process_case(n, p, j)
        print_ans(ans)

main_loop()