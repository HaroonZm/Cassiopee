import sys
import math

def closest_pair(points):
    def dist(p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    def closest_pair_rec(pts_sorted_x, pts_sorted_y):
        n = len(pts_sorted_x)
        if n <= 3:
            min_d = float('inf')
            for i in range(n):
                for j in range(i+1, n):
                    d = dist(pts_sorted_x[i], pts_sorted_x[j])
                    if d < min_d:
                        min_d = d
            return min_d
        mid = n // 2
        mid_x = pts_sorted_x[mid][0]

        left_x = pts_sorted_x[:mid]
        right_x = pts_sorted_x[mid:]
        left_y = []
        right_y = []
        for p in pts_sorted_y:
            if p[0] <= mid_x:
                left_y.append(p)
            else:
                right_y.append(p)

        d_left = closest_pair_rec(left_x, left_y)
        d_right = closest_pair_rec(right_x, right_y)
        d = min(d_left, d_right)

        strip = [p for p in pts_sorted_y if abs(p[0] - mid_x) < d]

        strip_len = len(strip)
        for i in range(strip_len):
            j = i + 1
            while j < strip_len and (strip[j][1] - strip[i][1]) < d:
                dist_ij = dist(strip[i], strip[j])
                if dist_ij < d:
                    d = dist_ij
                j += 1
        return d

    points_sorted_x = sorted(points, key=lambda p: p[0])
    points_sorted_y = sorted(points, key=lambda p: p[1])
    return closest_pair_rec(points_sorted_x, points_sorted_y)

input = sys.stdin.readline
n = int(input())
points = [tuple(map(float, input().split())) for _ in range(n)]

result = closest_pair(points)
print(f"{result:.9f}")