from sys import stdin

def max_subarray_sum(arr):
    max_sum = current_sum = float('-inf')
    for x in arr:
        current_sum = max(x, current_sum + x if current_sum != float('-inf') else x)
        max_sum = max(max_sum, current_sum)
    return max_sum

def x(a):
    n = len(a)
    m = float('-inf')
    for c in range(n):
        p = [0] * n
        for e in range(c, n):
            for r, val in enumerate(a):
                p[r] += val[e]
            m = max(m, max_subarray_sum(p))
    return m

n = int(stdin.readline())
a = [list(map(int, stdin.readline().split())) for _ in range(n)]
print(x(a))