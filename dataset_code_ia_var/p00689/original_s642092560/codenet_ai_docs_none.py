import math

def getangle(pointstart, pointend):
    sx, sy = pointstart
    ex, ey = pointend
    return math.atan2(ey - sy, ex - sx)

def getdistance(pointstart, pointend):
    sx, sy = pointstart
    ex, ey = pointend
    return math.hypot(ex - sx, ey - sy)

while 1:
    n = int(raw_input())
    if n == 0:
        break
    pointsnotyet = []
    for i in range(n):
        pointsnotyet.append([int(x) for x in raw_input().split()])
    pointstart = [0, 0]
    angle = math.pi / 2
    ans = 0
    for i in range(n):
        pointangle = getangle(pointstart, pointsnotyet[0])
        diff = -pointangle + angle
        if diff < 0:
            diff += math.pi * 2
        candidateangle = diff
        candidatedistance = getdistance(pointstart, pointsnotyet[0])
        candidateindex = 0
        for j in range(1, len(pointsnotyet)):
            pointangle = getangle(pointstart, pointsnotyet[j])
            pointdistance = getdistance(pointstart, pointsnotyet[j])
            diff = -pointangle + angle
            if diff < 0:
                diff += math.pi * 2
            if diff < candidateangle:
                candidateangle = diff
                candidatedistance = pointdistance
                candidateindex = j
            elif diff == candidateangle and pointdistance < candidatedistance:
                candidateangle = diff
                candidatedistance = pointdistance
                candidateindex = j
        pointend = pointsnotyet.pop(candidateindex)
        ans += getdistance(pointstart, pointend)
        angle = getangle(pointstart, pointend)
        pointstart = pointend
    print round(ans, 1)