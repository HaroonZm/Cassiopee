def get_input_value():
    return int(input())

def read_range():
    return map(int, input().split())

def compute_range_length(l, r):
    return r - l + 1

def update_ans(ans, value):
    return ans + value

def handle_single_iteration(ans):
    l, r = read_range()
    length = compute_range_length(l, r)
    return update_ans(ans, length)

def loop_over_ranges(N, ans):
    def iterate(i, ans):
        if i >= N:
            return ans
        ans = handle_single_iteration(ans)
        return iterate(i + 1, ans)
    return iterate(0, ans)

def print_output(ans):
    print(ans)

def main():
    N = get_input_value()
    ans = 0
    ans = loop_over_ranges(N, ans)
    print_output(ans)

main()