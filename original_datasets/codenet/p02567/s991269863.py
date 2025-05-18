import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

### セグメント木

class SegmentTree:
    def __init__(self, n, a=None):
        """初期化
        num : n以上の最小の2のべき乗
        """
        num = 1
        while num<=n:
            num *= 2
        self.num = num
        self.seg = [0] * (2*self.num-1)
        if a is not None:
            # O(n)で初期化
            assert len(a)==n
            for i in range(n):
                self.seg[num-1+i] = a[i]
            for k in range(num-2, -1, -1):
                self.seg[k] = max(self.seg[2*k+1], self.seg[2*k+2])
    def update(self,i,x):
        """update(i,x):Aiをxに更新する
        """
        k = i+(self.num-1)
        self.seg[k] = x
        k = (k-1)//2
        while k >= 0:
            self.seg[k] = max(self.seg[2*k+1], self.seg[2*k+2])
            k = (k-1)//2
    def query(self,a,b):
        k = 0
        l = 0
        r = self.num
        q = [(k,l,r)]
        ans = -float("inf")
        while q:
            k,l,r = q.pop()
            if r<=a or b<=l:
                pass
            elif a<=l and r<=b:
                ans = max(ans, self.seg[k])
            else:
                q.append((2*k+1,l,(l+r)//2))
                q.append((2*k+2,(l+r)//2,r)) 
        return ans
    # def find_right(self,a,b,x):
    #     """[a,b)で値がx以上のインデックスの最大
    #     """
    # def find_right(self,a,b,x):
    #     """[a,b)で値がx以上のインデックスの最大
    #     """
    #     return self._find_right(a,b,x,k=0,l=0,r=self.num)
    # def _find_right(self,a,b,x,k,l,r):
    #     if self.seg[k]<x or r<=a or b<=l: # x以上を満たせない or 区間が重複しない
    #         return -1
    #     elif k>=self.num-1: # 自身が葉
    #         return k - (self.num-1)
    #     else:
    #         vr = self._find_right(a,b,x,2*k+2,(l+r)//2,r)
    #         if vr>=0:
    #             return vr
    #         else:
    #             return self._find_right(a,b,x,2*k+1,l,(l+r)//2)
    def find_left(self,a,b,x):
        """[a,b)で値がx以上のインデックス(0,1,...,self.num-1)の最小
        条件を満たすものが存在しないとき、self.numを返す
        """
        k = 0
        l = 0
        r = self.num
        q = [(k,l,r,True)] # 行きがけかどうか
        ans = self.num
        while q:
            k,l,r,b = q.pop()
            if b:
                if self.seg[k]<x or r<=a or b<=l: # x以上を満たせない or 区間が重複しない
                    pass
                elif k>=self.num-1: # 自身が葉
                    ans = min(ans, k - (self.num-1))
                    return ans
                else:
                    # 右への探索を予約
                    q.append((2*k+2,(l+r)//2,r,False))
                    # 左への探索
                    q.append((2*k+1,l,(l+r)//2,True))
            else:
                if ans<self.num:
                    return ans
                q.append((k+1,r,2*r-l,True))
        return ans
    def find_left(self,a,b,x):
        """[a,b)で値がx以上のインデックスの最小
        """
        return self._find_left(a,b,x,k=0,l=0,r=self.num)
    def _find_left(self,a,b,x,k,l,r):
        if self.seg[k]<x or r<=a or b<=l: # x以上を満たせない or 区間が重複しない
            return self.num
        elif k>=self.num-1: # 自身が葉
            return k - (self.num-1)
        else:
            vl = self._find_left(a,b,x,2*k+1,l,(l+r)//2)
            if vl<self.num:
                return vl
            else:
                return self._find_left(a,b,x,2*k+2,(l+r)//2,r)
    def query_index(self,a,b,k=0,l=0,r=None):
        """query(a,b,0,0,num):[a,b)の最大値
        最大値を与えるインデックスも返す
        """
        if r is None:
            r = self.num
        if r <= a or b <= l:
            return (-float("inf"), None)
        elif a <= l and r <= b:
            return (self.seg[k], self._index(k))
        else:
            return max(self.query_index(a,b,2*k+1,l,(l+r)//2),self.query_index(a,b,2*k+2,(l+r)//2,r))
    def _index(self, k):
        if k>=self.num:
            return k - (self.num-1)
        else:
            if self.seg[2*k+1]>=self.seg[2*k+2]:
                return self._index(2*k+1)
            else:
                return self._index(2*k+2)
n,q = list(map(int, input().split()))
a = list(map(int, input().split()))
sg = SegmentTree(n, a)
for _ in range(q):
    t,x,y = map(int, input().split())
    if t==1:
        sg.update(x-1,y)
    elif t==2:
        print(sg.query(x-1,y))
    else:
        res = sg.find_left(x-1,n,y)+1
        if res>=n+1:
            print(n+1)
        else:
            print(res)