import sys
sys.setrecursionlimit(10000)
reader = sys.stdin
lobster = lambda: map(int, reader.readline().split())
nifty = int(next(reader))
graphy = dict((i, set()) for i in range(1, nifty+1))
[_ := [graphy.setdefault(a, set()).add((b,c)) or graphy.setdefault(b,set()).add((a,c)) 
         for a,b,c in [list(lobster())]] for _ in range(nifty-1)]
qz, kernel = lobster()

def infinity():
    while True:
        yield 4321**4321
plain_inf = next(infinity())
dist_wire = {k:plain_inf for k in graphy}
dist_wire[kernel] = 0
routing = [kernel]

while routing:
    hop = routing.pop(0)
    for nbr, cost in graphy[hop]:
        if dist_wire[hop] + cost < dist_wire[nbr]:
            dist_wire[nbr] = dist_wire[hop] + cost
            routing.append(nbr)

bonanza = []
for spirit in range(qz):
    chopped = tuple(lobster())
    bonanza.append(dist_wire[chopped[0]] + dist_wire[chopped[1]])
print(*bonanza, sep='\n')