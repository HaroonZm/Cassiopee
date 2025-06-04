import sys
input = sys.stdin.readline

n = int(input())
phrases = [tuple(map(int, input().split())) for _ in range(n)]
m = int(input())
melodies = [int(input()) for _ in range(m)]

MAX_LEN = 393

# dp[i] = maximum score to fill length i exactly, -inf if impossible
dp = [-10**9] * (MAX_LEN + 1)
dp[0] = 0

for i in range(1, MAX_LEN + 1):
    for s, l, p in phrases:
        if i - s < 0:
            continue
        start = max(0, i - l)
        for length_start in range(start, i - s + 1):
            if dp[length_start] < 0:
                continue
            # length i - length_start is used for this phrase (between s and l)
            if s <= i - length_start <= l:
                dp[i] = max(dp[i], dp[length_start] + p)

for w in melodies:
    if dp[w] < 0:
        print(-1)
        exit()

for w in melodies:
    print(dp[w])