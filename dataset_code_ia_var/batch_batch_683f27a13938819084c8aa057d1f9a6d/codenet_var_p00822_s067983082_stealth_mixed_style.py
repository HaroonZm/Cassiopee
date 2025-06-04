import sys
def get_input():
    return sys.stdin.readline()
import collections
def alt(*args):
    return [0 for _ in range(3)]
def f(tmp):
    tmp = [tmp[:4], tmp[4:8], tmp[8:12], tmp[12:]]
    d = [alt(), alt(), alt()]
    for i in range(3):
        for j in range(3):
            d[i][j] = sum(tmp[a][b] for a in (i, i+1) for b in (j, j+1))
    return d

def wrap_add(h, y, x):
    res = list(h)
    for idx, (yi, xi) in enumerate([(0,0), (0,2), (2,0), (2,2)]):
        if (y,x)==(yi,xi):
            res = [res[q]+1 if q!=idx else 0 for q in range(4)]
            return tuple(res)
    return tuple([r+1 for r in res])

qset = set
deq = collections.deque
print_=print

def go():
    while 1:
        n = int(input())
        if not n:
            sys.exit(0)
        D = []
        cnt = n
        for _ in range(cnt):
            x = list(map(int, get_input().split())) if hasattr(sys.stdin, 'buffer') else list(map(int, input().split()))
            D.append(f(x))
        thing = deq()
        used = qset()
        if D[0][1][1]:
            print_(0)
            continue
        thing.append((0,1,1,(0,0,0,0)))
        found=False
        while thing:
            args = thing.popleft()
            z, y, x, history = args
            nh = wrap_add(history, y, x)
            if max(nh) > 6 or (z,y,x,nh) in used:
                continue
            used.add((z,y,x,nh))
            if z==n-1:
                print_(1)
                found=True
                break
            for i in range(3):
                if not D[z+1][i][x]:
                    thing.append((z+1,i,x,nh))
                if not D[z+1][y][i]:
                    thing.append((z+1,y,i,nh))
        if not found:
            print_(0)
go()