from sys import stdin
from operator import itemgetter

N = int(stdin.readline())
LRs = [(*map(int, stdin.readline().split()), i) for i in range(N)]
Ls = sorted(LRs, key=itemgetter(0))
Rs = sorted(LRs, key=itemgetter(1))

def travel(first_positive=True):
    done = [0]*N
    iL, iR = N-1, 0
    x, ans = 0, 0
    while True:
        if first_positive:
            # + direction
            while iL >= 0 and done[Ls[iL][2]]: iL -= 1
            if iL < 0: break
            if (xNext := Ls[iL][0]) < x: break
            ans += xNext - x
            x = xNext
            done[Ls[iL][2]] = 1
            # - direction
            while iR < N and done[Rs[iR][2]]: iR += 1
            if iR == N: break
            if x < (xNext := Rs[iR][1]): break
            ans += x - xNext
            x = xNext
            done[Rs[iR][2]] = 1
        else:
            # - direction
            while iR < N and done[Rs[iR][2]]: iR += 1
            if iR == N: break
            if x < (xNext := Rs[iR][1]): break
            ans += x - xNext
            x = xNext
            done[Rs[iR][2]] = 1
            # + direction
            while iL >= 0 and done[Ls[iL][2]]: iL -= 1
            if iL < 0: break
            if (xNext := Ls[iL][0]) < x: break
            ans += xNext - x
            x = xNext
            done[Ls[iL][2]] = 1
    return ans + abs(x)

print(max(travel(False), travel(True)))