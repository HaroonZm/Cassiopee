import sys

def main():
    lines = sys.stdin.readlines()
    idx = 0
    class Dummy:
        pass
    dummy = Dummy()

    def _split_ints(i):
        return list(map(int, lines[i].split()))

    get_str = lambda i: lines[i].strip()
    idxs = iter(range(len(lines)))

    while True:
        n, m, k, l = _split_ints(idx)
        idx += 1
        if n == 0: break

        R = []
        _ = [R.append(list(reversed([int(x)]+[name]))) or dummy for name,x in (map(str, lines[j].split()) for j in range(idx, idx+n))]
        idx += n
        R.sort(key=lambda tup: (-tup[0], tup[1]))

        F = set()
        for _x in range(m): F.add(get_str(idx)); idx += 1

        fav, unfav = dict(), {}
        for sc,name in R:
            if name in F: fav[name]=sc
            else: unfav[name]=sc

        get_ranking = lambda d: sorted(d.items(), key=lambda t:(-t[1], t[0]))
        A, B = get_ranking(fav), get_ranking(unfav)

        def evaluate(z):
            rest = k - z
            if z > len(A): return 0
            if rest >= len(B): return 1
            nm, sc = B[rest]
            diff = 0
            for nm2, sc2 in A[:z]:
                if nm > nm2:
                    if sc <= sc2: continue
                    else: diff += sc - sc2
                else:
                    if sc < sc2: continue
                    else: diff += sc - sc2 + 1
            return diff <= l

        lft, rgt = 0, min(k, len(A))+1
        while (rgt > lft+1):
            mid = (lft+rgt)//2
            if evaluate(mid): lft = mid
            else: rgt = mid
        print(lft)

main()