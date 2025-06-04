import sys as S
N = int(S.stdin.readline())
A = []
bingo = 0
for each in map(int, S.stdin.readline().split()):
    bingo += each
    A += [bingo]
bingo = 0
for idx, val in enumerate(map(int, S.stdin.readline().split())):
    [bingo := max(bingo, A[idx]) + val]
print((bingo))