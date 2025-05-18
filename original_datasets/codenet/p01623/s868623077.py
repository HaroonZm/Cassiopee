class UnionFind:
    def __init__(self, size):
        self.table = [-1] * size
    
    def find(self, x):
        while self.table[x] >= 0:
            x = self.table[x]
        return x
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.table[x_root] < self.table[y_root]:
                self.table[x_root] += self.table[y_root]
                self.table[y_root] = x_root
            else:
                self.table[y_root] += self.table[x_root]
                self.table[x_root] = y_root
    
    def isDisjoint(self, x, y):
        return self.find(x) != self.find(y)

def solve():
    import sys
    input_lines = sys.stdin.readlines()
    from bisect import bisect_left
    from itertools import filterfalse
    
    while True:
        N, M = map(int, input_lines[0].split())
        if N == 0 and M == 0:
            break
        
        h = map(int, input_lines[1:1+N])
        h = list(zip(h, range(1, 1 + N)))
        h.sort()
        rm_days, islands = zip(*h)
        
        bridges = [tuple(map(int, l.split())) for l in input_lines[1+N:1+N+M]]
        bridges.sort(key=lambda x: x[2])
        
        S = UnionFind(N + 1)
        cost = 0
        i = N
        mst_flag = True
        target_bridges = bridges.copy()
        while i > 0:
            if mst_flag:
                i -= 1
                i = bisect_left(rm_days, rm_days[i])
                unsunk_islands = islands[i:]
                
                f = lambda x: x[0] in unsunk_islands and x[1] in unsunk_islands
                target_bridges = filter(f, bridges)
                
                # Number of required bridges
                bridge_num = len(unsunk_islands) - 1
                cnt = 0
                # Kruskal's algorithm
                for bridge in target_bridges:
                    a, b, c = bridge
                    if S.isDisjoint(a, b):
                        S.union(a, b)
                        cost += c
                        cnt += 1
                        if cnt == bridge_num:
                            mst_flag = False
                            break
                else:
                    mst_flag = True
                    S = UnionFind(N + 1)
                    cost = 0
            else:
                j = i
                i -= 1
                i = bisect_left(rm_days, rm_days[i])
                present_islands = islands[i:]
                unsunk_islands = islands[j:]
                
                f = lambda x: x[0] in present_islands and x[1] in present_islands
                target_bridges = filter(f, bridges)
                f = lambda x: x[0] in unsunk_islands and x[1] in unsunk_islands
                target_bridges = filterfalse(f, target_bridges)
                
                # Number of required bridges
                bridge_num = j - i
                cnt = 0
                # Kruskal's algorithm
                for bridge in target_bridges:
                    a, b, c = bridge
                    if S.isDisjoint(a, b):
                        S.union(a, b)
                        cost += c
                        cnt += 1
                        if cnt == bridge_num:
                            break
                else:
                    mst_flag = True
                    S = UnionFind(N + 1)
                    cost = 0
        
        if -N in S.table:
            print(cost)
        else:
            print(0)
            
        del input_lines[:N+1+M]

solve()