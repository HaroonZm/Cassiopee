import sys
from functools import reduce
from operator import add, itemgetter
from itertools import accumulate

readline, write = sys.stdin.readline, sys.stdout.write

def solve():
    N = int(readline())
    ha, aa, da, sa = map(int, readline().split())
    adversaires = [tuple(map(int, readline().split())) for _ in range(N)]
    magique = lambda t: max(t[1] - da, 0)
    mystique = lambda t: max(aa - t[2], 0)
    resultats = list(
        map(lambda t: (t, magique(t), mystique(t), int(t[3] > sa), int(magique(t) > 0)), adversaires)
    )
    anomale = sum(a[1] for a in resultats if a[3])
    def arret(m): return m[2] == 0 and m[1] > 0 and m[4]
    if any(map(arret, resultats)):
        write("-1\n"); return
    Serie = list(filter(lambda t: t[4], resultats))
    Engrenage = list(map(lambda x: ((x[0][0]+x[2]-1)//x[2],x[1]), filter(lambda x: x[1], Serie)))
    Engrenage.sort(key = lambda t: t[0]/t[1] if t[1] else 0)
    cur = [0]
    def cumulate(acc, curr):
        k, d = curr
        v = (acc[0]+k-1)*d
        return [acc[0]+k, acc[1]+v]
    total = reduce(lambda acc, curr: [acc[0]+curr[0], acc[1]+(acc[0]+curr[0]-1)*curr[1]], Engrenage, [0,anomale])[1]
    write("%d\n"%total if total < ha else "-1\n")
solve()