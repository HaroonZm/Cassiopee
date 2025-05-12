class PotUnionFind:
    def __init__(self, size):
        self.parent = [-1 for i in range(size)]#非負なら親ノード，負ならグループの要素数
        self.diff_p = [0 for i in range(size)]#親ノードを基準としたポテンシャル

    def root(self, x): #root(x): xの根ノードを返す
        if self.parent[x] < 0:
            return x
        else:
            rx = self.root(self.parent[x]) #xをxの根rxに直接つなぎたい
            self.diff_p[x] += self.diff_p[self.parent[x]] #そのために，diff(rx,x)を計算
            self.parent[x] = rx #xをrxに直接つなげる
            return rx

    def merge(self, x, y, dxy): #ポテンシャル差の条件p(y)-p(x)=dxyでxとyのグループをまとめる
        dxy = self.diff_p[x] + dxy - self.diff_p[y] #dxyをdiff(rx,ry)で置き換え
        x = self.root(x) #rxを新たにxと名づける
        y = self.root(y) #ryを新たにyと名づける
        if x == y:
            return False
        if self.parent[x] > self.parent[y]: #xの要素数がyの要素数より「小さい」とき入れ替える
            x,y=y,x
            dxy = -dxy
        self.parent[x] += self.parent[y] #xの要素数を更新
        self.parent[y] = x #yをxにつなぐ
        self.diff_p[y] = dxy #yの相対ポテンシャルを更新
        return True

    def issame(self, x, y): #issame(x,y): xとyが同じグループにあるならTrue
        return self.root(x) == self.root(y)
        
    def diff(self,x,y): #diff(x,y): xを基準としたyのポテンシャルを返す 
        if self.root(x) == self.root(y): #この時点でxの親はroot(x)
            return self.diff_p[y] - self.diff_p[x]
        else:
            return None

    def size(self,x): #size(x): xのいるグループの要素数を返す
        return -self.parent[self.root(x)]
#>>>>>>>>>>>>>>EhdCutHere>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n,m = list(map(int,input().split()))

uf = PotUnionFind(n)
ans = True
for i in range(m):
    l,r,d=list(map(int,input().split()))
    l-=1;r-=1;
    if uf.issame(l,r):
        ans = d==uf.diff(l,r)
    else:
        uf.merge(l,r,d)
    if ans == False:
        break

if ans == False:
    print('No')
else:
    print('Yes')
#print([uf.root(i) for i in range(n)])
#print([uf.parent[i] for i in range(n)])
#print([uf.size(i) for i in range(n)])