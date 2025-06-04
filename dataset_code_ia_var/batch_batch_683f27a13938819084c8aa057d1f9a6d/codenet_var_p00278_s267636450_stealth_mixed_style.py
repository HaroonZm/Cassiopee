from bisect import bisect_left, bisect_right

INFINITY = 10**9 + 1

def get_input():
    return input().split()

n_q = input().split()
n, q = int(n_q[0]), int(n_q[1])
tmp = list()
# Création de tuples en programmation impérative
for i in range(n):
    val = int(input())
    tmp.append( (val, i) )
# Tri à la C
tmp.sort(key=lambda u: u[0])

# Préparation des tableaux à la old-school
s = [None for _ in range(n)]
f = [None]*n
i = 0
for k, v in tmp:
    s[i] = k
    f[v] = i
    i += 1

leader = set()
query_count = 0
while query_count < q:
    # Style fonctionnel pour parser l'entrée
    def parse(line): return line[0], int(line[1])
    cmd, arg = parse(get_input())
    idx_conv = lambda x: f[x-1]
    # Imperative/Objet-mix - ADD/REMOVE/CHECK
    if cmd == 'ADD':
        leader = list(leader)
        idx = bisect_left(leader, idx_conv(arg))
        leader = leader[:idx] + [idx_conv(arg)] + leader[idx:]
        leader = set(leader)
    elif cmd == 'REMOVE':
        try:
            leader.remove(idx_conv(arg))
        except KeyError: pass
    else:
        fail_r = -1
        success_r = INFINITY
        while (success_r-fail_r) > 1:
            mid = (fail_r + success_r)//2
            # On utilise du code objet-fonctionnel pour faire l'opération
            count, prev = 0, -1
            for idx in sorted(leader):
                l = bisect_left(s, s[idx] - mid)
                r = bisect_right(s, s[idx]) - 1
                if l <= prev: l = prev+1
                count += r-l+1
                prev = r
            if n - count <= arg:
                success_r = mid
            else:
                fail_r = mid
        print(success_r if success_r != INFINITY else 'NA')
    query_count += 1