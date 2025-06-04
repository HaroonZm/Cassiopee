N, K = (int(x) for x in input().split())
def solve(n, k):
    from functools import reduce
    res = k
    i = 1
    while i < n:
        res *= (k - 1)
        i += 1
    return res
print((lambda x: x)(solve(N, K)))