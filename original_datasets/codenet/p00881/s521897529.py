from collections import Counter

while True:
    m, n = (int(s) for s in input().split())
    if not m:
        break

    objects = [int(input(), 2) for i in range(n)]
    dp = [bytearray(1 << m) for i in range(1 << m)]
    bits = [1 << i for i in range(m)]

    for mask in reversed(range((1 << m) - 1)):
        for masked, count in Counter(obj & mask for obj in objects).items():
            if count > 1:
                dp[mask][masked] = min(max(dp[mask + b][masked],
                                           dp[mask + b][masked + b]) + 1
                                       for b in bits if not b & mask)
    print(dp[0][0])