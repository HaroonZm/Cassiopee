def parse_input_line():
    return [int(x) for x in input().split()]

def initialize_wifi_map(length):
    return [0] * length

def get_wifi_input():
    return [int(x) for x in input().split()]

def bound_index(val):
    return max(0, val)

def update_map_value(map_wifi, index, reach):
    map_wifi[index] = max(map_wifi[index], reach)

def compute_reach(x, w, min_index):
    return x + w - min_index

def process_wifi_infos(N, map_x, map_y):
    for _ in range(N):
        x, y, w = get_wifi_input()
        update_wifi_x(map_x, x, w)
        update_wifi_y(map_y, y, w)

def update_wifi_x(map_x, x, w):
    idx = bound_index(x - w)
    reach = compute_reach(x, w, idx)
    update_map_value(map_x, idx, reach)

def update_wifi_y(map_y, y, w):
    idx = bound_index(y - w)
    reach = compute_reach(y, w, idx)
    update_map_value(map_y, idx, reach)

def check_wifi(wifi):
    return check_wifi_internal(wifi)

def check_wifi_internal(wifi):
    m = 0
    end = get_wifi_length(wifi)

    for i, x in enumerate(wifi):
        m = update_covered_max(m, i, x)
        if is_end_covered(m, end):
            return True
        if not is_index_covered(i, m):
            return False
    return False

def get_wifi_length(wifi):
    return len(wifi)

def update_covered_max(current_max, index, value):
    if value and index + value > current_max:
        return index + value
    return current_max

def is_end_covered(covered, end):
    return covered >= end

def is_index_covered(index, covered):
    return index < covered

def main():
    N, W, H = parse_input_line()
    map_x = initialize_wifi_map(W)
    map_y = initialize_wifi_map(H)
    process_wifi_infos(N, map_x, map_y)
    if output_wifi_result(map_x, map_y):
        print('Yes')
    else:
        print('No')

def output_wifi_result(map_x, map_y):
    return check_wifi(map_x) or check_wifi(map_y)

main()