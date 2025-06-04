import sys
sys.setrecursionlimit(50000)

def suite(n):
    memo = [0] * (n+1)
    def calc(k):
        if k == 0:
            return 2
        if k == 1:
            return 1
        if memo[k] != 0:
            return memo[k]
        result = calc(k-1) + calc(k-2)
        memo[k] = result
        return result
    return calc(n)

nombre = int(input())
print(suite(nombre))