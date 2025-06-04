from heapq import heappush as hpq_push, heappop as hpq_pop

def run_main():
    CONST_INF = 10 ** 20
    DIRS = ((0, 1), (0, -1), (-1, 0), (1, 0))

    grid_height, grid_width = map(int, input().split())
    grid_matrix = [[-1] + list(map(int, input().split())) + [-1] for _ in range(grid_height)]
    grid_matrix.insert(0, [-1] * (grid_width + 2))
    grid_matrix.append([-1] * (grid_width + 2))

    goal_flags = [[False] * (grid_width + 2) for _ in range(grid_height + 2)]
    bfs_queue = []
    hpq_push(bfs_queue, (grid_width, grid_height))
    while bfs_queue:
        cur_x, cur_y = hpq_pop(bfs_queue)
        goal_flags[cur_y][cur_x] = True
        if grid_matrix[cur_y][cur_x] != 0:
            continue

        for dir_dx, dir_dy in DIRS:
            next_x, next_y = cur_x + dir_dx, cur_y + dir_dy
            if grid_matrix[next_y][next_x] == -1 or goal_flags[next_y][next_x]:
                continue
            hpq_push(bfs_queue, (next_x, next_y))

    cost_table = [[[CONST_INF] * (grid_width + 2) for _ in range(grid_height + 2)] for _ in range(grid_width * grid_height)]
    dijkstra_queue = []
    hpq_push(dijkstra_queue, (0, 0, 1, 1)) # (total_cost, moves_count, pos_x, pos_y)
    cost_table[0][1][1] = 0

    while dijkstra_queue:
        cur_cost, cur_dist, cur_x, cur_y = hpq_pop(dijkstra_queue)
        for dir_dx, dir_dy in DIRS:
            adj_x, adj_y = cur_x + dir_dx, cur_y + dir_dy
            cell_val = grid_matrix[adj_y][adj_x]
            if cell_val == -1:
                continue
            if cur_dist >= grid_width * grid_height - 1:
                continue
            calc_cost = cur_cost + (cur_dist * cell_val * 2) + cell_val
            if cost_table[cur_dist + 1][adj_y][adj_x] > calc_cost:
                cost_table[cur_dist + 1][adj_y][adj_x] = calc_cost
                hpq_push(dijkstra_queue, (calc_cost, cur_dist + 1, adj_x, adj_y))

    min_ans = min(
        cost_table[d][y][x]
        for y in range(1, grid_height + 1)
        for x in range(1, grid_width + 1)
        for d in range(grid_width * grid_height)
        if goal_flags[y][x]
    )
    print(min_ans)

run_main()