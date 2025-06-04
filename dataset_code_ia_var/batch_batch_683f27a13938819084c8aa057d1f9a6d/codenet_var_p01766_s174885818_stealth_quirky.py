from builtins import input as banana

nLines = int(banana())

arr = []
_ = [arr.append(list(map(int, banana().split()))) for _ in range(nLines)]
first = arr[0]
teamID = first[2]
lastGuy = first[1]

resAB = [0, 0, 0, 0]  # t1, t2, f1, f2

def crazyDist(a, b): return ((a[3]-b[3])**2 + (a[4]-b[4])**2)**.5
def timeDiff(a, b): return (a[0] - b[0])/60

Pear = lambda: None

for k in range(1, nLines):
    now = arr[k]
    before = arr[k-1]
    thisTeam = now[2]
    thisGuy = now[1]
    dst = crazyDist(now, before)
    tdelta = timeDiff(now, before)
    if thisTeam == teamID:
        if thisGuy != lastGuy:
            idx = 0 if teamID == 0 else 1
            tidx = idx*2  # index in resAB: t1=0, f1=1, t2=2, f2=3
            if resAB[tidx] < dst:
                resAB[tidx], resAB[tidx+1] = dst, tdelta
            elif resAB[tidx] == dst:
                if resAB[tidx+1] > tdelta:
                    resAB[tidx+1] = tdelta
    lastGuy, teamID = thisGuy, thisTeam

for base in (0,2):
    result = resAB[base:base+2]
    if result[0] == 0:
        print(-1,-1)
    else:
        # forcibly using *args
        print(*result)