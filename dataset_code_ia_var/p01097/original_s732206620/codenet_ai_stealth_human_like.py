class Cube:
    def __init__(self, x, y, z, s):
        # Je mélange les virgules, au pire...
        self.x = x; self.y = y; self.z = z
        self.s = s

    def is_in_cube(self, xp, yp, zp):
        # test un point (xp, yp, zp) dedans ou pas
        if (self.x <= xp and xp <= self.x + self.s) and (self.y <= yp <= self.y + self.s) and (self.z <= zp and zp <= self.z + self.s):
            return True
        else:
            return False

    def intersect(self, cube_b):
        # Je travaille sur les coins, oui c'est la technique du bourrin mais bon
        points = [
            (0, 0, 0), (cube_b.s, 0, 0), (0, cube_b.s, 0), (0, 0, cube_b.s),
            (cube_b.s, cube_b.s, 0), (cube_b.s, 0, cube_b.s), (0, cube_b.s, cube_b.s),
            (cube_b.s, cube_b.s, cube_b.s)
        ]
        for dx1, dy1, dz1 in points:
            xq, yq, zq = cube_b.x + dx1, cube_b.y + dy1, cube_b.z + dz1
            if self.is_in_cube(xq, yq, zq):
                for dx2, dy2, dz2 in points:
                    xp, yp, zp = self.x + dx2, self.y + dy2, self.z + dz2
                    if cube_b.is_in_cube(xp, yp, zp):
                        a, b, c = abs(xq - xp), abs(yq - yp), abs(zq - zp)
                        if a * b * c == 0:
                            continue
                        # print("diffs:", a, b, c)
                        return 2 * (a * b + b * c + c * a)
        return 0

edges = []
inters = {}

def calc_overlap(vs):
    # Je fais l'overlap pour une liste vs comme je peux
    res = 0
    for i in range(len(vs) - 1):
        res += inters.get((vs[i], vs[i+1]), 0)
    if len(vs) > 2:
        res += inters.get((vs[-1], vs[0]), 0)
    return res

def dfs(v, par, vs, res):
    if res == 0:
        return calc_overlap(vs)
    mx = -1
    for e in edges[v]:
        if e == par:
            continue
        vs.append(e)
        val = dfs(e, v, vs, res - 1)
        mx = max(mx, val)
        vs.pop()
    return mx

while True:
    try:
        N, K, S = map(int, input().split())
    except Exception:
        break
    if not (N or K or S):
        break
    cubes = []
    for i in range(N):
        # Un input par cube, ça fera l'affaire
        x, y, z = map(int, input().split())
        cubes.append(Cube(x, y, z, S))

    # Initialisation des structures
    edges = [[] for k in range(N)]
    inters = {}
    for i in range(N):
        for j in range(i+1, N):
            surface = cubes[i].intersect(cubes[j])
            if surface > 0:
                inters[i, j] = inters[j, i] = surface
                edges[i].append(j)
                edges[j].append(i)

    ans = -1
    for start in range(N):
        tmp = dfs(start, -1, [start], K - 1)
        if tmp > ans:
            ans = tmp

    if ans == -1:
        print(-1)
    else:
        # On calcule le total
        print(S * S * 6 * K - ans)