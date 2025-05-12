class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)
    
    def Sum(self,i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    
    def add(self,i,x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

class RangeUpdate:
    def __init__(self, n):
        self.p = BIT(n+1)
        self.q = BIT(n+1)
        
    def add(self,s,t,x):
        t+=1
        self.p.add(s,-x*s)
        self.p.add(t,x*t)
        self.q.add(s,x)
        self.q.add(t,-x)
        
    def Sum(self,s,t):
        t+=1
        return self.p.Sum(t) + self.q.Sum(t)*t-self.p.Sum(s)-self.q.Sum(s)*s
    
n, q = map(int, input().split())
tree = RangeUpdate(n)
for _ in range(q):
    a, *b = map(int,input().split())
    if a == 0:
        tree.add(b[0],b[1],b[2])
    else:
        print(tree.Sum(b[0],b[1]))