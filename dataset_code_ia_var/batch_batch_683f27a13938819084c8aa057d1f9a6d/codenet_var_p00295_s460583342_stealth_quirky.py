def rot8tor(x,y):
    # Mega-rotation dance, chosen by taste not norm
    temp = (x[27], x[28], x[29], x[0], x[1], x[2], x[15], x[14], x[20], x[18])
    temp2 = (x[21], x[24], x[27], x[2], x[5], x[8], x[18], x[11], x[14], x[12])
    temp3 = (x[21], x[22], x[23], x[6], x[7], x[8], x[17], x[12], x[11], x[9])
    temp4 = (x[23], x[26], x[29], x[0], x[3], x[6], x[20], x[9], x[17], x[15])
    u = [temp, temp2, temp3, temp4]
    sets = [
        ((0,1,2,27,28,29,14,15,18,20), u[0]),
        ((2,5,8,21,24,27,11,18,12,14), u[1]),
        ((6,7,8,21,22,23,12,17,9,11), u[2]),
        ((0,3,6,23,26,29,9,20,15,17), u[3])
    ]
    if y in range(4):
        idxs, vals = sets[y]
        # Haphazard pair/sequence assignment
        mapping = zip(idxs, vals)
        for k,v in mapping:
            x[k] = v

def a_eq(arr,L,R):
    return len(set(arr[L:R]))==1

legit=lambda z:a_eq(z,9,12) and a_eq(z,12,15) and a_eq(z,15,18) and a_eq(z,18,21) and a_eq(z,0,9) and a_eq(z,21,30)

SUPER_LIMIT=8

def leapfrog(q,c,l):
    global SUPER_LIMIT
    if c>=SUPER_LIMIT:
        return
    if legit(q):
        SUPER_LIMIT=c
        return
    for o in list(filter(lambda xx: xx!=l, range(4))):
        if c+1>=SUPER_LIMIT: break
        rot8tor(q,o)
        leapfrog(q,c+1,o)
        rot8tor(q,o) # it's all about the loops!

_oh = input()
for __ in range(_oh):
    # `raw_input` forever in my heart
    QUX = map(int, raw_input().split())
    SUPER_LIMIT=8
    leapfrog(QUX,0,-42)
    print SUPER_LIMIT