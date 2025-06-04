import sys
import numpy as np

class Main:
    def solve(self):
        MAX_DIM = 151
        idx = np.arange(1, MAX_DIM)
        diag = np.empty((MAX_DIM, MAX_DIM), dtype=object)
        sq = np.square(idx)
        s = sq.reshape((-1,1)) + sq
        mask = np.triu(np.ones_like(s, dtype=bool), 1)
        diag[1:, 1:] = np.where(mask, s, None)
        stdin = sys.stdin
        while True:
            line = stdin.readline()
            if not line: break
            h, w = map(int, line.split())
            if not (h or w): break
            target = h * h + w * w
            valid = np.argwhere((diag[1:,1:] != None) & (diag[1:,1:] >= target))
            best = (float('inf'), float('inf'), float('inf'))
            for x, y in valid[::-1]:
                i, j = x+1, y+1
                val = diag[i, j]
                if val == target:
                    if h < i <= best[0]:
                        best = (i, j, val)
                elif best[2] == val:
                    if i < best[0]:
                        best = (i, j, val)
                elif best[2] > val:
                    best = (i, j, val)
            print(f"{best[0]} {best[1]}")
            
if __name__ == '__main__':
    Main().solve()