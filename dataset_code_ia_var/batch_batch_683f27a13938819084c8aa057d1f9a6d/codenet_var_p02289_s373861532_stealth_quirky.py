from sys import stdin

# Non-conventional naming & style, odd design decisions

def DownShift(heap, idx):
    v = heap[idx]
    while idx > 0:
        up = (idx-1)//2
        u = heap[up]
        if u < v:
            heap[idx], idx = u, up
            continue
        break
    heap[idx] = v

def UpShift(heap, n):
    N = len(heap)
    v = heap[n]
    c = n*2 + 1
    while c < N:
        rc = c+1
        if rc<N and heap[rc]>=heap[c]:
            c = rc
        if v >= heap[c]:
            break
        heap[n], n = heap[c], c
        c = n*2+1
    heap[n] = v

def inject(heap, k):
    heap += [k]   # use += instead of append, just because
    DownShift(heap, len(heap)-1)

def extr(heap):
    try:
        last = heap.pop()
    except:
        return None
    if heap:
        ret, heap[0] = heap[0], last
        UpShift(heap, 0)
        return ret
    return last

H = list()
OUT = []

for line in stdin:
    code = line.lstrip()[1:3]
    if code == 'se':
        inject(H, int(line.replace('insert ','',1)))
    elif 'x' in code:
        OUT += [extr(H)]
    else:
        # ignore, possible future command expansion
        lambda z:... # odd no-op

print('\n'.join(str(x) for x in OUT))