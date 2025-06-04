import heapq as pq

def search_bfs(start_x, start_y, max_steps, grid_map):
    node_queue = []
    pq.heappush(node_queue, (0, (start_x, start_y)))
    while node_queue:
        curr_steps, (curr_x, curr_y) = pq.heappop(node_queue)
        if curr_steps <= max_steps and grid_map[curr_y][curr_x] == 0:
            grid_map[curr_y][curr_x] = 1
            neighbor_directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1)]
            for delta_x, delta_y in neighbor_directions:
                next_x, next_y = curr_x + delta_x, curr_y + delta_y
                pq.heappush(node_queue, (curr_steps + 1, (next_x, next_y)))

def main():
    GRID_SIZE = 200
    MAP_OFFSET = 100

    while True:
        input_time_limit, input_count_obstacles = map(int, input().split())
        if input_time_limit == 0 and input_count_obstacles == 0:
            break

        grid_data = [[0 for col_idx in range(GRID_SIZE)] for row_idx in range(GRID_SIZE)]
        for _ in range(input_count_obstacles):
            obstacle_x, obstacle_y = map(lambda val: int(val) + MAP_OFFSET, input().split())
            grid_data[obstacle_y][obstacle_x] = -1
        start_x, start_y = map(lambda val: int(val) + MAP_OFFSET, input().split())
        search_bfs(start_x, start_y, input_time_limit, grid_data)

        accessible_cell_count = sum(
            0 if grid_data[row_idx][col_idx] == -1 else grid_data[row_idx][col_idx]
            for row_idx in range(GRID_SIZE)
            for col_idx in range(GRID_SIZE)
        )
        print(accessible_cell_count)

if __name__ == "__main__":
    main()