def main_loop():
    while True:
        n = get_input()
        if is_end(n):
            break
        L = compute_L(n)
        dp = initialize_dp(L)
        dp = process_all_items(n, L, dp)
        num, su = get_result(dp)
        display_result(num, su)

def get_input():
    return int(input())

def is_end(n):
    return n == 0

def compute_L(n):
    return 500 * n

def initialize_dp(L):
    dp = [None] * (L + 1)
    dp[0] = (0, 0)
    return dp

def process_all_items(n, L, dp):
    for i in range(n):
        cost = get_item_cost()
        d3 = get_d3(cost)
        dp2 = copy_dp(dp)
        for j in range(L + 1):
            update_dp_at_index(j, dp, dp2, d3, cost, L)
        dp = dp2
    return dp

def get_item_cost():
    return int(input())

def get_d3(cost):
    return cost % 1000

def copy_dp(dp):
    return dp[:]

def update_dp_at_index(j, dp, dp2, d3, cost, L):
    if is_invalid_dp(dp, j):
        return
    num, su = dp[j]
    if d3 == 0:
        handle_d3_zero(j, dp2, num, su, cost)
    elif is_d3_in_range_1_500_j(d3, j):
        handle_d3_in_range(j, dp2, num, su, cost, d3)
    else:
        handle_d3_else(j, dp2, num, su, cost, d3)

def is_invalid_dp(dp, j):
    return dp[j] is None

def handle_d3_zero(j, dp2, num, su, cost):
    if 500 <= j:
        update_dp_if_better(dp2, j - 500, num + 1, su - cost)

def is_d3_in_range_1_500_j(d3, j):
    return 1 <= d3 <= 500 + j

def handle_d3_in_range(j, dp2, num, su, cost, d3):
    new_j = j + (500 - d3)
    update_dp_if_better(dp2, new_j, num + 1, su - cost)

def handle_d3_else(j, dp2, num, su, cost, d3):
    new_j = j + (1000 - d3)
    update_dp_if_better(dp2, new_j, num, su - cost)

def update_dp_if_better(dp2, idx, num, su):
    if idx < len(dp2):
        current = dp2[idx]
        candidate = (num, su)
        if current is None or candidate > current:
            dp2[idx] = candidate

def get_result(dp):
    return max(x for x in dp if x is not None)

def display_result(num, su):
    print(num, -su)

main_loop()