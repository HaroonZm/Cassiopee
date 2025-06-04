from heapq import heappush as pq_push, heappop as pq_pop

while True:
    col_count, row_count = map(int, input().split())
    if col_count == 0:
        break

    grid_map = ["B" + input() + "B" for _ in range(row_count)]
    grid_map.insert(0, "B" * (col_count + 2))
    grid_map.append("B" * (col_count + 2))

    prio_queue = []
    is_visited = [[False] * (col_count + 2) for _ in range(row_count + 2)]
    is_invalid = False

    for col_idx in range(1, col_count + 1):
        if grid_map[1][col_idx] == "&" or grid_map[row_count][col_idx] == "&":
            is_invalid = True
            break
        cost_t, step_t = (1, 0) if grid_map[1][col_idx] == "#" else (0, 1)
        cost_b, step_b = (1, 0) if grid_map[row_count][col_idx] == "#" else (0, 1)
        pq_push(prio_queue, (cost_t, step_t, (col_idx, 1)))
        pq_push(prio_queue, (cost_b, step_b, (col_idx, row_count)))
        is_visited[1][col_idx] = True
        is_visited[row_count][col_idx] = True

    for row_idx in range(1, row_count + 1):
        if grid_map[row_idx][1] == "&" or grid_map[row_idx][col_count] == "&":
            is_invalid = True
            break
        cost_l, step_l = (1, 0) if grid_map[row_idx][1] == "#" else (0, 1)
        cost_r, step_r = (1, 0) if grid_map[row_idx][col_count] == "#" else (0, 1)
        pq_push(prio_queue, (cost_l, step_l, (1, row_idx)))
        pq_push(prio_queue, (cost_r, step_r, (col_count, row_idx)))
        is_visited[row_idx][1] = True
        is_visited[row_idx][col_count] = True

    if is_invalid:
        print(0)
        continue

    adj_offsets = ((0, 1), (0, -1), (1, 0), (-1, 0))
    has_reached = False

    while prio_queue and not has_reached:
        curr_cost, wall_status, (curr_x, curr_y) = pq_pop(prio_queue)
        for dx, dy in adj_offsets:
            next_x, next_y = curr_x + dx, curr_y + dy
            if not is_visited[next_y][next_x]:
                is_visited[next_y][next_x] = True
                cell_type = grid_map[next_y][next_x]
                if cell_type == "&":
                    print(curr_cost)
                    has_reached = True
                    break
                elif cell_type == "#":
                    if wall_status == 1:
                        pq_push(prio_queue, (curr_cost + 1, 0, (next_x, next_y)))
                    else:
                        pq_push(prio_queue, (curr_cost, 0, (next_x, next_y)))
                elif cell_type == ".":
                    pq_push(prio_queue, (curr_cost, 1, (next_x, next_y)))