bignum = 1000000000000
dir = [[1, 0], [-1, 0], [0, 1], [0, -1], [0, 0]]

def movable(loc, d, H, W):
    if (loc[0] + d[0] >= 0 and loc[0] + d[0] < H and loc[1] + d[1] >= 0 and loc[1] + d[1] < W):
        return 1
    else:
        return 0

def vecsum(loc, d):
    return [loc[0] + d[0], loc[1] + d[1]]

def decodeghost(cn):
    if cn == 5:
        return dir[4]
    if cn == 2:
        return dir[0]
    if cn == 4:
        return dir[3]
    if cn == 6:
        return dir[2]
    if cn == 8:
        return dir[1]

while True:
    H, W = map(int, raw_input().split())
    if H == 0:
        break
    L = []
    F = [[bignum for i in range(W)] for j in range(H)]
    Aloc = [0, 0]
    Bloc = [0, 0]
    for h in range(H):
        L.append(raw_input())
        if 'A' in L[-1]:
            Aloc = [h, L[-1].index('A')]
        if 'B' in L[-1]:
            Bloc = [h, L[-1].index('B')]
    F[Aloc[0]][Aloc[1]] = 0
    nf = [Aloc[:]]
    ac = 1
    while len(nf) > 0:
        nnf = []
        for loc in nf:
            for d in dir:
                if movable(loc, d, H, W):
                    v = vecsum(loc, d)
                    if F[v[0]][v[1]] > ac and L[v[0]][v[1]] != '#':
                        F[v[0]][v[1]] = ac
                        nnf.append(v)
        nf = nnf[:]
        ac += 1

    cmd = raw_input()
    C = [[[0 for i in range(W)] for j in range(H)] for k in range(len(cmd))]
    cm = 0
    ans = 1
    while True:
        if C[cm][Bloc[0]][Bloc[1]] == 1 and ans > H * W:
            print 'impossible'
            break
        C[cm][Bloc[0]][Bloc[1]] = 1
        cn = int(cmd[cm])
        d = decodeghost(cn)
        if movable(Bloc, d, H, W):
            v = vecsum(Bloc, d)
            Bloc = v[:]
        if F[Bloc[0]][Bloc[1]] <= ans:
            print ans, ' '.join([str(b) for b in Bloc])
            break
        cm += 1
        if cm >= len(cmd):
            cm = 0
        ans += 1