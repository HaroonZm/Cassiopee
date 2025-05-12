import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

"""
TwoSat
"""

class SCC:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.graph_rev = [[] for _ in range(n)]
        self.already = [False]*n
    
    def add_edge(self, fr, to):
        if fr == to:
            return
        self.graph[fr].append(to)
        self.graph_rev[to].append(fr)
    
    def dfs(self, node, graph):
        self.already[node] = True
        for n in graph[node]:
            if self.already[n]:
                continue
            self.dfs(n, graph)
        self.order.append(node)
    
    def first_dfs(self):
        self.already = [False]*self.n
        self.order = []
        for i in range(self.n):
            if self.already[i] == False:
                self.dfs(i, self.graph)
    
    def second_dfs(self):
        self.already = [False]*self.n
        self.ans = []
        for n in reversed(self.order):
            if self.already[n]:
                continue
            self.already[n] = True
            self.order = []
            self.dfs(n, self.graph_rev)
            self.order.reverse()
            self.ans.append(self.order)

    def scc(self):
        self.first_dfs()
        self.second_dfs()
        return self.ans

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1]*(n+1)#それぞれの要素がどの要素の子であるか

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]#それぞれの要素の根を再帰的に求める

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        
        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)#x,yが同じ集合に属するかどうか
    
    def size(self, x):
        return -self.par[self.find(x)]
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if root == self.find(i)]        

class TwoSat:
    def __init__(self, n):
        self.n = n
        self.scc = SCC(n*2)
        self.union = UnionFind(n*2)
    
    def add_sat(self, fr, to):
        self.scc.add_edge(fr, to)
    
    def scc_prepare(self):
        return self.scc.scc()

    def union_prepare(self):
        for v in self.res:
            if len(v) == 1:
                continue
            for i in range(len(v)-1):
                self.union.union(v[i], v[i+1])
    
    def ts_judge(self):
        for i in range(self.n):
            if self.union.same(i, i+self.n):
                return False
        return True
    
    def judge(self):
        self.res = self.scc_prepare()
        self.union_prepare()
        res = self.ts_judge()
        return res

def main():
    n, d = map(int, input().split())

    ts = TwoSat(n*2)
    flag = [None]*n
    for i in range(n):
        x, y = map(int, input().split())
        flag[i] = (x, y)
    
    for i in range(n):
        ts.add_sat(n*3+i, i)
        ts.add_sat(n*2+i, n+i)

    for i in range(n):
        for j in range(i+1, n):
            if abs(flag[i][0] - flag[j][0]) < d:
                ts.add_sat(i, n*2+j)
                ts.add_sat(j, n*2+i)
                ts.add_sat(i, n+j)
                ts.add_sat(j, n+i)
            if abs(flag[i][0] - flag[j][1]) < d:
                ts.add_sat(i, j)
                ts.add_sat(i, n*3+j)
                ts.add_sat(n+j, n+i)
                ts.add_sat(n+j, n*2+i)
            if abs(flag[i][1] - flag[j][0]) < d:
                ts.add_sat(j, i)
                ts.add_sat(j, n*3+i)
                ts.add_sat(n+i, n+j)
                ts.add_sat(n+i, n*2+j)
            if abs(flag[i][1] - flag[j][1]) < d:
                ts.add_sat(i+n, j)
                ts.add_sat(i+n, j+n*3)
                ts.add_sat(j+n, i)
                ts.add_sat(j+n, i+n*3)
    
    ans = ts.judge()
    print("Yes" if ans else "No")
    if ans:
        used = [-1]*n
        count = 0
        for lis in reversed(ts.res):
            for v in lis:
                if v >= n*2:
                    continue
                index = v if v < n else v - n
                if used[index] == -1:
                    count += 1
                    used[index] = v//n
                if count == n:
                    break
        
        for i in range(n):
            print(flag[i][used[i]])

    

if __name__ == "__main__":
    main()