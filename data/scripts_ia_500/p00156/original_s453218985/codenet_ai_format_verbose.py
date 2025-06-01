from heapq import heappush, heappop, heapify
from itertools import product

def solve_minimum_cost_path():
    
    starting_positions = [
        (0, row_index, column_index)
        for row_index, column_index in product(range(grid_height), range(grid_width))
        if not (0 < row_index < grid_height - 1 and 0 < column_index < grid_width - 1)
    ]
    
    priority_queue = starting_positions[:]
    heapify(priority_queue)
    
    while len(priority_queue) != 0:
        
        current_cost, current_row, current_column = heappop(priority_queue)
        
        if field[current_row][current_column] == "&":
            return current_cost
        
        if cost_memoization[current_row][current_column] <= current_cost:
            continue
        
        cost_memoization[current_row][current_column] = current_cost
        
        for delta_x, delta_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            
            neighbor_row = current_row + delta_y
            neighbor_column = current_column + delta_x
            
            if 0 <= neighbor_row < grid_height and 0 <= neighbor_column < grid_width:
                
                if (
                    field[neighbor_row][neighbor_column] != "#"
                    and field[current_row][current_column] == "#"
                ):
                    heappush(priority_queue, (current_cost + 1, neighbor_row, neighbor_column))
                else:
                    heappush(priority_queue, (current_cost, neighbor_row, neighbor_column))


while True:
    
    grid_width, grid_height = map(int, raw_input().split())
    
    if grid_width | grid_height == 0:
        break
    
    cost_memoization = [[1 << 20] * grid_width for _ in range(grid_height)]
    
    field = [raw_input() for _ in range(grid_height)]
    
    print(solve_minimum_cost_path())