def read_two_ints():
    return map(int, input().split())

def read_multiple_coords(num):
    return [read_coord() for _ in range(num)]

def read_coord():
    return [int(x) for x in input().split()]

def init_count_list(size):
    return [0] * size

def init_distance_matrix(rows, cols):
    return [[] for _ in range(rows)]

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def compute_distances_matrix(ab, cd, n, m):
    result = []
    for i in range(n):
        current_row = compute_distances_for_one(ab[i], cd, m)
        result.append(current_row)
    return result

def compute_distances_for_one(a, cd, m):
    distances = []
    for l in range(m):
        d = manhattan_distance(a[0], a[1], cd[l][0], cd[l][1])
        distances.append(d)
    return distances

def find_and_print_min_indices(distance, n):
    for i in range(n):
        print(find_min_index(distance[i]) + 1)

def find_min_index(row):
    return row.index(min(row))

def main():
    n, m = read_two_ints()
    ab = read_multiple_coords(n)
    cd = read_multiple_coords(m)
    count = init_count_list(n)
    distance = init_distance_matrix(n, m)
    distance = compute_distances_matrix(ab, cd, n, m)
    find_and_print_min_indices(distance, n)

main()