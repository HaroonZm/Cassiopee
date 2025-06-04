import os; import sys
import numpy as np

def solution(input_data):

    class Segtree:  # OOP
        TABS = []

        @staticmethod
        def bits(n):  # procedural
            ret = 0
            while n: n >>= 1; ret += 1
            return ret

        @classmethod
        def buildtree(cls, n):
            size = 1 << cls.bits(n)
            cls.TABS += [np.zeros((size << 1), dtype=np.int64)]
            return len(cls.TABS) - 1

        @classmethod
        def construct(cls, idx, values):
            tab = cls.TABS[idx]
            off = tab.size >> 1
            tab[off:off + len(values)] = values
            for i in reversed(range(1, off)):
                k = i << 1
                tab[i] = max(tab[k], tab[k + 1])

        @staticmethod
        def update(ins, i, v):
            tbl = Segtree.TABS[ins]; off = tbl.size >> 1
            x = i + off
            tbl[x] = v
            while x > 1:
                par = x >> 1
                tbl[par] = max(tbl[x], tbl[x ^ 1])
                x //= 2

        @staticmethod
        def query(ins, l, r):
            T = Segtree.TABS[ins]; o = T.size >> 1
            l, r, acc = l + o, r + o, -1
            # Some functional look:
            while l < r:
                acc = max(acc, (T[r-1] if r & 1 else acc))
                if l & 1: acc = max(acc, T[l]); l += 1
                l //= 2; r //= 2
            return acc

        @staticmethod
        def search(ins, lo, v):
            T = Segtree.TABS[ins]; o = T.size >> 1; i = lo + o
            # Sentinel trick
            while T[i] < v:
                while i & 1: i >>= 1
                i += 1
            while i < o:
                i <<= 1
                if T[i] < v: i += 1
            return i - o

    # tuple unpacking
    n, q = input_data[0], input_data[1]
    a = input_data[2:n + 2]
    t, x, y = (input_data[n + 2::3], input_data[n + 3::3], input_data[n + 4::3])
    BIG_NUM = 1 << 60

    # One-liner style
    a = np.concatenate((a, [BIG_NUM]))

    index = Segtree.buildtree(n + 1)
    Segtree.construct(index, a)
    answers = list()

    # Imperative
    for i in range(q):
        if t[i] == 1: Segtree.update(index, x[i] - 1, y[i])
        elif t[i] == 2: answers.append(Segtree.query(index, x[i] - 1, y[i]))
        else: answers.append(Segtree.search(index, x[i] - 1, y[i]) + 1)
    return answers

if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('solution', '(i8[:],)')(solution)
    cc.compile()
    exit()

if os.name == 'posix':
    from my_module import solution
else:
    from numba import njit
    solution = njit('(i8[:],)', cache=True)(solution)
    print('compiled', file=sys.stderr)

inp = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
ans = solution(inp)
for s in ans: print(s)