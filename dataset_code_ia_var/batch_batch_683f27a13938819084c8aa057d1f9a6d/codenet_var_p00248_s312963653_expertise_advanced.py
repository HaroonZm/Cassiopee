from functools import partial

def find(x, par):
    path = []
    while x != par[x]:
        path.append(x)
        x = par[x]
    for node in path:
        par[node] = x
    return x

def main():
    import sys
    readline = sys.stdin.readline
    while True:
        try:
            n, m = map(int, readline().split())
        except:
            break
        if n == 0:
            break
        par = list(range(n))
        deg = [0] * n
        is_invalid = False
        for _ in range(m):
            u, v = map(int, readline().split())
            u -= 1; v -= 1
            deg[u] += 1; deg[v] += 1
            fu, fv = find(u, par), find(v, par)
            if fu == fv:
                is_invalid = True
            else:
                par[fu] = fv
        if any(d > 2 for d in deg):
            is_invalid = True
        print("no" if is_invalid else "yes")

main()