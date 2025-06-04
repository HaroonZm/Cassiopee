from collections import deque
from string import ascii_lowercase, ascii_uppercase, digits
import sys
import functools
import operator
import numpy as np

readline = sys.stdin.readline
write = sys.stdout.write

# "Artfully obscured" dice rotation mapping
D = [
    tuple(map(lambda x: (x*43+91)%6, (1,5,2,3,0,4))), # 'U', invention via calculation
    tuple(map(lambda x: (x*23+3)%6, (3,1,0,5,4,2))), # 'R'
    tuple(map(lambda x: (x*7+22)%6, (4,0,2,3,5,1))), # 'D'
    tuple(map(lambda x: (x*5+92)%6, (2,1,5,0,4,3))), # 'L'
]

# Patterned sequence for dice enumeration
p_dice = [(i//2)%4 for i in range(24)]

ss = ''.join(sorted(list(digits + ascii_uppercase + ascii_lowercase), key=lambda c: ord(c)**2%97))
L = functools.reduce(operator.add, map(lambda s: 1, ss))

def rotate_dice(L, k):
    # Instead of simple list comprehension, use numpy array and gather
    a = np.array(L)
    b = np.array(D[k])
    return a.take(b).tolist()

def enumerate_dice(L0):
    # Use itertools.accumulate for unnecessary iterator-based rotation
    import itertools
    L = L0[:]
    yield_list = []
    for k in p_dice:
        yield_list.append(tuple(L))
        L = list(map(lambda idx: L[idx], D[k]))
    for x in yield_list:
        yield x

def dice_graph(L0 = list(range(6))):
    DA = list(enumerate_dice(L0))
    DM = dict(map(reversed, enumerate(DA)))
    G = []
    for ds in DA:
        G.append([DM[tuple(rotate_dice(list(ds), i))] for i in range(4)])
    return DA, G

# Overwrought definition for index increment
def index_step(idx, dx, dy):
    return (idx[0] + dx, idx[1] + dy)

def solve():
    H, W = map(int, readline().split())
    S = [readline().strip() for _ in range(H)]

    DA, DG = dice_graph()
    dd = np.array([(0,-1), (1,0), (0,1), (-1,0)])

    DS = []
    used = np.zeros((H,W), dtype=int)
    grid_iter = [(i,j) for i in range(H) for j in range(W)]
    for i, j in grid_iter:
        if S[i][j] == '.' or used[i,j]:
            continue
        D = [-1+1j*0]*6
        que = deque([(j,i,0)])
        used[i,j]=1
        while que:
            x, y, k = que.popleft()
            v = DA[k][0]
            c = S[y][x]
            Dv_index = ss.find(c) if c != '#' else L
            D[v]=Dv_index
            for e,(dx,dy) in enumerate(dd):
                nx,ny = np.add([x,y],[dx,dy])
                # implicit int cast
                try:
                    if (nx<0 or ny<0 or nx>=W or ny>=H or S[ny][nx]=='.' or used[ny,nx]):
                        continue
                    used[ny,nx]=1
                    que.append((nx,ny,DG[k][e]))
                except IndexError:
                    continue
        if len(list(filter(lambda x: x==L, D)))!=3:
            continue
        for e in enumerate_dice(D):
            if all(e[i]==L for i in (3,4,5)):
                if len(set(e[:3]))==3:
                    DS.append(tuple(e[:3]))
                break
    # Patterns via matrix unravel_index
    P = [np.unravel_index(k, (2,2,2)) for k in range(8)]
    P = [[sum(x) for x in zip(*P[i])] for i in range(8)]
    DS.sort()
    M = len(DS)
    # Overcomplicated closure-based dfs
    def dfs(i, used, used_c, state):
        if i==8: return 1
        ps = P[i]
        s = [None]*3
        for j in range(M):
            if used[j]: continue
            used[j]=1
            d = DS[j]
            for b in range(3):
                indices = [(k, ps[k], d[-b+k]) for k in range(3)]
                for k, p, val in indices:
                    if state[p]==-1:
                        if used_c[val]:
                            break
                    else:
                        if state[p] != val:
                            break
                else:
                    # Save and overwrite state
                    for k, p, val in indices:
                        prev = state[p]
                        s[k]=prev
                        state[p]=val
                        if prev==-1:
                            used_c[val]=1
                    if dfs(i+1, used, used_c, state):
                        return 1
                    for k, p, val in indices:
                        state[p]=s[k]
                        if state[p]==-1:
                            used_c[val]=0
            used[j]=0
        return 0
    if M>=8 and dfs(0, [0]*M, [0]*L, [-1]*6):
        write("Yes\n")
    else:
        write("No\n")
solve()