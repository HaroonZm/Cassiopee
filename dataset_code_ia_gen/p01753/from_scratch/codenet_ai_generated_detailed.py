import sys
import math

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def segment_sphere_intersection(sx, sy, sz, dx, dy, dz, cx, cy, cz, r):
    """
    判定線分(s->d)是否和半径为r，中心为(c)的球体相交。
    算法：
    - 设线段方向向量 v = d - s
    - 计算参数t，使点p = s + v*t是线与球面方程的交点
    - 解二次方程判断是否存在实根且根t在[0,1]范围内则相交（即线段穿过球）
    """
    vx = dx - sx
    vy = dy - sy
    vz = dz - sz

    # 向量 s->c
    sx_c = sx - cx
    sy_c = sy - cy
    sz_c = sz - cz

    # 二次方程参数
    a = vx*vx + vy*vy + vz*vz
    b = 2*(vx*sx_c + vy*sy_c + vz*sz_c)
    c = sx_c*sx_c + sy_c*sy_c + sz_c*sz_c - r*r

    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return False  # 无交点
    sqrt_discriminant = math.sqrt(discriminant)

    t1 = (-b - sqrt_discriminant)/(2*a)
    t2 = (-b + sqrt_discriminant)/(2*a)

    # 线段范围内有交点则相交
    if (0 <= t1 <= 1) or (0 <= t2 <= 1):
        return True
    return False

def main():
    # 读取数量N(障碍物), Q(询问数)
    N, Q = read_ints()

    obstacles = []
    for _ in range(N):
        x, y, z, r, l = read_ints()
        obstacles.append((x, y, z, r, l))

    queries = []
    for _ in range(Q):
        sx, sy, sz, dx, dy, dz = read_ints()
        queries.append((sx, sy, sz, dx, dy, dz))

    for (sx, sy, sz, dx, dy, dz) in queries:
        # 计算从红球->蓝球的路径上，射线经过哪些障碍物
        # 若障碍物被射线穿过，则消耗对应魔力
        cost = 0
        # 检查所有障碍物是否与线段(s->d)相交
        for (cx, cy, cz, r, l) in obstacles:
            if segment_sphere_intersection(sx, sy, sz, dx, dy, dz, cx, cy, cz, r):
                # 消耗该障碍物的魔力
                cost += l
        print(cost)

if __name__ == "__main__":
    main()