import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0]*n
        self.letter = [None]*n  # known letter or None

    def find(self,x):
        while self.par[x]!=x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return True
        # merge letter info
        lx,l y_let = self.letter[x],self.letter[y]
        if (lx is not None) and (y_let is not None) and (lx != y_let):
            return False  # contradiction impossible by problem statement
        if self.rank[x]<self.rank[y]:
            self.par[x]=y
            if self.letter[y] is None:
                self.letter[y]=self.letter[x]
        else:
            self.par[y]=x
            if self.letter[x] is None:
                self.letter[x]=self.letter[y]
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1
        return True

    def set_letter(self,x,c):
        x = self.find(x)
        l = self.letter[x]
        if l is not None and l != c:
            return False
        self.letter[x]=c
        return True

    def get_letter(self,x):
        x = self.find(x)
        return self.letter[x]

n,a,b,q = map(int,input().split())

fixed_pos = []
fixed_char = []
for _ in range(a):
    x,c = input().split()
    fixed_pos.append(int(x)-1)
    fixed_char.append(c)

ys = []
hs = []
for _ in range(b):
    y,h = map(int,input().split())
    ys.append(y-1)
    hs.append(h-1)

queries = [int(input())-1 for _ in range(q)]

# We'll only consider positions in fixed_pos and endpoints from duplicated substrings to build a graph,
# because n can be up to 10^9 and we only can store info about limited positions.

# endpoints: all starts and ends of blocks in duplicated substrings, and fixed positions, and query positions
points = set(fixed_pos)
points.update(queries)
for y in ys:
    points.add(y)
points.add(n)  # sentinel for end

# sort points and build mapping to compressed index
points = sorted(points)
comp_map = {p:i for i,p in enumerate(points)}
m = len(points)

uf = UnionFind(m)

# function to add union between two intervals of same length
def union_intervals(s1,e1,s2,e2):
    length = e1 - s1
    for i in range(length):
        uf.union(comp_map[s1+i],comp_map[s2+i])

# build intervals details from ys and hs
# intervals: start positions are ys + [n], each interval ends at next y or at n
interval_ends = ys[1:] + [n]
intervals = list(zip(ys, interval_ends, hs))

# For each pair of intervals where h != -1, unify corresponding letters
for s,e,h in intervals:
    if h == -1:
        continue  # h_i == -1 means hs[i] == -1, no duplication info
    length = e - s
    # The duplicated interval is [s,e), and identical to [h,h+length)
    # We'll union these intervals point by point using compressed coordinates
    # but only if these points are in comp_map (some positions may not be in points)
    # But all endpoints and fixed positions and queries are in points, so union only those
    # So we union all positions in these intervals that exist in compressed indices

    # positions to union are comp_map keys in range [s,e) intersected with points
    # But to keep complexity small, union intervals by stepping through points that are in this range
    # So we can proceed by scanning points and union where possible

    # Actually, since points is sorted, we can find all points in [s,e) and in [h,h+length)
    # Then union pairwise by offset index

    # get indices in points for s and e:
    si = comp_map[s]
    ei = comp_map[e]
    hi = comp_map[h]
    # Length in compressed indices may not be equal to actual length (because points are sparse)!
    # So the length in compressed indices can be less or equal to length,
    # but problem states all duplicates cover same lengths, so intervals must correspond in points

    # The intervals [s,e) and [h,h+length) correspond to same set of compressed indices from si to ei and hi to hi + (ei-si)
    length_comp = ei - si
    for i in range(length_comp):
        uf.union(si+i, hi+i)

# set known letters
for pos,c in zip(fixed_pos, fixed_char):
    uf.set_letter(comp_map[pos], c)

# answer queries
res = []
for z in queries:
    if z not in comp_map:
        # no info about this position
        res.append('?')
    else:
        c = uf.get_letter(comp_map[z])
        res.append(c if c is not None else '?')

print(''.join(res))