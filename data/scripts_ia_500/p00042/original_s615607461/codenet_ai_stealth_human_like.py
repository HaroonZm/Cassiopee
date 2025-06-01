counter = 0
while True:
    line = input()
    if line == '0':
        break
    counter += 1
    capacity = int(line)
    dp = [0] * (capacity + 1)
    n = int(input())
    for _ in range(n):
        val_str = input()
        val, weight = map(int, val_str.split(','))
        for cap in range(capacity, weight - 1, -1):
            if dp[cap] < dp[cap - weight] + val:
                dp[cap] = dp[cap - weight] + val
    # looking for minimal capacity that achieves max value
    for cap in range(capacity + 1):
        if dp[capacity] == dp[cap]:
            print(f'Case {counter}:\n{dp[capacity]}\n{cap}')
            break