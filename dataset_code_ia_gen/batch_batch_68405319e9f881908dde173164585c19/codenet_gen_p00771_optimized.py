import math
import sys

def can(h, anchors):
    z = h*h
    points = []
    for x,y,l in anchors:
        r = l*l - z
        if r < -1e-14:
            return False
        r = max(r,0)
        d = math.sqrt(r)
        points.append((x,y,d))
    # check no ropes cross:
    # Ropes do not cross if for every pair (i,j), distance(anchor_i,anchor_j) >= d_i + d_j
    n = len(points)
    for i in range(n):
        x1,y1,d1 = points[i]
        for j in range(i+1,n):
            x2,y2,d2 = points[j]
            dist = math.hypot(x2 - x1, y2 - y1)
            if dist + 1e-14 < d1 + d2:
                return False
    return True

def main():
    input = sys.stdin.readline
    while True:
        n = input()
        if not n:
            break
        n = n.strip()
        if n == '0':
            break
        n = int(n)
        anchors = []
        for _ in range(n):
            x,y,l = map(int,input().split())
            anchors.append((x,y,l))
        low, high = 0.0, 300.0
        for _ in range(60):
            mid = (low+high)/2
            if can(mid, anchors):
                low = mid
            else:
                high = mid
        print("%.7f"%low)
        
if __name__ == "__main__":
    main()