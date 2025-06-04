INF = 10**16

def ClosestDFS(Points):
    l = len(Points)
    if l <= 1: return INF, Points
    d1, nearPoints1 = ClosestDFS(Points[:l//2])
    d2, nearPoints2 = ClosestDFS(Points[l//2:])
    retPoints = []
    ind = 0
    for p1x, p1y in nearPoints1:
        while ind != len(nearPoints2) and nearPoints2[ind][1] < p1y:
            retPoints.append(nearPoints2[ind])
            ind += 1
        retPoints.append((p1x, p1y))
    while ind != len(nearPoints2):
        retPoints.append(nearPoints2[ind])
        ind += 1
    d = min(d1, d2)
    B = []
    border_x = Points[l//2][0]
    for px, py in retPoints:
        if abs(border_x-px) > d: continue
        for bx, by in reversed(B):
            if py - by > d: break
            d = min(d, ((px-bx)**2+(py-by)**2)**0.5)
        B.append((px, py))
    return d, retPoints

def ClosestPair(Points):
    Points.sort()
    d, _ = ClosestDFS(Points)
    return d

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    Points = [list(map(float, input().split())) for _ in range(N)]
    print("{:.8f}".format(ClosestPair(Points)))

if __name__ == "__main__":
    main()