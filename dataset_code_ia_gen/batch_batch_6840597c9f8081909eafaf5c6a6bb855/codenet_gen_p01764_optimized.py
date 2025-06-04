def calc_time(x, y, c_prev):
    res = 0
    c = 0
    while x > 0 or y > 0 or c != 0:
        xi = x % 10
        yi = y % 10
        t = xi * yi + c
        res += t
        c = 1 if (xi + yi + c_prev) >= 10 else 0
        x //= 10
        y //= 10
        c_prev = c
    return res

def min_time_sum(a):
    n = len(a)
    from functools import lru_cache
    import sys
    sys.setrecursionlimit(10**7)

    @lru_cache(None)
    def dp(l, r):
        if l == r:
            return 0, a[l]
        res = 10**15
        val = 0
        for m in range(l, r):
            left_time, left_val = dp(l, m)
            right_time, right_val = dp(m+1, r)
            c0 = 0
            temp_time = left_time + right_time + calc_time(left_val, right_val, c0)
            if temp_time < res:
                res = temp_time
                val = left_val + right_val
        return res, val

    return dp(0, n-1)[0]

n=int(input())
a=list(map(int,input().split()))
print(min_time_sum(a))