import sys

input = sys.stdin.readline

def squared_dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def add_points(a, b):
    return (a[0]+b[0], a[1]+b[1])

def sub_points(a, b):
    return (a[0]-b[0], a[1]-b[1])

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        points = [tuple(map(int, input().split())) for _ in range(n)]
        point_set = set(points)
        max_area = 0

        # Pour chaque paire de points, on essaie de former un carré
        for i in range(n):
            for j in range(i+1, n):
                A = points[i]
                B = points[j]
                # vecteur AB
                dx = B[0]-A[0]
                dy = B[1]-A[1]
                # vecteur perpendiculaire à AB, rotation 90° dans un sens
                px1 = -dy
                py1 = dx
                # points C et D possibles pour faire le carré ABCD
                C1 = (B[0]+px1, B[1]+py1)
                D1 = (A[0]+px1, A[1]+py1)
                if C1 in point_set and D1 in point_set:
                    area = dx*dx + dy*dy
                    if area > max_area:
                        max_area = area

                # vecteur perpendiculaire à AB, rotation 90° dans l'autre sens
                px2 = dy
                py2 = -dx
                C2 = (B[0]+px2, B[1]+py2)
                D2 = (A[0]+px2, A[1]+py2)
                if C2 in point_set and D2 in point_set:
                    area = dx*dx + dy*dy
                    if area > max_area:
                        max_area = area

        print(max_area)

if __name__ == "__main__":
    main()