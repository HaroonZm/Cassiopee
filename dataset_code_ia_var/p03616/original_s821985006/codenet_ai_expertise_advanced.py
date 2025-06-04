from sys import stdin
from bisect import bisect_left

def ints(): return map(int, stdin.readline().split())
def int1(): return int(stdin.readline())

X = int1()
K = int1()
r = list(ints())
Q = int1()
p = [tuple(ints()) for _ in range(Q)]

N0 = 1 << (Q-1).bit_length()
data = [0]*(2*N0)
def update(l, r, v):
    L, R = l+N0, r+N0
    while L < R:
        if R & 1:
            R -= 1
            data[R-1] += v
        if L & 1:
            data[L-1] += v
            L += 1
        L >>= 1; R >>= 1

def query(k):
    i = k+N0-1
    s = 0
    while i >= 0:
        s += data[i]
        i = (i-1)//2
    return s

# Prepare: ordered Q times, compress positions for fast access
p_ord = [(a,t,i) for i,(t,a) in enumerate(p)]
p_ord.sort()
id_map = [0]*Q
for idx,(*_,i) in enumerate(p_ord):
    id_map[i] = idx

events = []
for idx,(a,t,i) in enumerate(p_ord):
    update(idx,idx+1,a)
    events.append((t,i,0))

for i,x in enumerate(r):
    d = x - (r[i-1] if i > 0 else 0)
    events.append((x,-1,d))

events.sort()

ans = [0]*Q
L, R = 0, Q-1
start, sign = 0, '-'
for val, rawid, c in events:
    if rawid == -1:
        # Flip sign, advance start, update segment and boundary
        if sign == '-':
            update(L,R+1,-c)
            # Move L to next non-neg
            while L < R and query(L+1) < 0:
                L += 1
            aL = query(L)
            if aL < 0:
                update(L,L+1,-aL)
            start = val
            sign = '+'
        else:
            update(L,R+1,c)
            while L < R and query(R-1) > X:
                R -= 1
            aR = query(R)
            if aR > X:
                update(R,R+1,X-aR)
            start = val
            sign = '-'
    else:
        pid = rawid
        idx = id_map[pid]
        if sign == '-':
            if idx < L:
                res = max(query(L) - (val - start), 0)
            elif idx > R:
                res = max(query(R) - (val - start), 0)
            else:
                res = max(query(idx) - (val - start), 0)
        else:
            if idx < L:
                res = min(query(L) + (val - start), X)
            elif idx > R:
                res = min(query(R) + (val - start), X)
            else:
                res = min(query(idx) + (val - start), X)
        ans[pid] = res

print('\n'.join(map(str, (ans[i] for i in range(Q)) )) )