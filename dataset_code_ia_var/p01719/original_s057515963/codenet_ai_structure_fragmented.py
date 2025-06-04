from collections import defaultdict as ddict

def get_inputs():
    n, d, x = map(int, raw_input().split(" "))
    p = [list(map(int, raw_input().split(" "))) for _ in range(d)]
    return n, d, x, p

def make_profit_dict(current, nxt, n, x):
    profit = ddict(int)
    for j in range(n):
        tmp = nxt[j] - current[j]
        add_profit_entry(profit, tmp, current[j], x)
    return profit

def add_profit_entry(profit, tmp, cost, x):
    if should_add_profit(tmp, cost, x, profit):
        profit[cost] = tmp

def should_add_profit(tmp, cost, x, profit):
    return tmp > 0 and cost <= x and tmp > profit[cost]

def init_dp(x):
    return [0 for _ in range(x+1)]

def update_dp(dp, profit):
    for cost, prof in profit.iteritems():
        for j in range(cost, len(dp)):
            dp[j] = max(dp[j], dp[j-1], dp[j-cost]+prof)

def process_day(i, p, n, x):
    profit = make_profit_dict(p[i], p[i+1], n, x)
    dp = init_dp(x)
    update_dp(dp, profit)
    return dp[x]

def process_all(n, d, x, p):
    x_val = x
    for i in range(d-1):
        increment = process_day(i, p, n, x_val)
        x_val += increment
    return x_val

def main():
    n, d, x, p = get_inputs()
    result = process_all(n, d, x, p)
    print result

main()