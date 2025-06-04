from collections import deque
import sys
input = sys.stdin.readline

def slide_puzzle_solver():
    while True:
        grid_width, grid_height = map(int, input().split())
        if grid_width == 0:
            break

        grid_map = [list(map(int, input().split())) for row_idx in range(grid_height)]

        start_x, start_y, goal_x, goal_y = 0, 0, 0, 0
        wall_id_counter = 1

        for y_idx in range(grid_height):
            for x_idx in range(grid_width):
                cell_value = grid_map[y_idx][x_idx]
                if cell_value == 1:
                    grid_map[y_idx][x_idx] = wall_id_counter
                    wall_id_counter += 1
                elif cell_value == 2:
                    start_x, start_y = x_idx, y_idx
                    grid_map[y_idx][x_idx] = 0
                elif cell_value == 3:
                    goal_x, goal_y = x_idx, y_idx
                    grid_map[y_idx][x_idx] = 0

        queue_state = deque()
        queue_state.append([start_x, start_y, 0, 0, 0, [0], 1])
        solution_steps = -1

        while len(queue_state) > 0:
            curr_x, curr_y, curr_steps, move_dx, move_dy, visited_walls, walls_count = queue_state.popleft()
            if curr_x == goal_x and curr_y == goal_y:
                solution_steps = curr_steps
                break

            if move_dx == 0 and move_dy == 0:
                if curr_steps + 1 < 11:
                    for next_dx, next_dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                        next_x, next_y = curr_x + next_dx, curr_y + next_dy
                        if 0 <= next_x < grid_width and 0 <= next_y < grid_height:
                            neighbor_cell = grid_map[next_y][next_x]
                            if neighbor_cell in visited_walls[:walls_count]:
                                queue_state.append([next_x, next_y, curr_steps + 1, next_dx, next_dy, visited_walls[:walls_count], walls_count])
            else:
                slide_x, slide_y = curr_x, curr_y
                hit_boundary = False
                reached_goal = False

                while True:
                    next_slide_x = slide_x + move_dx
                    next_slide_y = slide_y + move_dy
                    if next_slide_x == goal_x and next_slide_y == goal_y:
                        solution_steps = curr_steps
                        reached_goal = True
                        break
                    if 0 <= next_slide_x < grid_width and 0 <= next_slide_y < grid_height:
                        if grid_map[next_slide_y][next_slide_x] not in visited_walls[:walls_count]:
                            break
                    else:
                        hit_boundary = True
                        break
                    slide_x += move_dx
                    slide_y += move_dy

                if reached_goal:
                    break
                if not hit_boundary:
                    next_wall = grid_map[slide_y + move_dy][slide_x + move_dx]
                    new_visited_walls = visited_walls[:walls_count] + [next_wall]
                    queue_state.append([slide_x, slide_y, curr_steps, 0, 0, new_visited_walls, walls_count + 1])

        print(solution_steps)

if __name__ == "__main__":
    slide_puzzle_solver()