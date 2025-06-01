class DFS:
    def __init__(self, bolls):
        self.bolls = bolls
        self.possible = False

    def search(self, left, right, remaining):
        if len(remaining) == 0:
            self.possible = True
            return
        boll = remaining[0]
        if boll > max(left):
            self.search(left + [boll], right, remaining[1:])
        if boll > max(right):
            self.search(left, right + [boll], remaining[1:])

    def run(self):
        self.search([-1], [-1], self.bolls)

N = int(input())
for _ in range(N):
    bolls = list(map(int, input().split()))
    dfs = DFS(bolls)
    dfs.run()
    if dfs.possible:
        print("YES")
    else:
        print("NO")