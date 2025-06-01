def solve(prob_num, max_pos, special_count, steps, flags, adjust):
    dp = [[0.0 for _ in range(6001)] for __ in range(max_pos + 11)]
    dp[0][0] = 1.0
    for pos in range(max_pos):
        for val in range(5001):
            if dp[pos][val] == 0.0:
                continue
            for step in steps:
                new_pos = pos + step
                if new_pos > max_pos:
                    dp[max_pos][val] += dp[pos][val] / prob_num
                elif flags[new_pos] == 1:
                    dp[min(max_pos, new_pos + adjust[new_pos])][val] += dp[pos][val] / prob_num
                else:
                    new_val = val + adjust[new_pos]
                    if new_val < 0:
                        new_val = 0
                    dp[new_pos][new_val] += dp[pos][val] / prob_num
    total = 0
    for v in range(5001):
        total += v * dp[max_pos][v]
    print(int(total))


if __name__ == "__main__":
    import sys

    while True:
        # read the inputs
        X, Y, Z = map(int, input().split())
        if X == 0 and Y == 0 and Z == 0:
            break  # no more data, exit
        V = list(map(int, input().split()))
        E = [0]*100
        A = [0]*100
        for _ in range(Z):
            n, e, a = map(int, input().split())
            E[n] = e
            if e == 3:
                A[n] = -a  # some penalty maybe
            else:
                A[n] = a  # bonus or something
        solve(X, Y, Z, V, E, A)