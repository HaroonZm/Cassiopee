t=int(input())
def expect(mvals, mprobs):
    return sum(v*r for v,r in zip(mvals,mprobs))/(sum(mprobs))
dices=[]
for _ in range(t):
    n,m=map(int,input().split())
    vals=[]
    probs=[]
    for __ in range(m):
        v,r=input().split()
        vals.append(int(v))
        probs.append(float(r))
    dices.append((vals,probs))
p,q=map(int,input().split())
pv=[]
pr=[]
for _ in range(q):
    v,r=input().split()
    pv.append(int(v))
    pr.append(float(r))
boss_exp=expect(pv,pr)
for vals,probs in dices:
    e=expect(vals,probs)
    if e-boss_exp>1e-7:
        print("YES")
        break
else:
    print("NO")