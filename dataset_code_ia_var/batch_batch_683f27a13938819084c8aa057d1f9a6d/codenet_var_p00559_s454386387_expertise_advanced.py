from sys import stdin
from itertools import islice

def main():
    # Lecture de toutes les entrées en une fois pour rapidité
    it = iter(map(int, stdin.read().split()))
    n, q, s, t = (next(it) for _ in range(4))
    a = [next(it) for _ in range(n + 1)]
    diff = [a[i + 1] - a[i] for i in range(n)]
    score = lambda d: -s * d if d > 0 else -t * d
    res = sum(map(score, diff))
    out = []
    for _ in range(q):
        l, r, x = (next(it) for _ in range(3))
        l -= 1  # passage à l'indice 0-based
        bef = diff[l]
        diff[l] += x
        res += score(diff[l]) - score(bef)
        if r < n:
            bef_r = diff[r]
            diff[r] -= x
            res += score(diff[r]) - score(bef_r)
        out.append(str(res))
    print('\n'.join(out))

main()