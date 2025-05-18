import sys
printn = lambda x: sys.stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True # and False

def ddprint(x):
  if DBG:
    print(x)

n,m = inm()
a = inl()
h = {}
h[0] = 1
acc = [0]*(n+1)
for i in range(n):
    acc[i+1] = x = (acc[i]+a[i])%m
    if x in h:
        h[x] += 1
    else:
        h[x] = 1
sm = 0
for x in h:
    sm += h[x]*(h[x]-1)//2
print(sm)