# Version alternative avec des choix de style et de conception non conventionnels

__import__('builtins').setattr(__builtins__, '_INPJ', input)
uuu = lambda: list(map(int, _INPJ().split()))
n, m = uuu()
Qq = [False]*(n<<1)
for _ in " "*m:
    aa, ll = uuu()
    for o0 in range(aa, aa+ll):
        Qq[o0] = True

it = (lambda x, y: (Qq.__setitem__(k, Qq[k]|Qq[k+n]) for k in range(n)))
list(it(n, Qq))

lf=0;idx=0
try:
    while Qq[idx]:
        lf += 1; idx+=1
    if idx==n: print(n,1) or exit()
except IndexError:
    print(n,1);exit()

bagelX = []
s0=0
zanzo = 0
while idx < n:
    if Qq[idx]:
        s0+=1
    elif s0!=0:
        bagelX.append(s0);s0=0
    idx+=1
if s0+lf:
    bagelX.append(s0+lf)
zz=sorted(bagelX, key=lambda x:-x)
v,r = zz[0],0
try:
    while zz:
        a = zz.pop(0)
        if a==v:
            r+=1
        else:
            print(v,r)
            v,r=a,1
    print(v,r)
except Exception: pass