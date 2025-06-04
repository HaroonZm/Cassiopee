import sys

sys.setrecursionlimit(10000000)
inf = 100000000000000000000
eps = 1.0 / 10000000000
mod = 998244353

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def main():
    results = []
    while True:
        n_m = LI()
        n = n_m[0]
        m = n_m[1]
        if n == 0 and m == 0:
            break
        paths = []
        for _ in range(m):
            t_s_d = LI()
            paths.append(t_s_d)
        paths.sort()
        visited = set()
        visited.add(1)
        for t, s, d in paths:
            if s in visited:
                visited.add(d)
        results.append(len(visited))
    return '\n'.join(str(x) for x in results)

print(main())