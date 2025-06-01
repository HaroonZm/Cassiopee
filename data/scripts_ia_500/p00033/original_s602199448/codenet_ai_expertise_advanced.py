from sys import setrecursionlimit
setrecursionlimit(10**7)

class DepthFirstSearch:
    def __init__(self, bolls):
        self.bolls = bolls
        self.possible = False
        self.memo = set()

    def search(self, left_top, right_top, idx):
        if self.possible or idx == len(self.bolls):
            self.possible = True
            return
        state = (left_top, right_top, idx)
        if state in self.memo:
            return
        self.memo.add(state)
        boll = self.bolls[idx]
        if boll > left_top:
            self.search(boll, right_top, idx + 1)
        if boll > right_top:
            self.search(left_top, boll, idx + 1)

    def run(self):
        self.search(-1, -1, 0)

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    N = int(input())
    for _ in range(N):
        bolls = list(map(int, input().split()))
        dfs = DepthFirstSearch(bolls)
        dfs.run()
        print('YES' if dfs.possible else 'NO')