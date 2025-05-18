class PotUnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) #親ノード
        self.size = [1]*n #グループの要素数
        self.diff_p = [0]*n #親ノードを基準としたポテンシャル
 
    def root(self, x): #root(x): xの根ノードを返す．
        while self.parent[x] != x:
            self.diff_p[x] += self.diff_p[self.parent[x]]
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x 

    def weight(self, x): #root(x): xの根ノードを返す．
        c=0
        while self.parent[x] != x:
            self.diff_p[x] += self.diff_p[self.parent[x]]
            self.parent[x] = self.parent[self.parent[x]]
            c += self.diff_p[x]
            x = self.parent[x]
        return c

    def merge(self, x, y, dxy): #ポテンシャル差p(y)-p(x)=dxyでxとyの組をまとめる
        dxy += self.weight(x) - self.weight(y) #dxyをで置き換え
        x,y = self.root(x), self.root(y)
        if x == y: return False
        if self.size[x] < self.size[y]: #xの要素数が大きいように
            x,y,dxy = y,x,-dxy
        self.size[x] += self.size[y] #xの要素数を更新
        self.parent[y] = x #yをxにつなぐ
        self.diff_p[y] = dxy #yの相対ポテンシャルを更新
        return True
 
    def issame(self, x, y): #xとyが同じ組ならTrue
        return self.root(x) == self.root(y)
        
    def diff(self,x,y): #xを基準としたyのポテンシャルを返す 
        if self.root(x) == self.root(y):
            return self.weight(y) - self.weight(x)
        else:
            return None

    def getsize(self,x): #xのいるグループの要素数を返す
        return self.size[self.root(x)]

import sys
while True:
    n,Q=[int(i) for i in input().split()]
    if n==0 and Q ==0: exit()
    T=PotUnionFind(n)
    for _ in [0]*(Q):
        u = [i for i in sys.stdin.readline().split()]
        if u[0] =="!":
            u1, u2, u3 = int(u[1])-1, int(u[2])-1, int(u[3])
            T.merge(u1,u2,u3)
        else:
            u1, u2 = int(u[1])-1, int(u[2])-1
            if T.issame(u1,u2):
                print(T.diff(u1,u2))
            else:
                print("UNKNOWN")