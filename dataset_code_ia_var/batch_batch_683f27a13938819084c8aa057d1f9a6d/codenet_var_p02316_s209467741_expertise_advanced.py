from sys import maxsize

def main():
    N, W = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [-maxsize] * (W + 1)
    dp[0] = 0

    for weight in range(W):
        if dp[weight] == -maxsize:
            continue
        for value, w in items:
            next_weight = weight + w
            if next_weight <= W:
                dp[next_weight] = max(dp[next_weight], dp[weight] + value)

    print(max(dp))

if __name__ == "__main__":
    main()