import sys
sys.setrecursionlimit(1000000)

class SCCGraph:
    def __init__(self, n):
        self.n = n
        self.graph = {}

    def num_vertices(self):
        return self.n

    def add_edge(self, frm, to):
        if frm in self.graph:
            self.graph[frm].append(to)
        else:
            self.graph[frm] = [to]

    def scc_ids(self):
        order = [-1] * self.n
        low = [0] * self.n
        ids = [0] * self.n
        stack = []
        now_ord = 0
        group_num = 0

        def dfs(v):
            nonlocal now_ord, group_num
            order[v] = now_ord
            low[v] = now_ord
            now_ord += 1
            stack.append(v)
            if v in self.graph:
                for to in self.graph[v]:
                    if order[to] == -1:
                        dfs(to)
                        low[v] = min(low[v], low[to])
                    else:
                        if order[to] < self.n:
                            low[v] = min(low[v], order[to])
            if low[v] == order[v]:
                while True:
                    u = stack.pop()
                    order[u] = self.n
                    ids[u] = group_num
                    if u == v:
                        break
                group_num += 1

        for i in range(self.n):
            if order[i] == -1:
                dfs(i)
        for i in range(self.n):
            ids[i] = group_num - 1 - ids[i]
        return group_num, ids

    def scc(self):
        group_num, ids = self.scc_ids()
        groups = [[] for _ in range(group_num)]
        for i in range(self.n):
            groups[ids[i]].append(i)
        return groups

class TwoSAT:
    def __init__(self, n):
        self.n = n
        self.answer = [False] * n
        self.scc = SCCGraph(2 * n)

    def add_clause(self, i, f, j, g):
        self.scc.add_edge(2 * i + (not f), 2 * j + (g))
        self.scc.add_edge(2 * j + (not g), 2 * i + (f))

    def satisfiable(self):
        group_num, ids = self.scc.scc_ids()
        for i in range(self.n):
            if ids[2 * i] == ids[2 * i + 1]:
                return False
            self.answer[i] = ids[2 * i] < ids[2 * i + 1]
        return True

    def get_answer(self):
        return self.answer

def main():
    input = sys.stdin.readline
    N, D = map(int, input().split())
    XY = []
    for _ in range(N):
        x, y = map(int, input().split())
        XY.append([x, y])

    ts = TwoSAT(N)

    for i in range(N):
        for j in range(i + 1, N):
            xi, yi = XY[i]
            xj, yj = XY[j]
            if abs(xi - xj) < D:
                ts.add_clause(i, False, j, False)
            if abs(xi - yj) < D:
                ts.add_clause(i, False, j, True)
            if abs(yi - xj) < D:
                ts.add_clause(i, True, j, False)
            if abs(yi - yj) < D:
                ts.add_clause(i, True, j, True)

    if not ts.satisfiable():
        print("No")
        return

    print("Yes")
    ans = ts.get_answer()
    for i in range(N):
        x, y = XY[i]
        if ans[i]:
            print(x)
        else:
            print(y)

main()