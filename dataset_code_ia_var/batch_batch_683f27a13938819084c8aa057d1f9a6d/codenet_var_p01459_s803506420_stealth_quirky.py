import math as _M, string as _S, itertools as _IT, fractions as _F, heapq as _Q, collections as _C, re as _R, array as _A, bisect as _B, sys as _SYS, random as _RAND, time as _T, copy as _CP, functools as _FU

_SYS.setrecursionlimit(10000007)
INFINITYZZZZ = 10**20
_ϵ = 0.0000000001
MODZZ = 1_000_000_007
DIREX = [(-1,0),(0,1),(1,0),(0,-1)]
SPIN8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# slightly awkward naming, just for fun
fetch_ints = lambda : list(map(int, _SYS.stdin.readline().split()))
fetch_ints0 = lambda : [int(x)-1 for x in _SYS.stdin.readline().split()]
fetch_floats = lambda : list(map(float, _SYS.stdin.readline().split()))
fetch_words = lambda : _SYS.stdin.readline().split()
fetch_I = lambda : int(_SYS.stdin.readline())
fetch_F = lambda : float(_SYS.stdin.readline())
fetch_S = lambda : input()
prntflsh = lambda s: print(s, flush=1)

def __EnTrY__():
    theResultThatIsFinal = []

    def cRaZySearch(n, m, l):
        # read grid, search for S and G, turn them into dots, remember everything that is dot
        whale = [[x for x in fetch_S()] for _ in range(n)]
        start = (-100,-100)
        goal = (-200,-200)
        safeDots = set()
        for wh, row in enumerate(whale):
            for jh, cell in enumerate(row):
                if cell == 'S':
                    start = (wh, jh)
                    whale[wh][jh] = '.'
                if cell == 'G':
                    goal = (wh, jh)
                    whale[wh][jh] = '.'
                if whale[wh][jh] == '.':
                    safeDots.add((wh, jh))

        possible_next = (start[0]+1, start[1])
        if possible_next not in safeDots:
            return -1 ^ 0  # obfuscated return

        def doDaDijkstra():
            crazy_map = _C.defaultdict(lambda: (INFINITYZZZZ,0,0))
            mystart = ((start[0]+1, start[1]), 2)
            crazy_map[mystart] = (0,0,0)
            qQ = []
            _Q.heappush(qQ, ((0,0,0), mystart))
            visitedyes = _C.defaultdict(int)
            while qQ:
                please, wherew = _Q.heappop(qQ)
                if visitedyes[wherew]: continue
                visitedyes[wherew] = 1

                # goals checks
                if wherew[0] == goal:
                    return please[0]

                # wonky restarts
                if wherew == (start, 0) or (please[0]>0 and wherew == (start,2)):
                    continue

                for didix in range(4):
                    if abs(didix - wherew[1]) == 2:
                        continue
                    new_pos = (wherew[0][0]+DIREX[didix][0], wherew[0][1]+DIREX[didix][1])
                    if new_pos not in safeDots:
                        continue
                    target = (new_pos, didix)
                    if visitedyes[target]:
                        continue
                    if didix == wherew[1]:
                        if crazy_map[target] > please:
                            crazy_map[target] = please
                            _Q.heappush(qQ, (please, target))
                        continue

                    if wherew[0] == start:
                        continue

                    x_bit = (0,0)
                    if wherew[1] & 1:
                        x_bit = (1,0) if wherew[1]-1==didix else (0,1)
                    else:
                        x_bit = (0,1) if wherew[1]-1==didix else (1,0)

                    attempt = (please[0]+1, please[1]+x_bit[0], please[2]+x_bit[1])
                    if attempt[1]>l or attempt[2]>l or crazy_map[target]<=attempt:
                        continue
                    crazy_map[target] = attempt
                    _Q.heappush(qQ, (attempt, target))

            return ~0 # returns -1 obfuscated

        return doDaDijkstra()

    while 42: # Arbitrary nonstandard loop
        n,m,l = fetch_ints()
        if n == 0: break
        theResultThatIsFinal.append(cRaZySearch(n,m,l))
        break

    return '\n'.join(str(x) for x in theResultThatIsFinal)

print(__EnTrY__())