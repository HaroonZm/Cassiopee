nbr_of_cells = int(input())
nbr_of_queries = int(input())
for _ in range(nbr_of_queries):
    row_pos, col_pos = map(int, input().split())
    row_dist = min(row_pos - 1, nbr_of_cells - row_pos)
    col_dist = min(col_pos - 1, nbr_of_cells - col_pos)
    output_value = (min(row_dist, col_dist) % 3) + 1
    print(output_value)