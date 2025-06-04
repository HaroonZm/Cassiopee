import sys

def read_number():
    return int(input())

def read_edge_row():
    return list(map(int, sys.stdin.readline().split()))

def read_all_edges(n):
    edges = []
    for i in range(n):
        row = read_edge_row()
        edges.append(row)
    return edges

def min_edge_value(a, b):
    return min(a, b)

def compute_pair_min(edges, i, j):
    return min_edge_value(edges[i][j], edges[j][i])

def sum_all_pairs(edges, n):
    total = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            value = compute_pair_min(edges, i, j)
            total += value
    return total

def print_result(ans):
    print(ans)

def main():
    n = read_number()
    edges = read_all_edges(n)
    ans = sum_all_pairs(edges, n)
    print_result(ans)

if __name__ == '__main__':
    main()