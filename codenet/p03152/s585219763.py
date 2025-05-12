#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def modinv2(x,r):
  return pow(x,r-2,r)

def perm(n,i):
    return (fact[n]*modinv2(fact[n-i],R))%R

n,m = inm()
a = inl()
b = inl()
fact = [0]*(n*m+1)
fact[0] = 1
for i in range(1,n*m+1):
    fact[i] = (fact[i-1]*i)%R
a.sort(reverse=True)
b.sort(reverse=True)
if a[0]!=n*m or b[0]!=n*m:
    print(0)
    exit()
prev = n*m
i = j = 1
x = 1
free = 0
while i<n or j<m:
    if i<n and (j==m or a[i]>b[j]):
        cur = a[i]
        use = prev-cur-1
        if use>free or use<0:
            print(0)
            exit()
        x = (x*perm(free,use)*j)%R
        free += j-1-use
        prev = cur
        i += 1
    elif j<m and (i==n or a[i]<b[j]):
        cur = b[j]
        use = prev-cur-1
        if use>free or use<0:
            print(0)
            exit()
        x = (x*perm(free,use)*i)%R
        free += i-1-use
        prev = cur
        j += 1
    elif i<n and j<m and a[i]==b[j]:
        cur = a[i]
        use = prev-cur-1
        if use>free or use<0:
            print(0)
            exit()
        x = (x*perm(free,use))%R
        free += i+j-use
        prev = cur
        i += 1
        j += 1
    #ddprint(f"{i=} {j=} {x=} {free=} {use=} {cur=}")
print((x*fact[prev-1])%R)