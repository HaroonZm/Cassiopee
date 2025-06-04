import sys
from functools import reduce
from operator import add

def solve():
    S = sys.stdin.readline().strip()
    rot = lambda d, c: (d + (1 if c == "R" else -1)) % 4
    cur_upd = lambda cur, d, prev_d: cur + 1 if d == (prev_d+1)%4 and d == cur else (0 if d == 0 else cur)
    state_seq = list(zip(S, [None] + list(S[:-1])))
    d = 0
    cur = 0
    ans = 0

    def step(state, pair):
        d, cur, ans, prev_d = state
        c, prev_c = pair
        nd = rot(d, c)
        ncur = cur + 1 if (c=="R" and d==cur) else cur
        ncur = 0 if (c!="R" and nd==0) else ncur
        if c=="R": ndcur = ncur
        else: ndcur = ncur
        nans, ncur = (ans+1, 0) if (nd==0 and ncur==4 and c=="R") else (ans, ndcur)
        return (nd, ncur, nans, d)
    # apply step
    d, cur, ans, _ = reduce(step, state_seq, (0,0,0,0))
    sys.stdout.write("%d\n" % ans)
solve()