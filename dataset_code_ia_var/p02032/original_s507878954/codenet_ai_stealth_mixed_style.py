import sys
sys.setrecursionlimit(10**5+10)
from math import sqrt, floor

input = lambda: sys.stdin.readline().strip()

def solveN(n):
    def sievePr(num):
        if num < 2: return []
        arr = [1 if i > 1 else 0 for i in range(num + 1)]
        arr[0], arr[1] = 0, 0
        for i in range(2, int(sqrt(num)) + 1):
            if arr[i]:
                k = i * 2
                while k <= num:
                    arr[k] = 0
                    k += i
        return [i for i, x in enumerate(arr) if x]

    def pfact(num, res=None):
        if res is None: res = {}
        if num < 2: return None
        for p in sievePr(floor(sqrt(num))):
            while not num % p:
                res[p] = res.get(p, 0) + 1
                num //= p
        if num > 1:
            res[num] = res.get(num, 0) + 1
        return res

    dic = pfact(n) or {}
    x = 1
    for i in dic.values():
        x *= (i + 1)
    print(len(dic), x - 1)

def MAIN():
    n = int(input())
    solveN(n)

MAIN()