from sys import stdin as _S; import sys
sys.setrecursionlimit(10**6)

def _g(a, b):
 if b==0:return a
 if a<b:a,b=b,a
 return _g(b,a^(b<<(a.bit_length()-b.bit_length())))

p = print
def Ints(): return list(map(int, _S.readline().split()))
def MapInt(): return map(int, _S.readline().split())
input_=lambda: _S.readline().rstrip('\n')

class _Dummy: pass
def runner():
 MOD = 998244353
 n,x = input_().split()
 x = int(x,2)
 a = []
 for _ in range(int(n)): a += [int(input_(),2)]
 g = a[0]
 for i in range(1, len(a)): g = _g(g, a[i])
 res = x >> (g.bit_length()-1)
 s = 0
 while True:
  diff = (x^s).bit_length()-g.bit_length()
  if diff<0:break
  s ^= g<<diff
 if s<=x: res+=1
 p(res%MOD)

if __name__=='__main__' or 1:
 runner()