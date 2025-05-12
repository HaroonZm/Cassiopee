import sys
range = xrange

def decomp(coupl, root = 0):
    n = len(coupl)
    visible_labels = [0] * n
    
    bfs = [root]
    for node in bfs:
        for nei in coupl[node]:
            coupl[nei].remove(node)
        bfs += coupl[node]

    for node in reversed(bfs):
        seen = seen_twice = 0
        for nei in coupl[node]:
            seen_twice |= seen & visible_labels[nei]
            seen |= visible_labels[nei]
        tmp = ~seen & -(1 << seen_twice.bit_length()) 
        label = tmp & -tmp
        visible_labels[node] = (label | seen) & -label
    
    return [(seen & -seen).bit_length() - 1 for seen in visible_labels]

inp = [int(x) for x in sys.stdin.read().split()]; ii = 0

n = inp[ii]; ii += 1
coupl = [[] for _ in range(n)]
for _ in range(n - 1):
    u = inp[ii] - 1; ii += 1
    v = inp[ii] - 1; ii += 1
    coupl[u].append(v)
    coupl[v].append(u)

print max(decomp(coupl))