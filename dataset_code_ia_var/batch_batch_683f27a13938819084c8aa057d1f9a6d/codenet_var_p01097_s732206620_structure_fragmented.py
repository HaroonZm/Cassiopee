class Cube:
    def __init__(self, x, y, z, s):
        self.x, self.y, self.z = x, y, z
        self.s = s

def create_cube(x, y, z, s):
    return Cube(x, y, z, s)

def point_within_cube(cube, x, y, z):
    return (cube.x <= x <= cube.x + cube.s and
            cube.y <= y <= cube.y + cube.s and
            cube.z <= z <= cube.z + cube.s)

def get_dxyz():
    return [(0, 0, 0),
            (1, 0, 0), (0, 1, 0), (0, 0, 1),
            (1, 1, 0), (1, 0, 1), (0, 1, 1),
            (1, 1, 1)]

def scale_dxyz(dxyz, s):
    return [(dx * s, dy * s, dz * s) for dx, dy, dz in dxyz]

def iter_cube_vertices(cube):
    dxyz = scale_dxyz(get_dxyz(), cube.s)
    vertices = []
    for dx, dy, dz in dxyz:
        nx, ny, nz = cube.x + dx, cube.y + dy, cube.z + dz
        vertices.append((nx, ny, nz))
    return vertices

def check_points_in_other_cube(points, other_cube):
    result = []
    for x, y, z in points:
        if point_within_cube(other_cube, x, y, z):
            result.append((x, y, z))
    return result

def vertex_pairs(vertices1, vertices2):
    for v1 in vertices1:
        for v2 in vertices2:
            yield v1, v2

def overlap_measure(v1, v2):
    a = abs(v1[0] - v2[0])
    b = abs(v1[1] - v2[1])
    c = abs(v1[2] - v2[2])
    return a, b, c

def surface_formula(a, b, c):
    return 2 * (a * b + b * c + c * a)

def should_continue(a, b, c):
    return a * b * c == 0

def cube_intersection_surface(cube1, cube2):
    vertices1 = iter_cube_vertices(cube2)
    vertices2 = iter_cube_vertices(cube1)
    valid_v1 = check_points_in_other_cube(vertices1, cube1)
    for nx1, ny1, nz1 in valid_v1:
        for nx2, ny2, nz2 in check_points_in_other_cube(vertices2, cube2):
            a, b, c = overlap_measure((nx1, ny1, nz1), (nx2, ny2, nz2))
            if should_continue(a, b, c):
                continue
            return surface_formula(a, b, c)
    return 0

def build_cubes(N, S):
    cubes = []
    for _ in range(N):
        x, y, z = map(int, input().split())
        cubes.append(create_cube(x, y, z, S))
    return cubes

def build_edges_inters(cubes):
    N = len(cubes)
    edges = [[] for _ in range(N)]
    inters = dict()
    for i in range(N):
        for j in range(i + 1, N):
            sur = cube_intersection_surface(cubes[i], cubes[j])
            if sur > 0:
                inters[(i, j)] = sur
                inters[(j, i)] = sur
                edges[i].append(j)
                edges[j].append(i)
    return edges, inters

def overlap_between_pair(a, b, inters):
    return inters.get((a, b), 0)

def calc_overlap_path(vs, inters):
    path_length = len(vs)
    ret = 0
    for i in range(path_length - 1):
        ret += overlap_between_pair(vs[i], vs[i+1], inters)
    if path_length > 2:
        ret += overlap_between_pair(vs[-1], vs[0], inters)
    return ret

def dfs_search(v, par, vs, res, edges, inters):
    if res == 0:
        return calc_overlap_path(vs, inters)
    ret = -1
    for e in edges[v]:
        if e != par:
            vs.append(e)
            new_ret = dfs_search(e, v, vs, res - 1, edges, inters)
            ret = max(ret, new_ret)
            vs.pop()
    return ret

def process_single_case(N, K, S):
    cubes = build_cubes(N, S)
    edges, inters = build_edges_inters(cubes)
    ans = -1
    for i in range(N):
        r = dfs_search(i, -1, [i], K - 1, edges, inters)
        ans = max(ans, r)
    return -1 if ans == -1 else S * S * 6 * K - ans

def parse_input():
    try:
        while True:
            vals = input().split()
            if not vals:
                continue
            N, K, S = map(int, vals)
            if not (N or K or S):
                break
            yield N, K, S
    except EOFError:
        return

def main():
    for N, K, S in parse_input():
        result = process_single_case(N, K, S)
        print(result)

main()