try:
    x=input()
except Exception:
    x=int(input())
from collections import defaultdict
score=dict()
for i in range(x+1):score[i]=0
def process(a,b,c,d):
    if c>d:score[a]+=3
    elif c<d:score[b]+=3
    else:
        score[a]+=1
        score[b]+=1
game=0
total=int(x*(x-1)/2)
while game<total:
    s=raw_input().split() if 'raw_input' in globals() else input().split()
    a=int(s[0])
    b=int(s[1])
    c=int(s[2])
    d=int(s[3])
    process(a,b,c,d)
    game+=1
for xx in range(1,x+1):
    z=1
    jj=1
    while jj<=x:
        if score[xx]<score[jj]:
            z+=1
        jj+=1
    print(z)