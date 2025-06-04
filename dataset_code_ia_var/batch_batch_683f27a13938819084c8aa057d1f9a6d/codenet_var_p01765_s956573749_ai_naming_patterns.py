import sys

def read_input_line(): return sys.stdin.readline().strip()
def create_2d_list(rows, cols, value): return [[value] * cols for _ in range(rows)]
def create_3d_list(l1, l2, l3, value): return [[[value] * l3 for _ in range(l2)] for _ in range(l1)]
def create_4d_list(l1, l2, l3, l4, value): return [[[[value] * l4 for _ in range(l3)] for _ in range(l2)] for _ in range(l1)]
def ceil_div(x, y=1): return int(-(-x // y))
def read_int(): return int(read_input_line())
def read_ints(): return map(int, read_input_line().split())
def read_int_list(size=None): return list(read_ints()) if size is None else [read_int() for _ in range(size)]
def print_yes(): print('Yes')
def print_no(): print('No')
def print_yes_upper(): print('YES')
def print_no_upper(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF_CONST = 10 ** 18
MOD_CONST = 10 ** 9 + 7

class GeometryUtil:
    """ Class for geometric computation """

    EPSILON = 1e-9

    def point_add(self, pt1, pt2):
        x1, y1 = pt1
        x2, y2 = pt2
        return (x1 + x2, y1 + y2)

    def point_sub(self, pt1, pt2):
        x1, y1 = pt1
        x2, y2 = pt2
        return (x1 - x2, y1 - y2)

    def point_mul(self, pt, factor):
        x1, y1 = pt
        if not isinstance(factor, tuple):
            return (x1 * factor, y1 * factor)
        x2, y2 = factor
        return (x1 * x2, y1 * y2)

    def point_div(self, pt, divisor):
        x1, y1 = pt
        if not isinstance(divisor, tuple):
            return (x1 / divisor, y1 / divisor)
        x2, y2 = divisor
        return (x1 / x2, y1 / y2)

    def point_abs(self, pt):
        from math import hypot
        x1, y1 = pt
        return hypot(x1, y1)

    def point_norm(self, pt):
        x, y = pt
        return x ** 2 + y ** 2

    def point_dot(self, pt1, pt2):
        x1, y1 = pt1
        x2, y2 = pt2
        return x1 * x2 + y1 * y2

    def point_cross(self, pt1, pt2):
        x1, y1 = pt1
        x2, y2 = pt2
        return x1 * y2 - y1 * x2

    def project_point_onto_segment(self, segment, pt):
        pt1, pt2 = segment
        base_vec = self.point_sub(pt2, pt1)
        ratio = self.point_dot(self.point_sub(pt, pt1), base_vec) / self.point_norm(base_vec)
        return self.point_add(pt1, self.point_mul(base_vec, ratio))

    def reflect_point_over_segment(self, segment, pt):
        return self.point_add(pt, self.point_mul(self.point_sub(self.project_point_onto_segment(segment, pt), pt), 2))

    def ccw_type(self, pivot, pt1, pt2):
        a = self.point_sub(pt1, pivot)
        b = self.point_sub(pt2, pivot)
        cross_ab = self.point_cross(a, b)
        if cross_ab > self.EPSILON: return 1
        if cross_ab < -self.EPSILON: return -1
        if self.point_dot(a, b) < -self.EPSILON: return 2
        if self.point_norm(a) < self.point_norm(b): return -2
        return 0

    def is_segments_intersect(self, seg1, seg2):
        p1, p2 = seg1
        p3, p4 = seg2
        return (
            self.ccw_type(p1, p2, p3) * self.ccw_type(p1, p2, p4) <= 0
            and self.ccw_type(p3, p4, p1) * self.ccw_type(p3, p4, p2) <= 0
        )

    def distance_line_point(self, line, pt):
        pt1, pt2 = line
        return abs(self.point_cross(self.point_sub(pt2, pt1), self.point_sub(pt, pt1)) / self.point_abs(self.point_sub(pt2, pt1)))

    def distance_segment_point(self, segment, pt):
        pt1, pt2 = segment
        if self.point_dot(self.point_sub(pt2, pt1), self.point_sub(pt, pt1)) < 0:
            return self.point_abs(self.point_sub(pt, pt1))
        if self.point_dot(self.point_sub(pt1, pt2), self.point_sub(pt, pt2)) < 0:
            return self.point_abs(self.point_sub(pt, pt2))
        return self.distance_line_point(segment, pt)

    def distance_segment_segment(self, seg1, seg2):
        pt1, pt2 = seg1
        pt3, pt4 = seg2
        if self.is_segments_intersect(seg1, seg2):
            return 0
        return min(
            self.distance_segment_point(seg1, pt3), self.distance_segment_point(seg1, pt4),
            self.distance_segment_point(seg2, pt1), self.distance_segment_point(seg2, pt2)
        )

    def segment_segment_cross_point(self, seg1, seg2):
        pt1, pt2 = seg1
        pt3, pt4 = seg2
        base_vec = self.point_sub(pt4, pt3)
        dist1 = abs(self.point_cross(base_vec, self.point_sub(pt1, pt3)))
        dist2 = abs(self.point_cross(base_vec, self.point_sub(pt2, pt3)))
        t = dist1 / (dist1 + dist2)
        return self.point_add(pt1, self.point_mul(self.point_sub(pt2, pt1), t))

    def circle_line_cross_points(self, circle, line):
        from math import sqrt
        x, y, r = circle
        pt1, pt2 = line
        proj_pt = self.project_point_onto_segment(line, (x, y))
        e_vec = self.point_div(self.point_sub(pt2, pt1), self.point_abs(self.point_sub(pt2, pt1)))
        base_len = sqrt(r * r - self.point_norm(self.point_sub(proj_pt, (x, y))))
        return [self.point_add(proj_pt, self.point_mul(e_vec, base_len)), self.point_sub(proj_pt, self.point_mul(e_vec, base_len))]

    def point_arg(self, pt):
        from math import atan2
        x, y = pt
        return atan2(y, x)

    def point_polar(self, r, theta):
        from math import sin, cos
        return (cos(theta) * r, sin(theta) * r)

    def circle_circle_cross_points(self, circle1, circle2):
        from math import acos
        x1, y1, r1 = circle1
        x2, y2, r2 = circle2
        d = self.point_abs(self.point_sub((x1, y1), (x2, y2)))
        a = acos((r1 * r1 + d * d - r2 * r2) / (2 * r1 * d))
        t = self.point_arg(self.point_sub((x2, y2), (x1, y1)))
        return [
            self.point_add((x1, y1), self.point_polar(r1, t + a)),
            self.point_add((x1, y1), self.point_polar(r1, t - a))
        ]

geometry_util = GeometryUtil()

polygon1_vertex_count = read_int()
polygon1_points = [(0, 0)]
for _ in range(polygon1_vertex_count):
    px, py = read_ints()
    polygon1_points.append((px, py))
polygon1_points.append((1000, 0))

polygon2_vertex_count = read_int()
polygon2_points = [(0, 1000)]
for _ in range(polygon2_vertex_count):
    px, py = read_ints()
    polygon2_points.append((px, py))
polygon2_points.append((1000, 1000))

polygon1_segments = []
for i in range(polygon1_vertex_count + 1):
    x1, y1 = polygon1_points[i]
    x2, y2 = polygon1_points[i + 1]
    polygon1_segments.append(((x1, y1), (x2, y2)))
polygon2_segments = []
for i in range(polygon2_vertex_count + 1):
    x1, y1 = polygon2_points[i]
    x2, y2 = polygon2_points[i + 1]
    polygon2_segments.append(((x1, y1), (x2, y2)))

min_distance = INF_CONST
for idx1 in range(polygon1_vertex_count + 1):
    for idx2 in range(polygon2_vertex_count + 1):
        min_distance = min(min_distance, geometry_util.distance_segment_segment(polygon1_segments[idx1], polygon2_segments[idx2]))
print(min_distance)