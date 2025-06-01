def read_input():
    n, m, p = map(int, raw_input().split())
    return n, m, p

def read_distances(m):
    distances = []
    for _ in xrange(m):
        distances.append(int(raw_input()))
    return distances

def calculate_mod_distances(distances, p, n):
    mod_distances = []
    for dist in distances:
        mod_distances.append((dist - p + n) % n)
    return mod_distances

def sort_distances(distances):
    distances.sort()
    return distances

def initial_min_distance(d, n):
    return min(d[-1], n - d[0])

def min_distance_first_loop(d, n, m, current_min):
    for i in xrange(m - 1):
        val = d[i] + (d[i] + n - d[i + 1])
        current_min = min(current_min, val)
    return current_min

def min_distance_second_loop(d, n, m, current_min):
    for i in xrange(m - 1):
        val = (n - d[i + 1]) + (n - d[i + 1] + d[i])
        current_min = min(current_min, val)
    return current_min

def compute_answer(n, m, p, distances):
    mod_distances = calculate_mod_distances(distances, p, n)
    sorted_distances = sort_distances(mod_distances)
    ans = initial_min_distance(sorted_distances, n)
    ans = min_distance_first_loop(sorted_distances, n, m, ans)
    ans = min_distance_second_loop(sorted_distances, n, m, ans)
    return ans * 100

def main():
    n, m, p = read_input()
    distances = read_distances(m)
    answer = compute_answer(n, m, p, distances)
    print answer

main()