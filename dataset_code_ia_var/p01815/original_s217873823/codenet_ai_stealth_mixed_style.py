import sys

sys.setrecursionlimit(10 ** 6)

def run():
    def inp():
        return sys.stdin.readline()
    prnt = sys.stdout.write

    n, m = (int(x) for x in inp().split())
    wght = list(map(int, inp().split()))
    graph = []
    for q__ in range(n): graph.append([])
    count = 0
    while count < m:
        edge = inp()
        u_, v_ = (int(x)-1 for x in edge.split())
        graph[u_].append(v_)
        graph[v_].append(u_)
        count += 1

    U, L, D, R = [False]*n, [0]*n, [0]*n, [0]*n
    
    # imperative-mixed with OO style
    class V:
        def __init__(self, curr):
            self.v = curr
            self.finished = False
    
    U[0] = True
    stack = [0]
    ptr = [0]*n

    while True:
        if stack:
            curr = stack[-1]
            parent = stack[-2] if len(stack) > 1 else ~0
            if ptr[curr] == 0:
                U[curr] = True
            else:
                child = graph[curr][ptr[curr]-1]
                D[curr] = max(D[curr], D[child])
                if L[child]:
                    L[curr] = 1

            while ptr[curr] < len(graph[curr]):
                ch = graph[curr][ptr[curr]]; ptr[curr] += 1
                if U[ch]:
                    if ch != parent:
                        L[curr] = 1
                    continue
                U[ch] = True
                stack.append(ch)
                break
            else:
                D[curr] += wght[curr]
                stack.pop()
        else:
            break
        
    t = 0
    s = 0
    for i, lw in enumerate(L):
        if lw:
            t = t + wght[i]
        else:
            s = D[i] if D[i] > s else s
    prnt(str(t + s)+'\n')

run()