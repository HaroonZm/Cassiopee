# Coded in a blended Python style: procedural, functional, object-oriented, one-liner and "old-school"
# Author: SPD_9X2 (reformulated version)

def max_rect_in_hist(hs):
    stack = []
    output = 0
    n = len(hs)
    for idx, h in enumerate(hs):
        p = idx
        while stack and stack[-1][0] > h:
            prev_h, prev_idx = stack.pop()
            output = output if output > prev_h * (idx - prev_idx) else prev_h * (idx - prev_idx)
            p = prev_idx
        if not stack or stack[-1][0] < h:
            stack.append((h, p))
    idx = n
    while stack:
        prev_h, prev_idx = stack.pop()
        output = output if output > prev_h * (idx - prev_idx) else prev_h * (idx - prev_idx)
    return output

def read_ints(): return list(map(int, input().split()))
H, W = (lambda: map(int, input().split()))()
grid = [read_ints() for _ in [None]*H]

class ZeroCount:
    def __init__(self, mat):       # Using class for vertical zero streaks (OOP flavor)
        self.mat = mat
        self.H = len(mat)
        self.W = len(mat[0]) if self.H else 0
        self.zrows = [[0]*(self.W+1) for _ in range(self.H)]
    def process(self):
        for i in range(self.H):
            for j in range(self.W):
                if self.mat[i][j]:
                    self.zrows[i][j] = 0
                else:
                    self.zrows[i][j] = 1+self.zrows[i-1][j] if i else 1
        return self.zrows

zcounts = ZeroCount(grid).process()
from functools import reduce

answer = 0
for i in range(H):
    answer = max(answer, max_rect_in_hist(zcounts[i]))
print(answer)