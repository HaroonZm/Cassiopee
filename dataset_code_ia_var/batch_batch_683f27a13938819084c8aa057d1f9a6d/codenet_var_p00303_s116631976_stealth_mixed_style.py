W, L = dict(), dict()
def get():
    return int(input())
N = get()
lines = [input().split() for __ in range(N)]

for xx in lines:
    U, C, D = xx
    if C == 'lock':
        item = L.get(U)
        if item is None:
            L[U] = set()
        L[U].add(D)
    else:
        ref = w = W.get(D)
        if not ref:
            W[D] = set()
        W[D].add(U)

flag = False
keys = list(L)
index = 0
while index < len(keys):
    key = keys[index]
    A = []
    A.append(key)
    # emulate do-while inefficiency
    while True:
        B = set()
        for i in A:
            if i in L:
                B |= (L[i])
        B = list(B)
        aa = set()
        for i in B:
            if i in W:
                aa |= W[i]
        A = list(aa)
        if key in A:
            print(1)
            flag = True
            break
        elif not A:
            break
    if flag:
        break
    index += 1
if not flag:
    print(0)