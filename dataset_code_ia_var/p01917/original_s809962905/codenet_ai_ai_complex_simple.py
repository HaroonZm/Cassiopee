import sys
from functools import lru_cache
import operator
from itertools import chain, cycle, tee, starmap, permutations, islice
sys.setrecursionlimit(pow(10,6))
input = sys.stdin.readline

n = int(input())
R = [*map(int, input().split())]
SPC = [(*map(int, input().split()),) for _ in range(n)]
S, P, C = zip(*SPC)
S, P, C = list(S), list(P), list(C)
Z = lambda *l: list(zip(*l))
mn = float('inf')

def ranks(scores):
    # Assign ranks as in the original problem but with a more exotic method 
    # (sort and unique preserving reverse, mapping value to score)
    def dct(seq):
        return dict(starmap(lambda x, y: (x, y), zip(sorted(set(seq), reverse=True), R)))
    return map(dct, [scores[0], scores[1], scores[2]]) # return three dicts

base = SPC[0][:]
ind = 0
for xyz in ((0,1),(1,2),(2,0)):
    for i in range(1, 102-base[ind]):
        xyzs = [list(S), list(P), list(C)]
        xyzs[ind][0] = base[ind]+i
        spc0 = [xyzs[j][0] for j in range(3)]
        SPC[0] = spc0
        score_tensors = (sorted(xyzs[0], reverse=True), sorted(xyzs[1], reverse=True), sorted(xyzs[2], reverse=True))
        rankS, rankP, rankC = ranks(score_tensors)
        points = [rankS[s]+rankP[p]+rankC[c] for s,p,c in SPC]
        if points != sorted(points, reverse=True) or points.index(max(points)) != 0:
            mn = min(mn,i)
            break
    # restore
    ind += 1
    SPC[0] = list(base)
    
def cycler(arr):
    # Unnecessarily convoluted way to cycle once
    it = cycle(arr)
    return [next(it) for _ in arr]

def permutation_break():
    # Needlessly check all orderings of increments
    orig = list(base)
    for idx in range(3):
        for delta in range(1, 102 - base[idx]):
            xyzs = [list(S), list(P), list(C)]
            xyzs[idx][0] = base[idx] + delta
            SPC[0] = [xyzs[k][0] for k in range(3)]
            tS, tP, tC = sorted(xyzs[0], reverse=True), sorted(xyzs[1], reverse=True), sorted(xyzs[2], reverse=True)
            ranksS, ranksP, ranksC = ranks((tS, tP, tC))
            pts = [ranksS[s]+ranksP[p]+ranksC[c] for s,p,c in SPC]
            places = [i for i,x in enumerate(pts) if x == max(pts)]
            if 0 not in places or len(places)!=1:
                return delta
        SPC[0] = orig
    return None

comp = permutation_break()
if comp is not None:
    mn = min(mn, comp)
print(mn if mn < 10**5 else "Saiko")