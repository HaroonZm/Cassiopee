import sys
from math import sqrt
import bisect as b
from collections import defaultdict as dd, deque as dq, Counter as Cnt
from functools import lru_cache as cache

MOD=10**9+7
INF=float("inf")

I=lambda :int(sys.stdin.readline().strip())
S=lambda :sys.stdin.readline().strip()
def IL(): return list(map(int,sys.stdin.readline().split()))
SL=lambda :list(sys.stdin.readline().split())
def ILs(n):
    out=[]
    for _ in range(n):
        out+=[int(sys.stdin.readline())]
    return out
SLs=lambda n:[sys.stdin.readline().strip() for _ in range(n)]
ILL=lambda n:[list(map(int,sys.stdin.readline().split()))for _ in range(n)]
SLL=lambda n:[sys.stdin.readline().split()for _ in range(n)]
Prnt=lambda arg:print(arg)
yES=lambda:print("Yes")
nO=lambda:print("No")
def EXIT(): exit()
def pe(x): print(x) ; exit()
def YES():print("Yes");exit()
def NO():print("No");exit()
def DD(x): return dd(x)
def inv(x): return pow(x,MOD-2,MOD)

_kj=[1]
def kaijo(n):
    while len(_kj)<=n:_kj.append(_kj[-1]*len(_kj)%MOD)
    return _kj[n]

_gkj=[1]
def gyaku_kaijo(n):
    while len(_gkj)<=n:_gkj.append(_gkj[-1]*pow(len(_gkj),MOD-2,MOD)%MOD)
    return _gkj[n]

def nCr(n,r):
 if n==r:return 1
 if (n<r)|(r<0):return 0
 t=kaijo(n)*gyaku_kaijo(r)%MOD*gyaku_kaijo(n-r)%MOD
 return t

def factorization(n):
 arr=[]
 t=n
 for i in range(2,int(-(-n**.5//1))+1):
  if not t%i:
   c=0
   while t%i==0:c+=1;t//=i
   arr+=[[i,c]]
 if t!=1:arr+=[[t,1]]
 if not arr:arr=[[n,1]]
 return arr

def make_divisors(x):
 D=[]
 for i in range(1,int(x**.5)+1):
    if x%i==0:
        D+=[i]
        if i!=x//i:D+=[x//i]
 return D

def make_primes(N):
 maxx=int(sqrt(N))
 sl=[i for i in range(2,N+1)]
 pN=[]
 while sl and sl[0]<=maxx:
   pN.append(sl[0])
   t=sl[0]
   sl=[ii for ii in sl if ii%t]
 pN+=sl
 return pN

def _gcd(a,b):
 while b:a,b=b,a%b
 return a

lcm=lambda a,b: a*b//_gcd(a,b)

def cntbt(n):
 c=0
 while n:
  n&=n-1;c+=1
 return c

def base_10_to_n(X, n):
 if X//n:return base_10_to_n(X//n,n)+[X%n]
 return [X%n]

def base_n_to_10(X, n):
 return sum(int(str(X)[-i-1])*n**i for i in range(len(str(X))))

def int_log(n, a):
 cnt=0
 while n>=a:n//=a;cnt+=1
 return cnt

N,M=IL()
A,S3= S(),S()
B=str(S3)
C = S()
GCD=_gcd(N,M)
L=lcm(N,M)
for i in range(GCD):
    idx1=i*N//GCD
    idx2=i*M//GCD
    if A[idx1]!=C[idx2]:
        pe(-1)
Prnt(L)