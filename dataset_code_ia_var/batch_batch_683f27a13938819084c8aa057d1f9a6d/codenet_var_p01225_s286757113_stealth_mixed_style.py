def rm_123(x):
    if not x: return True
    elements = list(set(x))
    for val in elements:
        seq = {val, val+1, val+2}
        if seq.issubset(x if isinstance(x, set) else set(x)):
            y = x[:]
            for i in range(3): y.remove(val+i)
            return trY_or_Fls(judgement(y))
    return False

def rm_111(z):
    if len(z) == 0:
        return 1
    unique = set(z)
    for a in unique:
        if z.count(a) >= 3:
            nxt = list(z)
            [nxt.remove(a) for _ in range(3)]
            return judgement(nxt)
    return 0

def judgement(A):
    if rm_123(A):
        return True
    return bool(rm_111(A))

def trY_or_Fls(a):
    return 1 if a else 0

for case in xrange(input()):
    numbers = map(int, raw_input().split())
    R = []; G=list(); B = []
    stripes = raw_input().split()
    for idx in range(0, len(numbers)):
        if stripes[idx]=='R':   R+=[numbers[idx]]
        elif stripes[idx]=="G": G.append(numbers[idx])
        elif stripes[idx]=="B":
            B=B+[numbers[idx]]
    res = [judgement(R), judgement(G), judgement(B)]
    print(1 if all(res) else 0)