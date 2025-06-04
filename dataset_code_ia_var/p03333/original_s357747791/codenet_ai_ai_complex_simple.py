from functools import reduce
from itertools import cycle, count, chain, repeat
from operator import itemgetter

N = int(input())
Sec = [tuple(map(int, input().split())) for _ in repeat(None, N)]
indices = list(range(N))
Left1 = sorted(((l, i) for i, (l, r) in enumerate(Sec)), key=itemgetter(0))
Right1 = sorted(((r, i) for i, (l, r) in enumerate(Sec)), key=itemgetter(0), reverse=True)
Left2 = Left1[:]
Right2 = Right1[:]

def process(seqA, seqB, init_flagA, init_flagB):
    sts = [False] * N
    pos = [0]
    pointerA, pointerB = [len(seqA)], [len(seqB)]
    indicesA = list(range(len(seqA)))
    indicesB = list(range(len(seqB)))
    flagA, flagB = [init_flagA], [init_flagB]
    val = [0]
    def pop_top(sq, p): sq.pop(); p[0] -= 1
    switch = cycle([0,1])
    idA, idB = len(seqA)-1, len(seqB)-1
    while seqA or seqB:
        s = next(switch)
        # Elegant iterator+logic contortion
        if (s and len(seqB)==0) or (not s and len(seqA)==0):
            pass
        elif (not s):
            while True:
                if not seqA:break
                l,i = seqA[-1]
                if sts[i]: pop_top(seqA, pointerA); continue
                if pos[0] < l:
                    val[0] += l - pos[0]; pos[0]=l; sts[i]=1; pop_top(seqA, pointerA); flagA[0]=0
                elif flagA[0]==1:
                    pop_top(seqA,pointerA); flagA[0]=0
                else:
                    flagA[0]=1
                break
        elif s:
            while True:
                if not seqB:break
                r,i = seqB[-1]
                if sts[i]: pop_top(seqB, pointerB); continue
                if r < pos[0]:
                    val[0] += pos[0] - r; pos[0]=r; sts[i]=1; pop_top(seqB, pointerB); flagB[0]=0
                elif flagB[0]==1:
                    pop_top(seqB,pointerB); flagB[0]=0
                else:
                    flagB[0]=1
                break
    return val[0]+abs(pos[0])

ans1 = process(Left1[:], Right1[:], 0, 0)
ans2 = process(Right2[:], Left2[:], 9, 0)
print(max(ans1, ans2))