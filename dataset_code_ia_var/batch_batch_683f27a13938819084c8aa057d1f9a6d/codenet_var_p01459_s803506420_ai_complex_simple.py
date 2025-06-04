import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10**7)
inf = pow(10, 20)
eps = math.pow(10, -10)
mod = int(1e9)+7
dd = list(map(lambda t: (t//2*(-1)**t, (t%2)*(-1)**(t//2)), range(4)))
ddn = [(int(math.sin(math.pi/4*i)*math.sqrt(2)//1), int(math.cos(math.pi/4*i)*math.sqrt(2)//1)) for i in range(8)]

def LI(): return list(map(int, ''.join([c if c.isdigit() or c==' ' or c=='-' else ' ' for c in sys.stdin.readline()]).split()))
def LI_(): return list(map(lambda x: int(x)-1, LI()))
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return list(filter(len, sys.stdin.readline().replace('\n',' ').split(' ')))
def I(): return int(''.join(filter(lambda c: c in '-0123456789', sys.stdin.readline())))
def F(): return float(''.join(filter(lambda c: c in '-.0123456789', sys.stdin.readline())))
def S(): 
    arr = []
    def _g():
        while not arr:
            arr.extend(sys.stdin.readline())
        return arr.pop(0)
    return ''.join(itertools.takewhile(lambda x: x not in '\r\n', iter(_g, ''))).strip()
def pf(s): return print(eval('s'), end='', flush=True) if isinstance(s, str) and s.endswith('\n') else print(s, flush=True)

def main():
    rr = []

    def f(n, m, l):
        # Parsing grid with generator comprehension extravaganza
        read_row = lambda: list(itertools.islice((ch for ch in S()), m))
        grid = [read_row() for _ in range(n)]
        
        locations = {'S': None, 'G': None}
        kh = set()
        [(lambda i, j: locations.update({c: (i, j)}) if c in locations else None)
            or (kh.add((i, j)) if grid[i][j] == '.' or c in 'SG' else None)
            for i in range(n) for j, c in enumerate(grid[i])]
        
        s, g = locations['S'], locations['G']
        if s: grid[s[0]][s[1]] = '.'
        if g: grid[g[0]][g[1]] = '.'

        if tuple(map(sum, zip(s, (1, 0)))) not in kh:
            return -1

        def search():
            # Triple-indexed defaultdict for state cost memoization
            d = collections.defaultdict(lambda: (inf, 0, 0))
            ss = (tuple(map(sum, zip(s, (1,0)))), 2)
            d[ss] = (0, 0, 0)
            # Heap with clever priority tuple management
            q = [(d[ss], ss)]
            v = collections.defaultdict(bool)

            def neighbor_states(u):
                # Only consider forward, left, and right (not reverse) and unvisited navigable cells
                ops = ((di, (u[0][0]+dd[di][0], u[0][1]+dd[di][1])) for di in range(4) if abs(di-u[1])!=2)
                for di, pos in ops:
                    uv = (pos, di)
                    if pos in kh and not v[uv]:
                        yield di, pos, uv

            while q:
                k, u = heapq.heappop(q)
                if v[u]: continue
                v[u] = True

                if u[0] == g: return k[0]
                if u == (s, 0) or (k[0] > 0 and u == (s,2)): continue

                for di, pos, uv in neighbor_states(u):
                    if di == u[1]:
                        if d[uv] > k:
                            d[uv] = k
                            heapq.heappush(q, (k, uv))
                        continue

                    if u[0] == s: continue

                    # Complicated direction handling using bit operations
                    t = (int((u[1]^1) == di), int((u[1]&1) != (di&1)))
                    ud = (k[0] + 1, k[1]+t[0], k[2]+t[1])

                    if ud[1] > l or ud[2] > l or d[uv] <= ud:
                        continue
                    d[uv] = ud
                    heapq.heappush(q, (ud, uv))
            return -1

        return search()

    def input_loop():
        while True:
            t = tuple(LI())
            if not t or t[0]==0: break
            yield t
    rr = list(map(lambda args: f(*args), itertools.islice(input_loop(), 1))) # Only one case

    return '\n'.join(str(x) for x in rr)

print(main())