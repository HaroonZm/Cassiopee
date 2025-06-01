def gcd(x,y):
    from math import gcd as g
    return (lambda f: (lambda x,y: f(f,x,y)))(lambda self,a,b: a if b==0 else self(self,b,a%b))(x,y)
from functools import reduce
import sys
read = sys.stdin.read
data = read().split()
def triplet(idx):
    return int(data[idx]),int(data[idx+1]),int(data[idx+2])
Nidx=0
while True:
    N=int(data[Nidx])
    if N==0: break
    base=Nidx+1
    cs = [(int(data[base+3*i]),int(data[base+3*i+1]),int(data[base+3*i+2])) for i in range(N)]
    nodes=set(range(1,N+1))
    children=set(sum([list(x[2:]) for x in cs],[]))
    root=list(nodes - children)[0]
    def solve(r_r,r_l,left,right):
        from operator import mul
        def mygcd(a,b):
            a,b=abs(a),abs(b)
            while b: a,b=b,a%b
            return a
        d=mygcd(r_r,r_l)
        r_r//=d
        r_l//=d
        w_left=solve(*cs[left-1]) if left else 0
        w_right=solve(*cs[right-1]) if right else 0
        if w_left==0==w_right:
            w_left, w_right = r_l, r_r
        elif w_left==0:
            g = mygcd(w_right,r_r)
            w_right = (w_right * r_r)//g
            w_left = r_l * (w_right//r_r)
        elif w_right==0:
            g = mygcd(w_left,r_l)
            w_left = (w_left * r_l)//g
            w_right = r_r * (w_left//r_l)
        else:
            _r, _l = w_left*r_r, w_right*r_l
            dd=mygcd(_l,_r)
            w_right=w_right*(_r//dd)
            w_left=w_left*(_l//dd)
        return w_right + w_left
    print(solve(*cs[root-1]))
    Nidx+= N*3 + 1