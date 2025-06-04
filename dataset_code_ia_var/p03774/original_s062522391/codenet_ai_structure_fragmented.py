import sys

def get_input_reader():
    return sys.stdin.readline

def read_ints(reader):
    return list(map(int, reader().split()))

def read_points(count, reader):
    return [read_ints(reader) for _ in range(count)]

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def find_nearest_point(a, b, CD):
    min_distance = 10**10
    nearest_index = 0
    for idx, (c, d) in enumerate(CD):
        distance = manhattan_distance((a, b), (c, d))
        if distance < min_distance:
            min_distance = distance
            nearest_index = idx
    return nearest_index

def compute_all_nearest(AB, CD):
    result = []
    for a, b in AB:
        idx = find_nearest_point(a, b, CD)
        result.append(idx + 1)
    return result

def print_results(results):
    for res in results:
        print(res)

def main():
    reader = get_input_reader()
    N_and_M = read_ints(reader)
    N = N_and_M[0]
    M = N_and_M[1]
    AB = read_points(N, reader)
    CD = read_points(M, reader)
    Ans = compute_all_nearest(AB, CD)
    print_results(Ans)

main()