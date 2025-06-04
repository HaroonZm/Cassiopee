def solve():
    t = int(input())
    while t>0:
        t-=1
        n = int(input())
        A = [int(x) for x in input().split()]
        def process(L):
            s = 0
            m = None
            M = float('-inf')
            for idx in range(len(L)-1):
                diff = L[idx+1] - L[idx]
                if m is None or diff < m: m = diff
                if diff > M: M = diff
            return (M, -m)
        ans = process(A)
        print(ans[0], ans[1])
solve()