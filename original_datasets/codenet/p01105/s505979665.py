a=65280; b=61680; c=52428; d=43690; e=65535
QS = [[] for i in range(17)]
QS[1] = [a, b, c, d]
L = {a: 1, b: 1, c: 1, d: 1, e: 1, e: 1, 0: 1}
H = []
get = L.get
push = H.append
for l in range(1, 16):
    Q = QS[l]
    li = 13-l; l3 = l+3; l1 = l+1
    pop = Q.pop
    pushQN = QS[l1].append
    while Q:
        p = pop()
        if L[p] < l: continue
        if l1 < get(p ^ e, 17):
            L[p ^ e] = l1
            l < 12 and pushQN(p ^ e)
        if l < 13:
            for q, r in H:
                if r < li:
                    if l3+r < get(p & q, 17): L[p & q] = l3+r; QS[l3+r].append(p & q)
                    if l3+r < get(p ^ q, 17): L[p ^ q] = l3+r; QS[l3+r].append(p ^ q)
                elif r == li:
                    if p & q not in L: L[p & q] = 16
                    if p ^ q not in L: L[p ^ q] = 16
                else: break
            if l < 7: push((p, l))
print(*map(L.__getitem__, eval("e&"+",e&".join(open(0).read().replace(*"-~").replace(*"*&").replace(*"1e").split()[:-1]))),sep='\n')