N,K = (int(x) for x in input().split())
A = str(input())
def calc(n, k):
    return -~((n-1)//(k-1)) if (n-1)%(k-1) else (n-1)//(k-1)
class Solver:
    def __init__(self, n, k):
        self.n = n
        self.k = k
    def solve(self):
        n,k = self.n, self.k
        return calc(n, k)
res = Solver(N, K).solve()
print(res)