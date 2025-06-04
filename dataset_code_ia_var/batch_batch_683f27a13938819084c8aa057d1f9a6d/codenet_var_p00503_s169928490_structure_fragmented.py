def read_input():
    n, k = map(int, input().split())
    return n, k

def init_lists():
    return [], [], [], []

def read_and_store_plst(n, plst, xlst, ylst, dlst):
    for _ in range(n):
        add_point_to_lists(plst, xlst, ylst, dlst)
    return

def add_point_to_lists(plst, xlst, ylst, dlst):
    x1, y1, d1, x2, y2, d2 = map(int, input().split())
    append_point(plst, x1, y1, d1, x2, y2, d2)
    append_to_lists(xlst, x1, x2)
    append_to_lists(ylst, y1, y2)
    append_to_lists(dlst, d1, d2)

def append_point(plst, x1, y1, d1, x2, y2, d2):
    plst.append((x1, y1, d1, x2, y2, d2))

def append_to_lists(lst, a, b):
    lst.append(a)
    lst.append(b)

def unique_sort(lst):
    return sorted(set(lst))

def get_lengths(xlst, ylst, dlst):
    return len(xlst), len(ylst), len(dlst)

def make_dic(lst):
    return dict((v, i) for i, v in enumerate(lst))

def build_new_map(lx, ly, ld):
    return [[[0] * ld for _ in range(ly)] for _ in range(lx)]

def fill_new_map(plst, xdic, ydic, ddic, new_map):
    for p in plst:
        x1, y1, d1, x2, y2, d2 = p
        xi1, yi1, di1, xi2, yi2, di2 = xdic[x1], ydic[y1], ddic[d1], xdic[x2], ydic[y2], ddic[d2]
        update_new_map(new_map, xi1, yi1, di1, xi2, yi2, di2)
    return

def update_new_map(new_map, xi1, yi1, di1, xi2, yi2, di2):
    for x in range(xi1, xi2):
        for y in range(yi1, yi2):
            for d in range(di1, di2):
                new_map[x][y][d] += 1

def compute_ans(lx, ly, ld, xlst, ylst, dlst, xdic, ydic, ddic, new_map, k):
    ans = 0
    for i in range(lx - 1):
        xlsti, xlsti1 = xlst[i], xlst[i + 1]
        xi = xdic[xlsti]
        for j in range(ly - 1):
            ylstj, ylstj1 = ylst[j], ylst[j + 1]
            yj = ydic[ylstj]
            for z in range(ld - 1):
                dlstz, dlstz1 = dlst[z], dlst[z + 1]
                dz = ddic[dlstz]
                if cover_condition(new_map, xi, yj, dz, k):
                    ans += cell_volume(xlsti, xlsti1, ylstj, ylstj1, dlstz, dlstz1)
    return ans

def cover_condition(new_map, xi, yj, dz, k):
    return new_map[xi][yj][dz] >= k

def cell_volume(xlsti, xlsti1, ylstj, ylstj1, dlstz, dlstz1):
    return (xlsti1 - xlsti) * (ylstj1 - ylstj) * (dlstz1 - dlstz)

def main():
    n, k = read_input()
    plst, xlst, ylst, dlst = init_lists()
    read_and_store_plst(n, plst, xlst, ylst, dlst)
    xlst = unique_sort(xlst)
    ylst = unique_sort(ylst)
    dlst = unique_sort(dlst)
    lx, ly, ld = get_lengths(xlst, ylst, dlst)
    xdic = make_dic(xlst)
    ydic = make_dic(ylst)
    ddic = make_dic(dlst)
    new_map = build_new_map(lx, ly, ld)
    fill_new_map(plst, xdic, ydic, ddic, new_map)
    ans = compute_ans(lx, ly, ld, xlst, ylst, dlst, xdic, ydic, ddic, new_map, k)
    print(ans)

main()