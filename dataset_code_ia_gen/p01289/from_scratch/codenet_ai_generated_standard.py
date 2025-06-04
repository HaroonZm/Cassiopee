import sys
import math

def floyd_warshall(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] < math.inf and dist[k][j] < math.inf:
                    nd = dist[i][k] + dist[k][j]
                    if nd < dist[i][j]:
                        dist[i][j] = nd

def solve():
    input=sys.stdin.readline
    while True:
        n,s,t = map(int,input().split())
        if n==0 and s==0 and t==0:
            break
        q = list(map(int,input().split()))
        a = [list(map(int,input().split())) for _ in range(n)]
        dist = [[math.inf]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if a[i][j]>0:
                    dist[i][j] = a[i][j]
            dist[i][i] = 0
        floyd_warshall(n, dist)
        if dist[s-1][t-1]==math.inf:
            print("impossible")
            continue
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if a[i][j]>0:
                    adj[i].append((j,a[i][j]))
        M = n*2
        # Variables: E(i,p) expected distance from node i coming from p (p in -1..n-1)
        # We'll encode p=-1 as index n
        idx = lambda i,p: i*(n+1)+(p+1)
        size = n*(n+1)
        A = [[0.0]*(size) for _ in range(size)]
        B = [0.0]*size
        for i in range(n):
            for p in range(-1,n):
                row = idx(i,p)
                if i == t-1:
                    A[row][row] = 1.0
                    B[row] = 0.0
                    continue
                edges = adj[i]
                if not edges:
                    # Dead end, no way to go
                    # expectation infinite, system unsolvable or no solution
                    # Let's put E=0 to avoid singular, will test later
                    A[row][row] = 1.0
                    B[row] = 0.0
                    continue
                if q[i]==1:
                    # With sign: go only to neighbors on shortest path to t
                    min_dist = math.inf
                    for (nx,dst) in edges:
                        cand = dst + dist[nx][t-1]
                        if cand < min_dist:
                            min_dist = cand
                    nxt_candidates = []
                    for (nx,dst) in edges:
                        if abs(dst + dist[nx][t-1] - min_dist)<1e-14:
                            nxt_candidates.append((nx,dst))
                else:
                    # No sign: choose among all edges uniformly
                    nxt_candidates = edges
                k = len(nxt_candidates)
                if k == 0:
                    # No way to progress
                    A[row][row]=1.0
                    B[row]=0.0
                    continue
                A[row][row]=1.0
                p_idx = p
                for (nx,dst) in nxt_candidates:
                    # next state is (nx, i)
                    col = idx(nx,i)
                    A[row][col] += -1.0/k
                    B[row] += dst/k
        # Solve linear system A x = B
        # Gaussian elimination
        for i in range(size):
            pivot = i
            for r in range(i+1,size):
                if abs(A[r][i]) > abs(A[pivot][i]):
                    pivot = r
            if abs(A[pivot][i]) < 1e-16:
                # Singular matrix
                # Means no solution or infinite expectation
                # Print impossible
                print("impossible")
                break
            if pivot != i:
                A[i],A[pivot] = A[pivot],A[i]
                B[i],B[pivot] = B[pivot],B[i]
            inv = 1.0/A[i][i]
            for j in range(i,size):
                A[i][j] *= inv
            B[i] *= inv
            for r in range(size):
                if r!=i and abs(A[r][i])>1e-16:
                    factor = A[r][i]
                    for c in range(i,size):
                        A[r][c] -= factor*A[i][c]
                    B[r] -= factor*B[i]
        else:
            # Solution found
            res = B[idx(s-1,-1)]
            if math.isinf(res) or math.isnan(res) or res > 1e18:
                print("impossible")
            else:
                print(f"{res:.8f}")

if __name__=="__main__":
    solve()