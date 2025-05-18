def inpl(): return list(map(int, input().split()))
from collections import defaultdict
from itertools import combinations, permutations

N = int(input())
S = list(map(int, input()))

move = defaultdict(int)
b = S[0]
for i in range(N-1):
    a, b = S[i], S[i+1]
    move[(a, b)] += 1
    move[(b, a)] += 1

R = set(list(range(1, 10)))
bestscore = 10**10
bestans = "9"*9

def calc_br(bl, re):
    b0, b1, b2, b3 = bl
    r0, r1, r2, r3 = re
    stage3 = 0
    stage3 += move[(b0, r3)] + move[(b0, r0)] + 3*move[(b0, r1)] + 3*move[(b0, r2)]
    stage3 += move[(b1, r0)] + move[(b1, r1)] + 3*move[(b1, r2)] + 3*move[(b1, r3)]
    stage3 += move[(b2, r1)] + move[(b2, r2)] + 3*move[(b2, r3)] + 3*move[(b2, r0)]
    stage3 += move[(b3, r2)] + move[(b3, r3)] + 3*move[(b3, r0)] + 3*move[(b3, r1)]
    return stage3
    
    
def fliplr(black, bl, re):
    order = [bl[0], re[0], bl[1],
             re[3], black, re[1],
             bl[3], re[2], bl[2]]
    best = [9] * 9
    ixss = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
            [2, 5, 8, 1, 4, 7, 0, 3, 6],
            [8, 7, 6, 5, 4, 3, 2, 1, 0],
            [6, 3, 0, 7, 4, 1, 8, 5, 2],
            [2, 1, 0, 5, 4, 3, 8, 7, 6],
            [0, 3, 6, 1, 4, 7, 2, 5, 8],
            [6, 7, 8, 3, 4, 5, 0, 1, 2],
            [8, 5, 2, 7, 4, 1, 6, 3, 0]]
    best = min(["".join([str(order[ix]) for ix in ixs]) for ixs in ixss])
    return best
    
    
for black in range(1, 10):
    remain = R.difference([black])
    for blue in combinations(remain, r=4):
        red = list(remain - set(blue))
        stage1 = 0
        for r in red:
            stage1 += move[(black, r)]
        for b in blue:
            stage1 += move[(black, b)] * 2
        for r1, r2 in combinations(red, 2):
            stage1 += move[(r1, r2)] * 2
    
        for bixs in [[0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]:
            bl = [blue[bix] for bix in bixs]
            stage2 = (move[(bl[0], bl[1])] +
                      move[(bl[1], bl[2])] +
                      move[(bl[2], bl[3])] +
                      move[(bl[3], bl[0])] +
                      move[(bl[0], bl[2])]*2 +
                      move[(bl[1], bl[3])]*2)*2
            
            for re in permutations(red, 4):
                stage3 = calc_br(bl, re)
                score = stage1 + stage2 + stage3
                #if score == 11:
                #    print(black, bl, re)
                #print(stage1, stage2, stage3)
                if score <= bestscore:
                    if score < bestscore:
                        bestans = "9"*9
                    bestscore = score
                    bestans = min(bestans, fliplr(black, bl, re))
print("".join((map(str, bestans[:3]))))
print("".join((map(str, bestans[3:6]))))
print("".join((map(str, bestans[6:]))))