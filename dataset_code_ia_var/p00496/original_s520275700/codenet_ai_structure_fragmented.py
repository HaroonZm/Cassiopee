def read_input():
    N, T, S = map(int, input().split())
    a = [parse_activity() for _ in range(N)]
    return N, T, S, a

def parse_activity():
    return tuple(map(int, input().split()))

def initialize_dp(T):
    dp = [float("-inf")] * (T + 1)
    dp[0] = 0
    return dp

def gen_prev_time_indices(T, mise_time):
    return range(T - mise_time, -1, -1)

def get_fun_and_time(activity):
    return activity

def should_skip_time(new_time, T):
    return new_time > T

def should_skip_interval(prev_time, S, new_time):
    return prev_time < S < new_time

def update_new_time(prev_time, mise_time, S):
    return S + mise_time

def process_assignment(dp, new_time, new_fun):
    if new_fun > dp[new_time]:
        dp[new_time] = new_fun

def process_activity(activity, T, S, dp):
    fun, mise_time = get_fun_and_time(activity)
    prev_time_indices = gen_prev_time_indices(T, mise_time)
    for prev_time in prev_time_indices:
        from_fun = dp[prev_time]
        new_time = prev_time + mise_time
        new_fun = fun + from_fun
        if should_skip_interval(prev_time, S, new_time):
            new_time = update_new_time(prev_time, mise_time, S)
            if should_skip_time(new_time, T):
                continue
        if should_skip_time(new_time, T):
            continue
        process_assignment(dp, new_time, new_fun)

def solve():
    N, T, S, a = read_input()
    dp = initialize_dp(T)
    for activity in a:
        process_activity(activity, T, S, dp)
    print(max(dp))

if __name__ == "__main__":
    solve()