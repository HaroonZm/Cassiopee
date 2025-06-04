def read_first_line():
    return map(int, input().split())

def read_input_rectangle():
    return tuple(map(int, input().split()))

def append_rectangle_data(plst, xlst, ylst, dlst):
    x1, y1, d1, x2, y2, d2 = read_input_rectangle()
    plst.append((x1, y1, d1, x2, y2, d2))
    xlst.append(x1)
    xlst.append(x2)
    ylst.append(y1)
    ylst.append(y2)
    dlst.append(d1)
    dlst.append(d2)

def get_unique_sorted(lst):
    return sorted(list(set(lst)))

def build_value_to_index_dict(lst):
    dic = {}
    for i, v in enumerate(lst):
        dic[v] = i
    return dic

def initialize_map_with_zeros(xlen, ylen, dlen):
    return [[[0] * dlen for _ in range(ylen)] for _ in range(xlen)]

def coordinate_compress_all(xlst, ylst, dlst):
    cx = get_unique_sorted(xlst)
    cy = get_unique_sorted(ylst)
    cd = get_unique_sorted(dlst)
    return cx, cy, cd

def build_all_value_to_index(cx, cy, cd):
    xdic = build_value_to_index_dict(cx)
    ydic = build_value_to_index_dict(cy)
    ddic = build_value_to_index_dict(cd)
    return xdic, ydic, ddic

def update_map_with_plst(plst, xdic, ydic, ddic, new_map):
    for p in plst:
        x1, y1, d1, x2, y2, d2 = p
        x1, y1, d1, x2, y2, d2 = xdic[x1], ydic[y1], ddic[d1], xdic[x2], ydic[y2], ddic[d2]
        for x in range(x1, x2):
            for y in range(y1, y2):
                for d in range(d1, d2):
                    new_map[x][y][d] += 1

def count_volume_at_least_k(new_map, xlst, ylst, dlst, xdic, ydic, ddic, k):
    ans = 0
    for i in range(len(xlst) - 1):
        for j in range(len(ylst) - 1):
            for z in range(len(dlst) - 1):
                x, y, d = xdic[xlst[i]], ydic[ylst[j]], ddic[dlst[z]]
                if new_map[x][y][d] >= k:
                    dx = xlst[i + 1] - xlst[i]
                    dy = ylst[j + 1] - ylst[j]
                    dd = dlst[z + 1] - dlst[z]
                    ans += dx * dy * dd
    return ans

def main():
    n, k = read_first_line()
    plst = []
    xlst = []
    ylst = []
    dlst = []
    for _ in range(n):
        append_rectangle_data(plst, xlst, ylst, dlst)
    cx, cy, cd = coordinate_compress_all(xlst, ylst, dlst)
    xdic, ydic, ddic = build_all_value_to_index(cx, cy, cd)
    new_map = initialize_map_with_zeros(len(cx), len(cy), len(cd))
    update_map_with_plst(plst, xdic, ydic, ddic, new_map)
    ans = count_volume_at_least_k(new_map, cx, cy, cd, xdic, ydic, ddic, k)
    print(ans)

main()