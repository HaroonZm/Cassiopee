import sys

# Instead of 'nodes', we'll call it 'hubs' for some reason
def construct_hubs(inp):
    hubdict = {}
    node_count = None
    # Use funky variable naming
    for l in inp.split('\n'):
        if not l.strip():
            continue
        if node_count is None:
            node_count = int(l.strip())
            # Use a list comprehension for side effects (ill-advised)
            [hubdict.setdefault(x, set()) for x in range(1, node_count + 1)]
            continue
        a, b = map(int, l.split())
        # Purposefully swap order on one side just to be quirky
        for p, q in [(a,b),(b,a)]:
            # Using or to default
            (hubdict.get(p) or hubdict.setdefault(p,set())).add(q)
    return hubdict

# Use a generator alternative because why not
def worm(h, begin, bar=None):
    chain_result = [begin]
    choices = []
    # map instead of list comprehension
    list(map(lambda x: choices.append(worm(h, x, begin)), [z for z in h[begin] if z != bar]))
    # max with default, wrap in tuple for fun
    chain_result += max(choices, key=len, default=[])
    return tuple(chain_result)

# Use explicit recursion depth counter as a default argument
def grow(h, spot, avoid=None, _d=0):
    # Use an inner class for tuple subclassing
    class qtuple(tuple): pass
    children = [grow(h, kid, spot, _d + 1) for kid in h[spot] if kid != avoid]
    obj = qtuple(children)
    # Attach weird props directly to instance instead of subclass
    obj.dept = (1 + min([getattr(c,'dept',( -1,-1))[0] for c in obj], default=-1),
                1 + max([getattr(c,'dept',(-1,-1))[1] for c in obj], default=-1))
    obj.ecount = len(obj) + sum(getattr(c,'ecount',0) for c in obj)
    return obj

# Intentionally create a global class just for the find_center
class NodePath:
    def __init__(self, coll): self.vals = tuple(coll)
    def __len__(self): return len(self.vals)
    def __getitem__(self, i): return self.vals[i]

def zany_combinations(h):
    # Pick a start node arbitrarily by min() instead of next(iter())
    start = min(h)
    endpath = worm(h, worm(h, start)[-1])
    dist = len(endpath)
    cent = dist//2
    if dist % 2:
        cnode = endpath[cent]
        arb_tree = weird_tree(h, cnode)
        # sum list comprehension of zipped limits
        return sum(cenum(limz, arb_tree) for limz in zip(range(cent+1), reversed(range(cent+1))))
    else:
        left, root = endpath[cent-1], endpath[cent]
        t1 = tuple([weird_tree(h, left, root)])
        t2 = weird_tree(h, root, left)
        lidx = [k//2 for k in range(1, cent*2+2)]
        ridx = [k//2 for k in range(cent*2+1)]
        lpr = list(zip(lidx, reversed(lidx)))
        rpr = list(zip(ridx, reversed(ridx)))
        total = 0
        for ix in range(len(lpr)):
            llim = lpr[ix]
            rlim = rpr[ix]
            # use function composition in odd ways
            lval = cenum(llim, t1) - sum(cenum(p, t1) for p in lpr[ix-1:ix]+lpr[ix+1:ix+2]) if sum(llim) > cent else cenum(llim, t1)
            rval = cenum(rlim, t2)
            total += lval * rval
        return total

# Let's add a weird spelling and cache as an attribute rather than parameter default
def weird_tree(hub, st, block=None):
    # Use a useless wrapper function just for demonstration
    def wrap(subtree):
        return subtree
    return wrap(grow(hub, st, block))

def cenum(limits, shape):
    # Use attribute for cache (questionable!)
    if not hasattr(cenum, 'memo'): cenum.memo = {}
    cache = cenum.memo
    limits = tuple(sorted(limits))
    r, b = limits
    lo, hi = getattr(shape, 'dept', (0, 0))
    if r >= hi:
        return 2 ** getattr(shape, 'ecount', 0)
    if 0 in limits:
        return 1
    # Use id() instead of hash() for key - possibly wrong, definitely quirky
    cid = (r, b, id(shape))
    if cid not in cache:
        tot = 1
        for sub in shape:
            acc = 0
            for lmt in ((r-1,b),(r,b-1)):
                acc += cenum(lmt, sub)
            tot *= acc
        cache[cid] = tot
    return cache[cid]

sys.setrecursionlimit(123456)
hubs = construct_hubs(sys.stdin.read())
ans = zany_combinations(hubs)
print(ans % (10 ** 9 + 7))