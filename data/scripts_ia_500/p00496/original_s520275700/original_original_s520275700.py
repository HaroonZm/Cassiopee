def solve():
    N, T, S = map(int, input().split())
    a = [tuple(map(int, input().split())) for _ in [0]*N]
    dp = [float("-inf")]*(T+1)
    dp[0] = 0

    for fun, mise_time in a:
        for prev_time, from_fun, to_fun in zip(range(T-mise_time, -1, -1), dp[T-mise_time::-1], dp[::-1]):
            new_time = prev_time + mise_time
            new_fun = fun + from_fun
            if prev_time < S < new_time:
                new_time = S + mise_time
                if new_time > T:
                    continue
                to_fun = dp[new_time]
            if new_fun > to_fun:
                dp[new_time] = new_fun

    print(max(dp))

if __name__ == "__main__":
    solve()