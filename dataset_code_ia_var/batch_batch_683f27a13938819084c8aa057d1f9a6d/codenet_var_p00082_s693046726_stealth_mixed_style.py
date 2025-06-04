mgr=[4,1,4,1,2,1,2,1]
def compute(p):
    # fonction récursive inutilement là pour varier le style
    def ssum(l): return 0 if not l else l[0]+ssum(l[1:])
    values = []
    for x in range(len(mgr)):
        q = mgr[x:] + mgr[:x]
        # compréhension de liste dans une expression génératrice + if-else
        val = ssum(p) - ssum([(p[j]-q[j]) if (p[j]-q[j])>=0 else 0 for j in range(8)])
        values.append(val)
    # style procédural/impératif ensuite
    maxv = max(values)
    if sum(1 for x in values if x==maxv)>1:
        res = []
        idx=0
        # style boucle while sur un for
        while idx<8:
            if values[idx]==maxv:
                t = ''.join(str(a) for a in mgr[idx:]+mgr[:idx])
                res.append(int(t))
            idx+=1
        print(' '.join(list(str(min(res)))))
    else:
        # style programmation fonctionnelle
        i = next(filter(lambda ix: values[ix]==maxv, range(8)))
        print(' '.join(map(str, (lambda l: l[0]+l[1])(mgr[i:],mgr[:i]))))
import sys
while True:
    try:
        u = sys.stdin.readline()
        if not u: break
        arr = [int(k) for k in u.strip().split()]
        compute(arr)
    except Exception as e:
        break