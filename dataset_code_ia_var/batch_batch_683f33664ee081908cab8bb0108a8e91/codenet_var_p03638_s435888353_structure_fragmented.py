def read_HW():
    return map(int, input().split())

def read_N():
    return int(input())

def read_A(N):
    return list(map(int, input().split()))

def build_alist(a_list):
    return [[a, idx + 1] for idx, a in enumerate(a_list)]

def sort_alist(alist):
    return sorted(alist)

def expand_alist_entry(entry):
    color, value = entry
    return [value] * color

def build_draw_order(sorted_alist):
    draw_order = []
    for entry in sorted_alist:
        draw_order += expand_alist_entry(entry)
    return draw_order

def get_row(draw_order, row, W):
    start = row * W
    end = (row + 1) * W
    return draw_order[start:end]

def process_row(row_data, reverse):
    if reverse:
        row_data = reversed(row_data)
    return list(map(str, row_data))

def print_rows(H, W, draw_order):
    for row in range(H):
        reverse = (row % 2 == 1)
        row_data = get_row(draw_order, row, W)
        row_strs = process_row(row_data, reverse)
        out_line = ' '.join(row_strs)
        print(out_line)

def main():
    H, W = read_HW()
    N = read_N()
    a_list = read_A(N)
    alist = build_alist(a_list)
    sorted_alist = sort_alist(alist)
    draw_order = build_draw_order(sorted_alist)
    print_rows(H, W, draw_order)

main()