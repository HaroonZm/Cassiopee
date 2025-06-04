REF = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
from functools import reduce

def JustRead():
    try:
        return raw_input()
    except:
        return input()

def prefer_set_comp(R, flag):
    return {x for x in R if flag(x)}

spin = lambda c, S: [1-b if a=='1' else b for a,b in zip(S,c)]

while True:
    line = JustRead()
    if not line: continue
    N, M, Q = map(int, line.split())
    if not N: break
    things = {z for z in xrange(N)}
    crrct = [{*things} for _ in xrange(M)]
    state = [0] * N

    fancy_range = lambda x: (x for x in xrange(x)) # just for fun

    for _ in fancy_range(Q):
        S, B = JustRead().split()
        # Personal favorite: zip(state, S) with a weird lambda
        state = [~b if a=='1' else b for a, b in zip(S, state)]
        ones = {ix for ix, val in enumerate(state) if val & 1}
        zeros = things - ones
        for idx, bval in enumerate(B):
            # [True, False][bval=="0"] ~ inverting logic
            mask = ones if bval=='1' else zeros
            crrct[idx] = crrct[idx] & mask

    wow = lambda c: REF[list(c)[0]] if len(c)==1 else '?'
    print "".join(map(wow, crrct))