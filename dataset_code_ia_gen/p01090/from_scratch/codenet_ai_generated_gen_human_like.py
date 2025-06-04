import sys
sys.setrecursionlimit(10**7)

def find(par, x):
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x

def union(par, rank, x, y):
    x = find(par, x)
    y = find(par, y)
    if x == y:
        return False
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
    return True

def main():
    input = sys.stdin.readline
    while True:
        n,m,k= map(int, input().split())
        if n == 0 and m == 0 and k == 0:
            break
        edges = []
        for _ in range(m):
            u,v,w,l = input().split()
            u = int(u)
            v = int(v)
            w = int(w)
            # store edges with company info and cost
            # company A will be flagged as 0, company B as 1 to ease counting
            comp = 0 if l == 'A' else 1
            edges.append((w, comp, u, v))
        # We want to pick exactly k edges from A, and n-1-k edges from B
        # There may be several MSTs varying in chosen edges from A and B
        # Strategy: binary search the penalty on using A edges (or use DP)
        # We'll use binary search on an auxiliary variable x:
        # adjust cost = w + x if company is A else = w
        # For different x, MST picks different number of edges from A
        # For each x, MST can be found and we know the count of A edges
        # We search x so that MST has k edges from A.
        # Then compute the original cost (not adjusted)
        
        left, right = -10000, 10000
        ans = -1
        
        def mst(x):
            # adjust cost: w + x if A, w if B
            adj_edges = []
            for w, comp, u, v in edges:
                cw = w + x if comp == 0 else w
                adj_edges.append((cw, w, comp, u, v))
            adj_edges.sort(key=lambda e: e[0])
            par = [i for i in range(n+1)]
            rank = [0]*(n+1)
            countA = 0
            total_orig = 0
            num = 0
            for cw, w_orig, comp, u, v in adj_edges:
                if union(par, rank, u, v):
                    num += 1
                    total_orig += w_orig
                    if comp == 0:
                        countA += 1
                    if num == n-1:
                        break
            if num < n-1:
                return None,None
            return countA, total_orig
        
        # binary search to find if there's a MST with k A edges
        for _ in range(50):
            mid = (left+right)/2
            cA, cost = mst(mid)
            if cA is None:
                # not spanning tree, remove too small mid
                left = mid
                continue
            if cA < k:
                right = mid
            else:
                left = mid
        
        # after binary search left ~= right, try both ends around left to find best
        candidates = []
        for testX in [left, right, (left+right)/2]:
            cA, cost = mst(testX)
            if cA == k and cost is not None:
                candidates.append(cost)
        if candidates:
            ans = min(candidates)
        print(ans)

if __name__ == "__main__":
    main()