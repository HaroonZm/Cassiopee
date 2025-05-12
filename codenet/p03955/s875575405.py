import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
a = [LI() for i in range(3)]

A = []
B = []
c = 0
d = 0

for i in range(N):
    if i % 2 == 0:
        if a[0][i] % 6 == 1 and a[1][i] % 6 == 2 and a[2][i] % 6 == 3:
            A.append(a[1][i]//6)
        elif a[0][i] % 6 == 3 and a[1][i] % 6 == 2 and a[2][i] % 6 == 1:
            c += 1
            A.append(a[1][i]//6)
        else:
            print('No')
            exit()
    else:
        if a[0][i] % 6 == 4 and a[1][i] % 6 == 5 and a[2][i] % 6 == 0:
            B.append(a[1][i]//6)
        elif a[0][i] % 6 == 0 and a[1][i] % 6 == 5 and a[2][i] % 6 == 4:
            d += 1
            B.append(a[1][i]//6)
        else:
            print('No')
            exit()

class SegmentTree():
    def __init__(self,init_value,seg_func,unit_elt):
        n = len(init_value)
        self.seg_func = seg_func
        self.unit_elt = unit_elt
        self.num = 1 << (n-1).bit_length()  # n以上の最小2冪
        self.tree = [unit_elt]*(2*self.num)
        for i in range(n):
            self.tree[self.num + i] = init_value[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.seg_func(self.tree[2*i],self.tree[2*i+1])
    def update(self,i,x):  # i(0-index)番目の値をxに更新
         i += self.num
         self.tree[i] = x
         while i > 1:
             i >>= 1
             self.tree[i] = self.seg_func(self.tree[2*i],self.tree[2*i+1])
    def quary(self,p,q):  # [p,q)に関するseg_funcの結果を返す(p,qは0-index)
        p += self.num
        q += self.num
        res = self.unit_elt
        while p < q:
            if p & 1:
                res = self.seg_func(res,self.tree[p])
                p += 1
            if q & 1:
                res = self.seg_func(res,self.tree[q-1])
            p >>= 1
            q >>= 1
        return res

def seg_func(x,y):
    return x + y

seg1 = SegmentTree([0]*(len(A)),seg_func,unit_elt=0)
seg2 = SegmentTree([0]*(len(B)),seg_func,unit_elt=0)

a = 0  # Aの転倒数
for i in range(len(A)):
    a += i-seg1.quary(0,A[i])
    seg1.update(A[i],1)
b = 0  # Bの転倒数
for i in range(len(B)):
    b += i-seg2.quary(0,B[i])
    seg2.update(B[i],1)

if (a-d) % 2 == 0 and (b-c) % 2 == 0:
    print('Yes')
else:
    print('No')