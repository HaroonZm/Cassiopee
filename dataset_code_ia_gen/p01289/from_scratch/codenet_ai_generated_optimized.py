import sys
import math

def solve():
    input = sys.stdin.readline
    while True:
        n,s,t = map(int, input().split())
        if n==0 and s==0 and t==0:
            break
        q = list(map(int, input().split()))
        a = [list(map(int, input().split())) for _ in range(n)]

        # Precompute shortest distances from each node to all others using Floyd-Warshall
        INF = 1e15
        dist = [[INF]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if a[i][j]>0:
                    dist[i][j] = a[i][j]
            dist[i][i] = 0
        for k in range(n):
            for i in range(n):
                di = dist[i]
                dik = di[k]
                dk = dist[k]
                for j in range(n):
                    if dik+dk[j]<di[j]:
                        di[j] = dik+dk[j]

        # Check if t reachable from s
        if dist[s-1][t-1]>=INF:
            print("impossible")
            continue

        # Build neighbors lists and precompute shortest edges from each node for sign nodes
        neighbors = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if a[i][j]>0:
                    neighbors[i].append(j)

        # For sign nodes, precompute the set of neighbors that lie on a shortest path to t
        sp_next = [set() for _ in range(n)]
        for i in range(n):
            if q[i]==1:
                d_i_t = dist[i][t-1]
                for nxt in neighbors[i]:
                    if a[i][nxt]+dist[nxt][t-1] == d_i_t:
                        sp_next[i].add(nxt)

        # State: (current_node, previous_node or -1)
        # - previous_node = -1 means start (no prev)
        # We'll number states as i*n + prev (prev from -1 to n-1; prev=-1 mapped to n)
        # total states = n*(n+1)
        max_prev = n
        size = n*(n+1)

        # Map (i,prev) => index
        def idx(i,prev):
            return i*(n+1)+ (prev if prev>=0 else n)

        # Build linear system: E[state] = expected dist to t from state
        # E[t, _] = 0 for all prev
        # For other states:
        # if i == t-1 => E=0
        # else:
        #   transitions depend on q[i]:
        #    if q[i]==1: go uniformly randomly to one of sp_next[i]
        #    else: go uniformly randomly to any neighbor (including prev)
        # Note: the graph may have loops even self-loops

        A = [[0.0]*size for _ in range(size)]
        B = [0.0]*size

        t0 = t-1
        for i in range(n):
            for prev in range(-1,n):
                row = idx(i,prev)
                if i==t0:
                    A[row][row] = 1.0
                    B[row] = 0.0
                    continue
                A[row][row] = 1.0
                # Determine next nodes and probabilities
                if q[i]==1:
                    nxts = sp_next[i]
                else:
                    nxts = neighbors[i]
                if not nxts:
                    # No way to move forward, infinite expected distance
                    # We'll put no solution: E=INF so print impossible
                    # Just make system unsolvable
                    # Set equation: E=INF impossible, put A[row][row]=1, B[row]=INF
                    # But better to detect this later by checking solutions
                    print("impossible")
                    break_flag=True
                    break
                deg = len(nxts)
                for nxt in nxts:
                    col = idx(nxt,i)
                    A[row][col] -= 1.0/deg
                    B[row] += a[i][nxt]* (1.0/deg)
            else:
                continue
            break
        else:
            # Solve linear system by Gaussian elimination with partial pivoting
            # size <= 101*101=10201 max but n=100 so 10100 states max (big but problem constraints)
            # Here limit states: n=100, max_prev=100 => size=10100 ~ acceptable optimized
            # We'll implement efficient Gaussian elimination for sparse system

            # Use dense Gaussian elimination
            # Convert to augmented matrix
            for irow in range(size):
                # Partial pivot
                pivot = irow
                for r2 in range(irow+1,size):
                    if abs(A[r2][irow]) > abs(A[pivot][irow]):
                        pivot = r2
                if abs(A[pivot][irow]) < 1e-14:
                    # Singular or no unique solution
                    print("impossible")
                    break
                if pivot != irow:
                    A[irow],A[pivot] = A[pivot],A[irow]
                    B[irow],B[pivot] = B[pivot],B[irow]
                pivot_val = A[irow][irow]
                for c in range(irow,size):
                    A[irow][c] /= pivot_val
                B[irow] /= pivot_val
                for r2 in range(size):
                    if r2 != irow and abs(A[r2][irow])>1e-14:
                        f = A[r2][irow]
                        for c in range(irow,size):
                            A[r2][c] -= f*A[irow][c]
                        B[r2] -= f*B[irow]
            else:
                # no break = solved
                E_s = B[idx(s-1,-1)]
                if E_s > 1e14 or E_s < 0: # sanity check (distance can't be negative)
                    print("impossible")
                else:
                    print(f"{E_s:.8f}")

solve()