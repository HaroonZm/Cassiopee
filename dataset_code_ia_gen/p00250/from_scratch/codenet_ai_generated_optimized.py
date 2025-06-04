import sys

def max_remainder(n, m, K):
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + K[i]
    max_mod = 0
    left = 0
    for right in range(1, n+1):
        while left < right and prefix[right] - prefix[left] >= m:
            left += 1
        # check subarray [left-1,right-1] if left>0
        if left>0:
            val = (prefix[right] - prefix[left-1]) % m
            if val > max_mod:
                max_mod = val
        val = (prefix[right] - prefix[left]) % m
        if val > max_mod:
            max_mod = val
    return max_mod

input = sys.stdin.readline
while True:
    line = input()
    if not line:
        break
    n,m = map(int, line.split())
    if n == 0 and m == 0:
        break
    K = list(map(int, input().split()))
    print(max_remainder(n, m, K))