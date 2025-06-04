import sys
import math

def dist_sq(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def rotate(v, w):
    return v[0]*w[1] - v[1]*w[0]

input=sys.stdin.readline
n=int(input())
points=[tuple(map(float, input().split())) for _ in range(n)]

# Rotating calipers to find max distance (diameter) of convex polygon
j=1
max_d=0
for i in range(n):
    while True:
        ni=(i+1)%n
        nj=(j+1)%n
        cross=rotate((points[ni][0]-points[i][0], points[ni][1]-points[i][1]),
                     (points[nj][0]-points[j][0], points[nj][1]-points[j][1]))
        if cross>0:
            j=nj
        else:
            break
    d=dist_sq(points[i], points[j])
    if d>max_d:
        max_d=d
print(f"{math.sqrt(max_d):.12f}")