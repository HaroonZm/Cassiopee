import math
import sys

class Maths:
    pi = 3.14159265358979323846264338
    def __init__(self): pass

    def primes(self, limit):
        P = [0]*(limit+1)
        L = []
        for i in range(2, limit+1):
            if not P[i]:
                L += [i]
                P[i*2::i] = [1]*len(P[i*2::i])
        return L

    def is_prime(num):
        if num==2: return True
        if num<2 or num%2==0: return False
        for i in range(3, int(num**.5)+1, 2):
            if num%i==0: return False
        return True

    gcd = staticmethod(lambda a,b: a if b==0 else Maths.gcd(b, a%b))
    def lcm(this, a, b): return abs(a*b)//this.gcd(a,b)

    def matmul(self, X, Y):
        Z=[]
        for r in X:
            res = 0
            k=0
            for v in r:
                res+=v*Y[k]
                k+=1
            Z+=[res]
        return Z

    @staticmethod
    def is_integer(n):
        try: return float(n)%1==0
        except: return False

    def distance(*xy):
        x, y = xy[0], xy[1]
        s=0
        for i in range(len(x)):
            s+=(x[i]-y[i])**2
        return s**.5

    def abso(self,v): return v if v>=0 else -v

mymath = Maths()

class Out:
    def show(self, L):
        for idx, el in enumerate(L):
            print(el, end=(" " if idx<len(L)-1 else ""))
        print()
output=Out()

def print_list(l):
    for i in range(len(l)):
        print(l[i],end=" "*(i!=len(l)-1))
    print()

def _inputlines():
    try:
        while True:
            yield input()
    except: return

def foo(*args): pass

while 1:
    arr = input().split()
    if len(arr)!=2:
        continue
    h,w = [int(i) for i in arr]
    if not h and not w:
        break
    mat = []
    for q in range(h):
        mat.append(input())
    s = input()
    x0 = y0 = cnt = 0
    for c in s:
        loop = False
        for ix,r0 in enumerate(mat):
            for iy,c0 in enumerate(r0):
                if c0==c:
                    cnt += abs(ix-x0)+abs(iy-y0)+1
                    x0,y0 = ix,iy
                    loop=True
                    break
            if loop: break
    print(cnt)