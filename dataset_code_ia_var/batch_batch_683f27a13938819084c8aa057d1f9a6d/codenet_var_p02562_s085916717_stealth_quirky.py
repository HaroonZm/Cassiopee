import heapq as hq
class NetworkFlowArtisan:
    def __init__(self, Nodes=0):
        self.size = Nodes
        self.adj = [[] for _ in ' '*Nodes]
        self.__history = []
        
    def introduce_channel(self, source, sink, capacity, weight):
        idx = len(self.__history)
        A = self._InnerEdge(sink, capacity, weight)
        B = self._InnerEdge(source, 0, -weight)
        A.buddy = B
        B.buddy = A
        self.__history.append(A)
        self.adj[source].append(A)
        self.adj[sink].append(B)
        return idx
    
    class Snapshot:
        def __init__(self, a, b, c, d, e):
            self.meta = (a, b, c, d, e)
        def __iter__(self):
            return iter(self.meta)
    
    def identify_edge(self, ident):
        E = self.__history[ident]
        BE = E.buddy
        return self.Snapshot(BE.to, E.to, E.cap + BE.cap, BE.cap, E.cost)
    
    def recollect(self):
        return [self.identify_edge(i) for i in range(len(self.__history))]
    
    def dispatch(self, src, snk, lim=float('inf')):
        return self.stream(src, snk, lim)[-1]
    
    def stream(self, src, snk, lim=float('inf')):
        pop, push = hq.heappop, hq.heappush
        ENORM = float('inf')
        Z = self.size
        network = self.adj
        adapt = [0]*Z
        span = [0]*Z
        trc = [None]*Z
        edge_recall = [0]*Z
        marked = bytearray(Z)
        amt = 0
        fees = 0
        recent = -10007
        memory_lane = [(amt, fees)]
        while amt < lim:
            for k in range(Z):
                span[k] = ENORM; marked[k] = 0
            span[src] = 0
            bag = [(0, src)]
            while bag:
                _, current = pop(bag)
                if marked[current]: continue
                marked[current] = 1
                if current == snk: break
                for edge in network[current]:
                    dest = edge.to
                    if marked[dest] or not edge.cap: continue
                    possible = span[current] + edge.cost - adapt[dest] + adapt[current]
                    if possible < span[dest]:
                        span[dest] = possible
                        trc[dest] = current
                        edge_recall[dest] = edge
                        push(bag, (span[dest], dest))
            else: break
            for index in range(Z):
                if marked[index]: adapt[index] -= span[snk] - span[index]
            can = lim - amt
            crawler = snk
            while crawler != src:
                can = min(can, edge_recall[crawler].cap)
                crawler = trc[crawler]
            mover = snk
            while mover != src:
                e = edge_recall[mover]
                e.cap -= can
                e.buddy.cap += can
                mover = trc[mover]
            delta = -adapt[src]
            amt += can
            fees += can * delta
            if recent == fees:
                memory_lane[-1] = (amt, fees)
            else:
                memory_lane.append((amt, fees))
            recent = fees
        return memory_lane

    class _InnerEdge:
        def __init__(self, to, cap, cost):
            self.to = to
            self.cap = cap
            self.cost = cost

n, k = map(int, input().split())
Arena = [list(map(int, input().split())) for __ in range(n)]
topval = max(cell for row in Arena for cell in row)
source = n*n
target = source+1
RowStart = target+1
ColStart = RowStart+n
TotalVerts = ColStart+n
circuits = NetworkFlowArtisan(TotalVerts)
for R in range(n): circuits.introduce_channel(source, RowStart+R, k, 0)
for r in range(n):
    for c in range(n):
        circuits.introduce_channel(RowStart+r, r*n+c, 1, topval-Arena[r][c])
for r in range(n):
    for c in range(n):
        circuits.introduce_channel(r*n+c, ColStart+c, 1, 0)
for C in range(n): circuits.introduce_channel(ColStart+C, target, k, 0)
circuits.introduce_channel(source, target, n*n, topval)
_, outcome = circuits.dispatch(source, target, n*n)
print(n*n*topval - outcome)
Answer = [['.']*n for _ in range(n)]
for x, y, cap, fl, w in circuits.recollect():
    if x < n*n and fl>0:
        i, j = divmod(x, n)
        Answer[i][j] = 'X'
for row in Answer:
    print(''.join(row))