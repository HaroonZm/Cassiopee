N = int(input())
A = list(map(int, input().split()))

def compute_total(a):
    res = 0
    idx = 0
    while idx < len(a):
        res += a[idx]
        idx += 1
    return res

def triangular(n): return (n * (n + 1)) // 2

class Result:
    def __init__(self, n, arr):
        self.val = None
        temp_sum = compute_total(arr)
        t_sum = triangular(n)
        self.val = temp_sum - t_sum

    def out(self): print(self.val)

res = Result(N, A)
res.out()