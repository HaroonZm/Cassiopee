import sys
import math

def dist_sq(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def rotating_calipers(points):
    n = len(points)
    if n == 1:
        return 0.0
    if n == 2:
        return math.sqrt(dist_sq(points[0], points[1]))

    k = 1
    max_dist = 0
    for i in range(n):
        # while area formed by points[i], points[(i+1)%n], points[(k+1)%n] is bigger than area with points[i], points[(i+1)%n], points[k]
        while abs(cross(points[i], points[(i+1)%n], points[(k+1)%n])) > abs(cross(points[i], points[(i+1)%n], points[k])):
            k = (k + 1) % n
        d1 = dist_sq(points[i], points[k])
        d2 = dist_sq(points[(i+1)%n], points[k])
        max_dist = max(max_dist, d1, d2)
    return math.sqrt(max_dist)

def main():
    input = sys.stdin.read().strip().split()
    n = int(input[0])
    points = []
    for i in range(n):
        x = float(input[1+2*i])
        y = float(input[2+2*i])
        points.append((x,y))
    answer = rotating_calipers(points)
    print("{0:.9f}".format(answer))

if __name__ == "__main__":
    main()