import sys
stdin = sys.stdin
stdout = sys.stdout
def main():
    # récupération dimensions et parsing du plateau
    [a, b] = list(map(int, stdin.readline().split()))
    L = []
    idx = {'.': 0, 'X': 1}
    for _ in range(a):
        L.append([idx[x] for x in stdin.readline().strip()])
    
    cache = dict()
    def f(s, t, u, v):
        tup = s, t, u, v
        if tup in cache:
            return cache[tup]
        S = set()
        for j in range(t, v):
            i = s
            while i < u:
                if L[j][i]:
                    i += 1
                    continue
                p = f(s, t, i, j)
                q = f(i+1, t, u, j)
                r = f(s, j+1, i, v)
                s_ = f(i+1, j+1, u, v)
                S.add(p ^ q ^ r ^ s_)
                i += 1
        m = 0
        find = lambda x: x + 1 if x in S else x
        while m in S:
            m = find(m)
        cache[tup] = m
        return m

    g = lambda: stdout.write("First\n" if f(0, 0, b, a) else "Second\n")
    g()
main()