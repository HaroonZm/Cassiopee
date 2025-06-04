def read_input():
    return int(input())

def read_list():
    return list(map(int, input().split()))

def create_sub_list(N):
    return [0] * N

def compute_sub_item(a_i, N):
    return (a_i - (N - 1) - 1) // N + 1

def fill_sub_list(N, a):
    sub = create_sub_list(N)
    for i in range(N):
        sub[i] = compute_sub_item(a[i], N)
    return sub

def calc_sum_sub(sub):
    return sum(sub)

def should_break(sum_sub):
    return sum_sub == 0

def update_ans(ans, sum_sub):
    return ans + sum_sub

def update_a_list(N, a, sub, sum_sub):
    for i in range(N):
        a[i] -= N * sub[i] - (sum_sub - sub[i])
    return a

def main():
    N = read_input()
    a = read_list()
    ans = 0
    while True:
        sub = fill_sub_list(N, a)
        sum_sub = calc_sum_sub(sub)
        if should_break(sum_sub):
            break
        ans = update_ans(ans, sum_sub)
        a = update_a_list(N, a, sub, sum_sub)
    print(ans)

main()