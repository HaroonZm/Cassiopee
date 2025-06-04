def get_input():
    return int(input())

def get_weights():
    return list(map(int, input().split()))

def compute_total(weights):
    return sum(weights)

def initialize_answer():
    return 1000000000

def compute_partial_weights(weights, index):
    return weights[:index]

def compute_partial_sum(weights):
    return sum(weights)

def compute_difference(total, partial_sum):
    return abs(total - 2 * partial_sum)

def update_answer(current_ans, diff):
    if current_ans > diff:
        return diff
    else:
        return current_ans

def main():
    N = get_input()
    W = get_weights()
    total_W = compute_total(W)
    ans = initialize_answer()
    for i in range(N):
        partial_W = compute_partial_weights(W, i)
        partial_sum = compute_partial_sum(partial_W)
        diff = compute_difference(total_W, partial_sum)
        ans = update_answer(ans, diff)
    print_result(ans)

def print_result(ans):
    print(ans)

main()