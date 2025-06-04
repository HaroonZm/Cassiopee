import sys
input=sys.stdin.readline
MAX=10**5
is_special=[False]*(MAX+1)
for m in range(2,MAX+1):
    exp=0
    x=m
    while x%2==0:
        x//=2
        exp+=1
    if x==1 and exp*2>=1:
        is_special[m]=True
pref=[0]*(MAX+1)
for i in range(2,MAX+1):
    pref[i]=pref[i-1]+is_special[i]
Q=int(input())
for _ in range(Q):
    N=int(input())
    print(pref[N])