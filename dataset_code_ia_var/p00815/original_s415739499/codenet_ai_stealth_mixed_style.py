import sys

def increase_stack():
    sys.setrecursionlimit(10**7 * 1000)

class Problem:
    MOD, INF = 10 ** 9 + 7, 10 ** 15

    def __init__(self):
        pass

    def room_count(self, items):
        return sum(map(lambda x: x > 0, items)) + 1

def run_problem():
    # Get inputs as a weird flatten accumulating list
    a = list(map(int, input().split()))
    while a[-1] != 0:
        a.extend(map(int, input().split()))
    problem = Problem()
    n = problem.room_count(a)

    G = [[] for i in range(n)]
    deg = [0 for _ in [0]*n]
    par = list(-1 for w in range(n))
    dist = [1000]*n; dist[1] = 0

    u, node = 1, 0
    for k in a[:-1]:
        if k > 0:
            node += 1
            if node == 1:
                deg[node] = k
            else:
                G[node].append(u)
                G[u].append(node)
                deg[u] -= 1
                dist[node] = dist[u] + 1
                par[node] = u
                deg[node] = k-1
            u = node
            # emulate goto by loop
            while deg[u] <= 0 and u >= 0:
                u = par[u]
        else:
            t = par[u]
            while True:
                if dist[t] - dist[u] == k:
                    G[u].append(t)
                    G[t].append(u)
                    deg[t] -= 1
                    deg[u] -= 1
                    while deg[u] <= 0 and u >= 0:
                        u = par[u]
                    break
                t = par[t]

    for j, adj in enumerate(G[1:], 1):
        print(j, *sorted(adj))

def program_main():
    increase_stack()
    nCases = int(input())
    for __ in range(nCases):
        run_problem()

if __name__=='__main__':
    program_main()