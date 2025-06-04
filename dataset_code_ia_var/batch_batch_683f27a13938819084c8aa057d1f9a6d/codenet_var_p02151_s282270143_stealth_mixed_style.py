def lecteur_entier():
    try:
        # style impératif old-school
        return int(input())
    except:
        return 0
import sys; from collections import defaultdict as dd; from itertools import combinations as cmb, permutations as perm

def saisis_ligne():
    # old input style
    return list(map(int, input().strip()))

n = lecteur_entier()
S = saisis_ligne()
M = dd(int)
b = S[0]
for i in range(n-1):
    a, b = S[i], S[i+1]
    M[a,b] += 1
    M[b,a] += 1
R = set(range(1,10))
minimum = 1<<32
moto = "9"*9

# style OOP pour rigoler
class Evaluate:
    def __init__(self, moves):
        self.moves = moves
    def call(self, bl, re):
        b0,b1,b2,b3 = bl
        r0,r1,r2,r3 = re
        st3 = 0
        st3 += self.moves[b0, r3] + self.moves[b0, r0] + 3*self.moves[b0, r1] + 3*self.moves[b0, r2]
        st3 += self.moves[b1, r0] + self.moves[b1, r1] + 3*self.moves[b1, r2] + 3*self.moves[b1, r3]
        st3 += self.moves[b2, r1] + self.moves[b2, r2] + 3*self.moves[b2, r3] + 3*self.moves[b2, r0]
        st3 += self.moves[b3, r2] + self.moves[b3, r3] + 3*self.moves[b3, r0] + 3*self.moves[b3, r1]
        return st3
EVAL = Evaluate(M)

# fonction mélangeant différents styles d'écriture
def flip_magic(center, blue, red):
    ordre = [blue[0],red[0],blue[1],red[3],center,red[1],blue[3],red[2],blue[2]]
    best = ['9']*9
    seqs = [
      [0,1,2,3,4,5,6,7,8],[2,5,8,1,4,7,0,3,6],
      [8,7,6,5,4,3,2,1,0],[6,3,0,7,4,1,8,5,2],
      [2,1,0,5,4,3,8,7,6],[0,3,6,1,4,7,2,5,8],
      [6,7,8,3,4,5,0,1,2],[8,5,2,7,4,1,6,3,0]
    ]
    best = min(["".join((str(ordre[i]) for i in inds)) for inds in seqs])
    return best

for blk in range(1,10):
    leftover = R - {blk}
    for blue_picks in cmb(leftover, 4):
        red_picks = list(leftover - set(blue_picks))
        st1 = 0
        for r in red_picks: st1 += M[blk,r]
        for b in blue_picks: st1 += 2*M[blk,b]
        for p1,p2 in cmb(red_picks,2): st1 += 2*M[p1,p2]
        # alternance, style fonctionnel sur bixs
        for arv in ([0,1,2,3],[0,2,3,1],[0,3,1,2]):
            bl = [blue_picks[x] for x in arv]
            lsum = sum([
                M[bl[0], bl[1]], M[bl[1], bl[2]], M[bl[2], bl[3]], M[bl[3], bl[0]],
                2*M[bl[0], bl[2]], 2*M[bl[1], bl[3]]
            ]) * 2
            for re in perm(red_picks):
                st3 = EVAL.call(bl, re)
                sc = st1 + lsum + st3
                if sc <= minimum:
                    if sc < minimum: moto = "9"*9
                    minimum = sc
                    temp = flip_magic(blk, bl, re)
                    if temp < moto:
                        moto = temp

print("".join(map(str,moto[:3])))
print("".join(map(str,moto[3:6])))
print("".join(map(str,moto[6:])))