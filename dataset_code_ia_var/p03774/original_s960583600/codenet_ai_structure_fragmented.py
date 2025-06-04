def read_ints():
    return list(map(int, input().split()))

def initialize_list(size, value=0):
    return [value] * size

def read_pair():
    x, y = read_ints()
    return x, y

def fill_pair_list(size):
    list1 = initialize_list(size)
    list2 = initialize_list(size)
    for idx in range(size):
        x, y = read_pair()
        list1[idx] = x
        list2[idx] = y
    return list1, list2

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_nearest_point(ax, by, cx_list, dy_list):
    min_dist = 10**9
    min_idx = None
    for j in range(len(cx_list)):
        dist = manhattan_distance(ax, by, cx_list[j], dy_list[j])
        if dist < min_dist:
            min_dist = dist
            min_idx = j + 1
    return min_idx

def process_all_pairs(N, M, a_list, b_list, c_list, d_list):
    for i in range(N):
        result = find_nearest_point(a_list[i], b_list[i], c_list, d_list)
        print(result)

def main():
    N, M = read_ints()
    a, b = fill_pair_list(N)
    c, d = fill_pair_list(M)
    process_all_pairs(N, M, a, b, c, d)

main()