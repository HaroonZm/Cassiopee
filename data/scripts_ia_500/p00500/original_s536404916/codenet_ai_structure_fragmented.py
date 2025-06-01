def read_input():
    N = int(input())
    all_game = [[int(j) for j in input().split()] for _ in range(N)]
    return N, all_game

def extract_column(all_game, index):
    return [row[index] for row in all_game]

def count_occurrences(lst):
    counts = {}
    for x in lst:
        if x not in counts:
            counts[x] = 1
        else:
            counts[x] += 1
    return counts

def update_points(points, values, counts):
    for i in range(len(values)):
        if counts[values[i]] == 1:
            points[i] += values[i]

def main():
    N, all_game = read_input()
    points = [0] * N
    for g_i in range(3):
        g = extract_column(all_game, g_i)
        counts = count_occurrences(g)
        update_points(points, g, counts)
    for p in points:
        print(p)

main()