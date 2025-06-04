import sys
input = sys.stdin.readline

def read_input():
    return list(map(int, input().split()))

def main():
    results = []
    while True:
        numbers = read_input()
        N = numbers[0]
        M = numbers[1]
        if N == 0 and M == 0:
            break
        C = []
        for i in range(M):
            C.append(int(input()))
        X = []
        for i in range(N):
            X.append(int(input()))

        dp = [float('inf')] * 256
        dp[128] = 0

        for xi in X:
            new_dp = [float('inf')] * 256
            for vol in range(256):
                if dp[vol] == float('inf'):
                    continue
                for delta in C:
                    next_vol = vol + delta
                    if next_vol < 0:
                        next_vol = 0
                    if next_vol > 255:
                        next_vol = 255
                    cost = (xi - next_vol) ** 2
                    if dp[vol] + cost < new_dp[next_vol]:
                        new_dp[next_vol] = dp[vol] + cost
            dp = new_dp
        min_cost = min(dp)
        results.append(min_cost)

    for r in results:
        print(r)

main()