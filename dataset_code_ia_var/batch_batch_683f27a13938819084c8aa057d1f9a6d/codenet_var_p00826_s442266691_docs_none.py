def string_to_complex(s):
    a, b, c, d = map(int, s.split())
    return (a + b * 1j, c + d * 1j)

def dot(c1, c2):
    return c1.real * c2.real + c1.imag * c2.imag

def cross(c1, c2):
    return c1.real * c2.imag - c1.imag * c2.real

def cross_point(p1, p2, p3, p4):
    crs1 = cross(p2 - p1, p3 - p1)
    crs2 = cross(p2 - p1, p4 - p1)
    if crs1 == 0 and crs2 == 0:
        if p1 == p3 or p1 == p4:
            return p1
        elif p2 == p3 or p2 == p4:
            return p2
        else:
            return None
    crs3 = cross(p4 - p3, p1 - p3)
    crs4 = cross(p4 - p3, p2 - p3)
    if crs1 * crs2 <= 0 and crs3 * crs4 <= 0:
        base = p4 - p3
        hypo1 = p1 - p3
        hypo2 = p2 - p3
        d1 = abs(cross(base, hypo1)) / abs(base)
        d2 = abs(cross(base, hypo2)) / abs(base)
        return p1 + d1 / (d1 + d2) * (p2 - p1)
    else:
        return None

def contain(polygon):
    flag = False
    for a, b in zip(polygon[0:], polygon[1:] + [polygon[0]]):
        if a.imag > b.imag:
            a, b = b, a
        if a.imag <= 0 and b.imag > 0 and cross(a, b) > 0:
            flag = not flag
    return flag

from cmath import phase, pi

def complex_compare_key(c):
    return (c.real, c.imag)

def complex_compare_key2(c):
    return c.real

def pos_phase(base, c1, c2):
    p = phase((c2 - base) / (c1 - base))
    if p < 0:
        p += 2 * pi
    return p

def solve():
    from sys import stdin
    lines = stdin.readlines()
    from itertools import combinations
    while True:
        n = int(lines[0])
        if n == 0:
            break
        edges = enumerate(map(string_to_complex, lines[1:1+n]))
        adj_edge_cp = [[] for i in range(n)]
        adj_cross_point = {}
        for e1, e2 in combinations(edges, 2):
            n1, t1 = e1
            n2, t2 = e2
            cp = cross_point(*t1, *t2)
            if cp:
                adj_edge_cp[n1].append(cp)
                adj_edge_cp[n2].append(cp)
                adj_cross_point[cp] = (n1, n2)
        for cp_list in adj_edge_cp:
            cp_list.sort(key=complex_compare_key)
        for cp, t in adj_cross_point.items():
            e1, e2 = t
            e1_cp = adj_edge_cp[e1]
            e2_cp = adj_edge_cp[e2]
            cp_l = []
            if len(e1_cp) == 1:
                pass
            else:
                if cp == e1_cp[0]:
                    cp_l.append(e1_cp[1])
                elif cp == e1_cp[-1]:
                    cp_l.append(e1_cp[-2])
                else:
                    cp_idx = e1_cp.index(cp)
                    cp_l.append(e1_cp[cp_idx - 1])
                    cp_l.append(e1_cp[cp_idx + 1])
            if len(e2_cp) == 1:
                pass
            else:
                if cp == e2_cp[0]:
                    cp_l.append(e2_cp[1])
                elif cp == e2_cp[-1]:
                    cp_l.append(e2_cp[-2])
                else:
                    cp_idx = e2_cp.index(cp)
                    cp_l.append(e2_cp[cp_idx - 1])
                    cp_l.append(e2_cp[cp_idx + 1])
            adj_cross_point[cp] = cp_l
        flag = True
        while flag:
            for cp, cp_list in adj_cross_point.items():
                if len(cp_list) == 1:
                    next_cp = cp_list.pop()
                    adj_cross_point[next_cp].remove(cp)
                    break
            else:
                flag = False
        del_cp_list = []
        for cp, cp_list in adj_cross_point.items():
            if not cp_list:
                del_cp_list.append(cp)
        for cp in del_cp_list:
            del adj_cross_point[cp]
        cp_list = list(adj_cross_point)
        cp_list.sort(key=complex_compare_key2)
        visited = dict(zip(cp_list, [False] * len(cp_list)))
        for start in cp_list:
            if start.real >= 0:
                print("no")
                break
            if visited[start]:
                continue
            visited[start] = True
            path = [start - 1, start]
            flag = True
            while flag:
                pre_cp = path[-2]
                cp = path[-1]
                ang = 2 * pi
                for p in adj_cross_point[cp]:
                    if p == pre_cp:
                        continue
                    new_ang = pos_phase(cp, pre_cp, p)
                    if new_ang < ang:
                        next_cp = p
                        ang = new_ang
                visited[next_cp] = True
                if next_cp == start:
                    if contain(path[1:]):
                        print("yes")
                        flag = False
                    else:
                        break
                else:
                    path.append(next_cp)
            else:
                break
        else:
            print("no")
        del lines[:1+n]

solve()