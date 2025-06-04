from collections import deque
def main():
    n,m,a,b,c=map(int,input().split())
    edges=[[] for _ in range(n)]
    for _ in range(m):
        u,v=map(int,input().split())
        edges[u-1].append(v-1)
    steps=[a,b,c]

    # Precompute adjacency matrices for step counts a,b,c
    # Using matrix exponentiation by BFS for each step count
    def reachable_nodes(start, step):
        visited = [False]*n
        q = deque()
        q.append((start,0))
        visited_nodes = set()
        while q:
            u,d = q.popleft()
            if d==step:
                visited_nodes.add(u)
            elif d<step:
                for w in edges[u]:
                    q.append((w,d+1))
        return visited_nodes

    # For each node and each step count, precompute reachable nodes
    next_pos = [{} for _ in range(n)]  # next_pos[u][step] = set of reachable nodes from u in exactly step steps
    for u in range(n):
        for s in steps:
            next_pos[u][s] = reachable_nodes(u,s)
            # If no reachable nodes in exact s steps, empty set

    INF = 10**9
    # dp[turn][position]: minimal turns to reach goal from position after turn turns
    # However we want minimal turns to finish no matter what sequence of numbers brother choose
    # We use a value function V: minimal turns needed from node to reach goal no matter what choice of step in {a,b,c}
    # At each turn, brother chooses in {a,b,c}, we must be able to pick a move accordingly
    # So: V[u] = 0 if u == goal (n-1)
    # else V[u] = 1 + max over s in steps of min over v in next_pos[u][s] of V[v]
    # If for some s, next_pos[u][s] is empty -> we lose (IMPOSSIBLE)
    # Value iteration to find least fixed point

    V = [INF]*n
    V[n-1] = 0
    changed = True
    for _ in range(n*10):
        changed=False
        for u in range(n):
            if u==n-1:
                continue
            vals = []
            impossible = False
            for s in steps:
                reach = next_pos[u][s]
                if not reach:
                    impossible=True
                    break
                vals.append(min(V[v] for v in reach))
            if impossible:
                continue
            newV = 1+max(vals)
            if newV < V[u]:
                V[u]=newV
                changed=True
        if not changed:
            break

    print("IMPOSSIBLE" if V[0]==INF else V[0])
main()