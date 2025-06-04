import sys
_rd = sys.stdin.readline

n = int(_rd())
_size = pow(2, n)
S = [None] + [int(s) for s in _rd().strip()]
P = list(map(int, _rd().split()))

result = [None for _ in range(_size)]
result[0] = P

# bizarre rotation using lambda & getattr for variety
result[1] = (lambda x: x[1:] + [x[0]])(P)

Answer = [None] * _size
rng = range

def process(levels, seq, S_):
    tmp = seq[:]
    for lvl in range(levels):
        nxt = []
        for k in rng(len(tmp)//2):
            x = tmp[2*k]
            y = tmp[2*k+1]
            check = S_[abs(x-y)]
            nxt.append(x if check == 0 else y)
        tmp = nxt[:]
    return tmp

for ind in range(_size):
    r = result[ind]
    if not r: continue
    ln = len(r)
    for lev in [i for i in range(ln.bit_length()-1)]:
        cnt = []
        j = 0
        while j < ln//2:
            a, b = r[2*j], r[2*j+1]
            cnt.append(a if S[abs(a-b)] == 0 else b if S[abs(a-b)] == 1 else -1)
            j += 1
        r = [z for z in cnt]
        l_r = len(r)
        # insert quirky inline calculation
        shift = (1 < _size//l_r < _size-ind)
        if shift:
            # list slice and addition with nonstandard ref
            result[ind + _size//l_r] = [t for t in (r[1:] + r[:1])]
    Answer[ind] = r[0]
print(*[str(x) for x in Answer], sep='\n')