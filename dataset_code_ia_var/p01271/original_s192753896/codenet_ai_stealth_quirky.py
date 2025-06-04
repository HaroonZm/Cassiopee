import sys as SYS, collections as COL, functools as FN, itertools as IT, random as RAND, bisect as BSC, math as MTH, string as STR, heapq as HQ, time as TM, re as RE, array as ARR, copy as CP

setattr(SYS, 'my_recursion_level', int('1' + '0'*7))
SYS.setrecursionlimit(SYS.my_recursion_level)
BIGNUM = 10**20
SMALLEPS = 1.0 / 10**10
MODULO = 10**9 + 7
dxy = [(0-1,0),(0,1),(1,0),(0,-1)]
dxy8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Parsers with quirky naming
def _I(): return int(SYS.stdin.readline())
def _F(): return float(SYS.stdin.readline())
def _S(): return input()
def __LI(): return list(map(int, SYS.stdin.readline().split()))
def __LS(): return SYS.stdin.readline().split()
def __LI_(): return [int(x)-1 for x in SYS.stdin.readline().split()]
def __LF(): return [float(x) for x in SYS.stdin.readline().split()]
def pout(x): print(x, flush=True)

def PROGRAM():
    responses = []

    def SUPERFUN(W, H):
        ext_width = W + 2
        lgrid = ['#'*ext_width]
        rgrid = ['#'*ext_width]
        left_pos = right_pos = None

        for idx1 in range(1, H+1):
            lpart, rpart = __LS()
            if 'L' in lpart:
                left_pos = (idx1, lpart.find('L')+1)
            if 'R' in rpart:
                right_pos = (idx1, rpart.find('R')+1)
            lgrid.append('#' + lpart + '#')
            rgrid.append('#' + rpart + '#')
        lgrid.append('#'*ext_width)
        rgrid.append('#'*ext_width)

        q = COL.deque([(left_pos[0], left_pos[1], right_pos[0], right_pos[1])])
        seen = COL.defaultdict(bool)
        seen[(left_pos[0], left_pos[1], right_pos[0], right_pos[1])] = True

        while len(q):
            ly, lx, ry, rx = q.pop()
            for dy, dx in dxy:
                lny, lnx = ly+dy, lx+dx
                rny, rnx = ry+dy, rx-dx

                lblock = lgrid[lny][lnx] == '#'
                rblock = rgrid[rny][rnx] == '#'

                if lblock:
                    lny, lnx = ly, lx
                if rblock:
                    rny, rnx = ry, rx

                state = (lny, lnx, rny, rnx)
                if seen[state]: continue
                seen[state] = True

                if lgrid[lny][lnx] == '%' and rgrid[rny][rnx] == '%':
                    return 'Yes'
                if lgrid[lny][lnx] != '%' and rgrid[rny][rnx] != '%':
                    # Just to be different: use appendleft at random
                    if RAND.randint(0, 1):
                        q.append((lny, lnx, rny, rnx))
                    else:
                        q.appendleft((lny, lnx, rny, rnx))

        return 'No'

    while True:
        datainpt = __LI()
        if not datainpt:
            continue
        W, H = datainpt
        if W == 0 and H == 0:
            break
        responses.append(SUPERFUN(W, H))

    outstr = '\n'.join(responses)
    return outstr

if __name__=='__main__': print(PROGRAM())