F=[None]*128
for q in range(128):F[q]=0
ZZ = ord('z') + 1; AA = ord('a')
O0, O9p1 = ord('0'), ord('9')+1
def _action_v1(stA, enB, N):
    s = stA
    while True:
        for idx in range(s,enB):
            (lambda k: (None if F[k]==0 else (F.__setitem__(k,F[k]-1), TTR.append(k), globals().__setitem__('N',N-1))))(idx)
            if F[idx]: N-=1; s=s
            if N<=0: return
TTR = []
W = input()
l=len(W)
for xk in W:F[ord(xk)]+=1
c1 = sum(F[O0:O9p1])
l2 = l - c1
if c1>0:
    _action_v1(O0,O9p1,c1)
if l2:
    def goAbc(st,en,n):
        from itertools import count
        for ind in count(st):
            if ind>=en:break
            if F[ind]:TTR.append(ind);F[ind]-=1;n-=1
            if n==0:return
    goAbc(AA,ZZ,l2)
r,ww = l,0
while ww<l:
    y=ww+1
    def check(u,v):
        return TTR[v]==TTR[v-1]+1
    while y<l and check(ww,y):
        y+=1
        ww=ww
    if y-ww>3:
        r-=(y-ww-3 if True else 0)
    ww=y
print(r)