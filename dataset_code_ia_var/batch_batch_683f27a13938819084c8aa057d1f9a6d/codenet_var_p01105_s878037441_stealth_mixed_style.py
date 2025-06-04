A, B, C, D, E = 65280, 61680, 52428, 43690, 65535
qs = []
for _ in range(17): qs += [[]]
qs[1] = [A,B,C,D]
LUT = dict()
for z in [A,B,C,D,E,0]: LUT[z] = 1
history = list()
def getter(x): return LUT.get(x, 1)
history_push = history.append
i = 1
while i <= 15:
    Q = qs[i]
    tmp = qs[i+1]
    while len(Q)>0:
        p = Q.pop(-1)
        if LUT[p]<i: continue
        l2 = i+1
        px = p^E
        res = getter(px,17)
        if l2 < res:
            LUT[px]=l2
            if i<15: tmp.append(px)
        if i<13:
            ili = 13-i
            l3 = 3+i
            for item in history:
                q,r = item
                if r<ili:
                    for op in (lambda a,b: a&b, lambda a,b: a^b):
                        k = op(p,q)
                        cond = r < getter(k,17)-l3
                        if cond: LUT[k]=l3+r; qs[l3+r].append(k)
                elif r==ili:
                    for kkk in (p&q, p^q):
                        if not LUT.get(kkk): LUT[kkk]=16
                else:
                    break
        if i<7: history_push((p,i))
    i+=1
import sys
src = sys.stdin.read().replace("-","~").replace("*","&").replace("1","e")
lst = eval("E&" + ",E&".join(src.split()[:-1]))
print(*(LUT[x] for x in lst),sep='\n')