def parse_first_line():
    n, k = map(int, input().split())
    return n, k

def init_lists():
    return [], [], [], []

def read_data(n, plst, xlst, ylst, dlst):
    for _ in range(n):
        x1, y1, d1, x2, y2, d2 = map(int, input().split())
        add_rectangle(plst, x1, y1, d1, x2, y2, d2)
        add_to_list(xlst, x1, x2)
        add_to_list(ylst, y1, y2)
        add_to_list(dlst, d1, d2)

def add_rectangle(plst, x1, y1, d1, x2, y2, d2):
    plst.append((x1, y1, d1, x2, y2, d2))

def add_to_list(lst, v1, v2):
    lst.append(v1)
    lst.append(v2)

def process_list(lst):
    return sorted(set(lst))

def build_index_dict(lst):
    d = dict()
    for i, v in enumerate(lst):
        d[v] = i
    return d

def build_3d_map(xlst, ylst, dlst):
    return [[[0] * len(dlst) for _ in ylst] for _ in xlst]

def compress_and_update_map(plst, new_map, xdic, ydic, ddic):
    for p in plst:
        x1, y1, d1, x2, y2, d2 = p
        ix1 = xdic[x1]
        iy1 = ydic[y1]
        id1 = ddic[d1]
        ix2 = xdic[x2]
        iy2 = ydic[y2]
        id2 = ddic[d2]
        fill_map(new_map, ix1, ix2, iy1, iy2, id1, id2)

def fill_map(new_map, x1, x2, y1, y2, d1, d2):
    for x in range(x1, x2):
        for y in range(y1, y2):
            for d in range(d1, d2):
                new_map[x][y][d] += 1

def calculate_volume(xlst, ylst, dlst, xdic, ydic, ddic, new_map, k):
    ans = 0
    for i in range(len(xlst) - 1):
        for j in range(len(ylst) - 1):
            for z in range(len(dlst) - 1):
                if cell_has_enough_cover(new_map, xdic, ydic, ddic, xlst, ylst, dlst, i, j, z, k):
                    ans += volume_cell(xlst, ylst, dlst, i, j, z)
    return ans

def cell_has_enough_cover(new_map, xdic, ydic, ddic, xlst, ylst, dlst, i, j, z, k):
    x = xdic[xlst[i]]
    y = ydic[ylst[j]]
    d = ddic[dlst[z]]
    return new_map[x][y][d] >= k

def volume_cell(xlst, ylst, dlst, i, j, z):
    return (xlst[i + 1] - xlst[i]) * (ylst[j + 1] - ylst[j]) * (dlst[z + 1] - dlst[z])

def output_result(ans):
    print(ans)

def main():
    n, k = parse_first_line()
    plst, xlst, ylst, dlst = init_lists()
    read_data(n, plst, xlst, ylst, dlst)
    xlst = process_list(xlst)
    ylst = process_list(ylst)
    dlst = process_list(dlst)
    xdic = build_index_dict(xlst)
    ydic = build_index_dict(ylst)
    ddic = build_index_dict(dlst)
    new_map = build_3d_map(xlst, ylst, dlst)
    compress_and_update_map(plst, new_map, xdic, ydic, ddic)
    ans = calculate_volume(xlst, ylst, dlst, xdic, ydic, ddic, new_map, k)
    output_result(ans)

main()