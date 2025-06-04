def read_n():
    return int(input())

def read_ai():
    return list(map(int, input().split()))

def initialize_sa():
    return [0]

def initialize_ans():
    return float("INF")

def calc_prefix_sums(sa, a_list, n):
    def add_next(i):
        sa.append(sa[i] + a_list[i])
    for i in range(n):
        add_next(i)

def get_total_sum(sa):
    return sa[-1]

def calc_diff(sa_value, total_sum):
    return abs(sa_value - (total_sum - sa_value))

def update_ans(ans, diff):
    return min(ans, diff)

def iter_prefix_sums(sa, n, total_sum):
    ans = initialize_ans()
    for i in range(n + 1):
        diff = calc_diff(sa[i], total_sum)
        ans = update_ans(ans, diff)
    return ans

def main():
    n = read_n()
    a_list = read_ai()
    sa = initialize_sa()
    calc_prefix_sums(sa, a_list, n)
    total_sum = get_total_sum(sa)
    ans = iter_prefix_sums(sa, n, total_sum)
    print(ans)

main()