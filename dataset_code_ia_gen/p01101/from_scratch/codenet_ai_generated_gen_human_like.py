import sys

def find_best_pair(prices, m):
    prices.sort()
    left, right = 0, len(prices) - 1
    best_sum = -1
    while left < right:
        s = prices[left] + prices[right]
        if s > m:
            right -= 1
        else:
            if s > best_sum:
                best_sum = s
            left += 1
    return best_sum

for line in sys.stdin:
    if line.strip() == '':
        continue
    n, m = map(int, line.split())
    if n == 0 and m == 0:
        break
    prices = list(map(int, sys.stdin.readline().split()))
    result = find_best_pair(prices, m)
    if result == -1:
        print("NONE")
    else:
        print(result)