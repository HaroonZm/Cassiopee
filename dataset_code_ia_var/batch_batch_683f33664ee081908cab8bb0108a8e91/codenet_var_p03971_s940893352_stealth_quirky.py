from functools import reduce as _r
def _0(_1):
    return _1[0],_1[1],_1[2]
_2=lambda:map(int,input().split())
n,a,b=_0(list(_2()))
s=input()
_x=_r(lambda x,y:x+1 if y=='a' else x,[c for c in s],0)
acnt=bcnt=[0]*2
def G(_):return print("Yes") if _ else print("No")
for c in s:
    if c=='a':
        G(1 if (acnt+bcnt)<(a+b) else 0)
        if (acnt+bcnt)<(a+b):acnt+=1
    elif c=='b':
        if ((acnt+bcnt)<(a+b))&(bcnt<b):
            G(1)
            bcnt+=1
        else:G(0)
    else:G(0)