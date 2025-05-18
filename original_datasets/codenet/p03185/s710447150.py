from collections import deque

def solve():
    class ConvexHullTrick:
        def __init__(self):
            self.LNows = deque()
            self.numL = 0

        def _isNotL2Min(self, L1, L2, L3):
            a1, b1 = L1
            a2, b2 = L2
            a3, b3 = L3
            return (a1-a2) * (b2-b3) >= (a2-a3) * (b1-b2)

        def _getY(self, L, x):
            a, b = L
            return a*x + b

        def addLine(self, L):
            while self.numL >= 2 and self._isNotL2Min(self.LNows[-2], self.LNows[-1], L):
                self.LNows.pop()
                self.numL -= 1
            self.LNows.append(L)
            self.numL += 1

        def getMin(self, x):
            y = self._getY(self.LNows[0], x)
            while self.numL >= 2:
                yNext = self._getY(self.LNows[1], x)
                if yNext > y: break
                y = yNext
                self.LNows.popleft()
                self.numL -= 1
            return y

    N, C = map(int, input().split())
    hs = list(map(int, input().split()))

    CHT = ConvexHullTrick()
    dp = [0] * N
    for i in range(1, N):
        CHT.addLine((-2*hs[i-1], dp[i-1] + hs[i-1]**2))
        minY = CHT.getMin(hs[i])
        dp[i] = minY + hs[i]**2 + C

    print(dp[-1])

solve()