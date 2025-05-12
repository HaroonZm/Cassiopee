import sys
input = lambda : sys.stdin.readline().strip()

from collections import deque

class Convex_Hull_Trick():
    def __init__(self):
        self.que = deque()

    @staticmethod
    def check(f1, f2, f3):
        return (f2[0] - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])

    @staticmethod
    def f(f1, x):
        return f1[0]*x + f1[1]

    def add_line(self, a, b):
        fi = (a, b)
        while len(self.que) >= 2 and self.check(self.que[-2], self.que[-1], fi):
            self.que.pop()
        self.que.append(fi)

    def query(self, x):
        while len(self.que) >= 2 and self.f(self.que[0], x) >= self.f(self.que[1], x):
            self.que.popleft()
        return self.f(self.que[0], x)

n,c = map(int, input().split())
h = list(map(int, input().split()))

CHT = Convex_Hull_Trick()
CHT.add_line(-2*h[0], h[0]**2)

DP = [0]*n

for i in range(1, n):
    min_cost = CHT.query(h[i])
    DP[i] = min_cost + h[i]*h[i] + c
    CHT.add_line(-2*h[i], h[i]**2+DP[i])

print(DP[-1])