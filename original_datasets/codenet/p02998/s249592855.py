import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    ################
    class UnionFind():
        """
        parents : 親要素(findしない場合は根ではないことの注意)，根の場合は"-(要素数）"
        find(x):要素xの属するグループの根を返す
        size(x):要素xの属するグループの要素数を返す
        same(x,y):x,yが同じグループに属しているか返す
        重いかも！　　members(x):要素xが属するグループに属する要素をリストで返す
        roots:全ての根の要素を返す
        group_count():グループの数を返す
        重いかも！　all_group_members():{根要素：[そのグループに含まれる要素のリスト]}の辞書を返す
        """
        def __init__(self, n):
            self.n = n
            self.parents = [-1] * n

        def find(self, x):
            #根を探す&つなぎかえる
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)

            if x == y:
                return

            if self.parents[x] > self.parents[y]:
                x, y = y, x

            self.parents[x] += self.parents[y]
            self.parents[y] = x

        def size(self, x):
            return -self.parents[self.find(x)]

        def same(self, x, y):
            return self.find(x) == self.find(y)

        def members(self, x):
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]

        def group_count(self):
            return len(self.roots())

        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}

        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
        
    ################

    """
    解説放送のように，グラフを考える．
    X座標を表す点を10**5個
    Y座標を表す点を10**5個用意．
    座標を点，点をグラフの辺として表す
    """

    N=I()
    M=10**5
    XY=[0]*(2*M)
    uf=UnionFind(2*M)
    for i in range(N):
        x,y=MI()
        x-=1
        y-=1
        y+=M
        XY[x]+=1
        XY[y]+=1
        uf.union(x,y)
    
    #　各根要素に対して，xの要素数，yの要素数，入出する辺の本数をメモ
    from collections import defaultdict
    ddx = defaultdict(int)
    ddy = defaultdict(int)
    dde = defaultdict(int)
    
    for i in range(2*M):
        root=uf.find(i)
        if i<M:
            ddx[root]+=1
        else:
            ddy[root]+=1
        dde[root]+=XY[i]
        
    ans=0
    
    for k,v in dde.items():
        temp=ddx[k]*ddy[k]-v//2
        ans+=temp
        
    print(ans)
    
    
    

main()