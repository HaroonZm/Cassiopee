import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
children = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    children[a].append(b)

MOD1, MOD2 = 10**9+7, 10**9+9
BASE1, BASE2 = 911, 3571

def hash_combine(h1,h2):
    return ((h1*BASE1 + h2) % MOD1, (h1*BASE2 + h2) % MOD2)

def hash_list(lst):
    h1 = 0
    h2 = 0
    for x in lst:
        h1 = (h1*BASE1 + x[0]) % MOD1
        h2 = (h2*BASE2 + x[1]) % MOD2
    return (h1,h2)

# returns:
# - depth_hash: hash of multiset of children subtrees depths (list of (depth, hash)) sorted by depth, then hash
# - profile: list of (depth, count) for this subtree
def dfs(u):
    if not children[u]:
        # leaf node: depth 0 with count 1
        # hash for depth 0: let's encode count=1 by hash(1), empty for others
        # profile: [(0,1)]
        return ( ((1,1),), [(0,1)] )
    # get children profiles
    child_profiles = []
    child_hashes = []
    for c in children[u]:
        c_hash, c_prof = dfs(c)
        child_profiles.append(c_prof)
        child_hashes.append(c_hash)
    # combine profiles by adding 1 to depths to represent depths from current root u
    # we merge all child_profiles shifted by +1 in depth and sum counts at same depths
    from collections import defaultdict
    depth_count = defaultdict(int)
    for prof in child_profiles:
        for d,cnt in prof:
            depth_count[d+1]+=cnt
    # current node has a node at depth 0
    depth_count[0]+=1
    # build sorted profile list
    profile = sorted(depth_count.items())
    # For hashing, build a multiset of (depth,hash) for children subtrees
    # But we don't have hashes per depth yet directly, so we recreate:
    # Instead, to distinguish subtrees by profile, we hash their profile list directly
    # We'll hash the profile list [(depth,count),...]
    # Encode it as a list of pairs, each pair is two ints (depth, count)
    # So we can combine depth and count nicely into a single int (e.g. (depth+1)*1e6+count)
    # But depths and counts can be large, keep separate hashing:
    hashable = []
    for d,cnt in profile:
        hashable.append( (d,cnt) )
    h = hash_list(hashable)
    return (h, profile)

hash_count = dict()

for i in range(N,0,-1):
    pass

# dfs returns hash of profile and profile list for each node
def main():
    from collections import defaultdict
    sys.setrecursionlimit(10**7)
    N=int(input())
    children=[[] for _ in range(N+1)]
    for _ in range(N-1):
        a,b=map(int,input().split())
        children[a].append(b)

    MOD1,MOD2=10**9+7,10**9+9
    BASE1,BASE2=911,3571

    def hash_list(lst):
        h1=h2=0
        for d,cnt in lst:
            h1=(h1*BASE1 + d) % MOD1
            h1=(h1*BASE1 + cnt) % MOD1
            h2=(h2*BASE2 + d) % MOD2
            h2=(h2*BASE2 + cnt) % MOD2
        return (h1,h2)

    def dfs(u):
        if not children[u]:
            # leaf node profile: [(0,1)]
            return ( (1,1), [(0,1)] )
        depth_count = dict()
        for c in children[u]:
            h,prof = dfs(c)
            for d,cnt in prof:
                depth_count[d+1] = depth_count.get(d+1,0) + cnt
        depth_count[0] = depth_count.get(0,0)+1
        profile = sorted(depth_count.items())
        h = hash_list(profile)
        return (h, profile)

    hash_freq = defaultdict(int)
    def collect(u):
        h,prof = dfs(u)
        hash_freq[h]+=1
        return h

    for i in range(1,N+1):
        # only compute once per node, so we use a postorder dfs
        # better to do a single dfs for all nodes - let's do that:
        pass

    # so revised: single dfs that returns hash per node and fills freq
    hash_freq.clear()
    def dfs2(u):
        if not children[u]:
            h=(1,1)
            hash_freq[h]+=1
            return h
        depth_count = dict()
        for c in children[u]:
            h_c = dfs2(c)
            # get profile from hash_freq? no
            # so we keep a memo of profile per node
            # but not needed, we only need profile counts per subtree, reimplement to get flattened profiles per node
            # no: we need profile from children, so we can store per node
            # Instead, we can do like before: each node store profile
        # We need to store profile per node, so keep as before
        # Let's separate storing profiles per node:

    # We need to store profile per node to avoid recomputing:
    profiles = [None]*(N+1)
    def dfs3(u):
        if not children[u]:
            profiles[u] = [(0,1)]
            return (1,1)
        depth_count = dict()
        for c in children[u]:
            h_c = dfs3(c)
            for d,cnt in profiles[c]:
                depth_count[d+1] = depth_count.get(d+1,0)+cnt
        depth_count[0] = depth_count.get(0,0)+1
        profile = sorted(depth_count.items())
        profiles[u] = profile
        h = hash_list(profile)
        hash_freq[h]+=1
        return h

    dfs3(1)
    # to handle nodes not in subtree of 1? No, all nodes in subtree of root

    # now compute pairs
    ans=0
    for v in hash_freq.values():
        ans += v*(v-1)//2
    print(ans)

main()