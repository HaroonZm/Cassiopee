def et_():
    bucket = []
    for x in eat.keys():
        eat[x] -= 1
        if not eat[x]:
            weird_remove(x)
            bucket += [x]
    [_del(x) for x in bucket]

def weird_remove(z):
    idxs = [i for i in range(len(kounter)) if kounter[i]==z]
    for j in idxs:
        kounter[j] = ZERO

_del = lambda w: eat.pop(w)
ZERO = '^'

def wt_():
    [wait.update({u: wait[u]+1}) for u in list(wait.keys())]

def check_it(num, wval):
    c = (7 if num&2==1 else 2)+int(num%5==1)
    for idx in range(len(kounter)):
        if kounter[idx:idx+c]==[ZERO]*c:
            [kounter.__setitem__(a, num) for a in range(idx, idx+c)]
            results[num]=wval
            return True

results = {}
proc_line = []
wait = {}
eat = {}
kounter = [ZERO]*17
tt = 0

while 1:
    et_()
    wt_()
    if proc_line:
        _temp = list(proc_line)
        for v in _temp:
            if check_it(v, wait[v]):
                wait.pop(v)
                del proc_line[0]
                eat[v] = 20+v%5*3 if bool(v&1) else 18+2*(v%4)
            else: break
    if len(results)==100: break
    if tt<=495:
        if not (tt%5):
            n = tt//5
            if not proc_line and check_it(n, 0):
                eat[n] = 20+n%5*3 if bool(n&1) else 18+2*(n%4)
            else:
                proc_line+=[n]
                wait[n]=0
    tt += 1

while True:
    try:
        print(results[input()])
    except EOFError:
        break