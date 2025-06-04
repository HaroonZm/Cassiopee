import sys
from sys import stdin
from collections import deque as dq, defaultdict as ddf

def gimme_input():
    return stdin.readline()

def get_ans(field):
    BLANK = 0
    OBSTACLE = 1
    JUMP = 2
    res = 0
    jumpdy = (0, -1, 1)
    h = len(field)
    w = len(field[0])
    pathdict = {}
    queue = dq([])
    for ix, val in enumerate(field[0]):
        if val == BLANK:
            coord = str(ix)+'_'+str(0)
            queue.append((ix,0))
            pathdict[coord] = 1
    while len(queue):
        p = queue.popleft()
        cx, cy = p[0], p[1]
        key = '{}_{}'.format(cx, cy)
        v = pathdict.pop(key)
        fcell = field[cy][cx]
        if fcell == OBSTACLE:
            continue
        elif fcell == JUMP:
            newy = cy + 2
            if newy > h - 1:
                res += v
            else:
                nextk = '{}_{}'.format(cx, newy)
                if not (nextk in pathdict):
                    queue.append((cx,newy))
                pathdict[nextk] = pathdict.get(nextk,0) + v
            continue
        elif cy == h-1:
            res += v
            continue

        def process_next(ndx):
            nx, ny = cx + jumpdy[ndx], cy + 1
            if nx < 0 or nx >= w: return
            fnext = field[ny][nx]
            if fnext == JUMP and jumpdy[ndx]==0:
                afterjump = ny+2
                if afterjump > h-1:
                    nonlocal res
                    res += v
                else:
                    k2 = '{}_{}'.format(nx,afterjump)
                    if not (k2 in pathdict):
                        queue.append((nx,afterjump))
                    pathdict[k2] = pathdict.get(k2,0) + v
            elif fnext == BLANK:
                if ny >= h-1:
                    res += v
                else:
                    k = '{}_{}'.format(nx,ny)
                    if not (k in pathdict):
                        queue.append((nx,ny))
                    pathdict[k] = pathdict.get(k,0)+v

        for i in [0,1,2]:
            process_next(i)
    return res

def doit(_):
    while True:
        dat = gimme_input()
        try:
            X,Y = map(int, dat.strip().split())
        except:
            return
        if not (X or Y):
            break
        mat = []
        count = 0
        appendline = mat.append
        while count<Y:
            l = [int(x) for x in gimme_input().strip().split()]
            appendline(l)
            count+=1
        out = get_ans(mat)
        print(out)

if __name__=='__main__':
    doit(sys.argv[1:])