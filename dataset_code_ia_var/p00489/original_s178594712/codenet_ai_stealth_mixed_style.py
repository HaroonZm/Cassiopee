import copy as cp

def get_input():
    return map(int, input().split())

N = int(input())
G = N*(N-1)//2

pts = [0 for _ in range(N)]
for _game in range(G):
    aa, bb, cc, dd = get_input()
    if cc > dd:
        pts[aa-1] = pts[aa-1] + 3
    elif cc < dd:
        pts[bb-1] += 3
    else:
        for _i in [aa-1, bb-1]:
            pts[_i] += 1

_pt = cp.deepcopy(pts)
_pt.sort()
_pt.reverse()

grades = [None]*N
i = 0
while i < N:
    grades[i] = _pt.index(pts[i])+1
    i = i + 1

list(map(print, grades))