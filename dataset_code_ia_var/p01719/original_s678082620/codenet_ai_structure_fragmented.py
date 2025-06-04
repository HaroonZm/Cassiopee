def parse_input():
    n, d, x = map(int, input().split())
    plst = [get_prices() for _ in range(d)]
    return n, d, x, plst

def get_prices():
    return list(map(int, input().split()))

def compute_value_list(plst, i, n):
    return [plst[i + 1][j] - plst[i][j] for j in range(n)]

def compute_weight_list(plst, i, n):
    return [plst[i][j] for j in range(n)]

def update_x(x, wlst, vlst):
    add_val = get_pro(wlst, vlst)
    return x + add_val

def get_pro(w, v):
    dp = initialize_dp()
    for a in range(get_n()):
        wa = get_weight(w, a)
        va = get_value(v, a)
        dp = update_dp(dp, wa, va)
    return get_final_profit(dp)

def initialize_dp():
    return [0] * (get_x() + 1)

def get_n():
    global n
    return n

def get_x():
    global x
    return x

def get_weight(w, idx):
    return w[idx]

def get_value(v, idx):
    return v[idx]

def update_dp(dp, wa, va):
    for b in range(wa, get_x() + 1):
        dp[b] = max(dp[b], dp[b - wa] + va)
    return dp

def get_final_profit(dp):
    return dp[get_x()]

def process(n, d, x_val, plst):
    global n, x
    n = n
    x = x_val
    for i in range(d - 1):
        vlst = compute_value_list(plst, i, n)
        wlst = compute_weight_list(plst, i, n)
        x = update_x(x, wlst, vlst)
    print(x)

def main():
    n_val, d_val, x_val, plst = parse_input()
    process(n_val, d_val, x_val, plst)

main()