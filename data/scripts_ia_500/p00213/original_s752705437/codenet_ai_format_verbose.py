from itertools import product

def place_piece(grid_width, grid_height, occupied_bitmap, unused_pieces, placed_pieces, solution_count, solution_pieces):
    
    if not unused_pieces:
        return solution_count + 1, placed_pieces
    
    if solution_count > 1:
        return 2, placed_pieces
    
    base_color, area, last_placed_y, last_placed_x = unused_pieces[-1]
    
    for piece_height, piece_width in set([
        (area // divisor, area // (area // divisor))
        for divisor in range(1, min(grid_width + 1, area + 1))
        if not (area // divisor) * (area // (area // divisor)) - area
    ]):
        
        possible_start_y_min = max(0, last_placed_y - piece_height + 1)
        possible_start_y_max = min(grid_height - piece_height + 1, last_placed_y + 1)
        possible_start_x_min = max(0, last_placed_x - piece_width + 1)
        possible_start_x_max = min(grid_width - piece_width + 1, last_placed_x + 1)
        
        for start_y, start_x in product(
            range(possible_start_y_min, possible_start_y_max),
            range(possible_start_x_min, possible_start_x_max)
        ):
            
            end_y = start_y + piece_height - 1
            end_x = start_x + piece_width - 1
            
            piece_bitmask = (
                sum(
                    (2 ** (end_x - start_x + 1) - 1) << row_index * grid_width
                    for row_index in range(end_y - start_y + 1)
                ) << (grid_width - end_x - 1)
            ) << (grid_height - end_y - 1) * grid_width
            
            single_cell_mark = (1 << (grid_width - last_placed_x - 1)) << (grid_height - last_placed_y -1) * grid_width
            
            if not (occupied_bitmap & piece_bitmask) ^ single_cell_mark:
                solution_count, solution_pieces = place_piece(
                    grid_width, grid_height,
                    occupied_bitmap | piece_bitmask,
                    unused_pieces[:-1],
                    placed_pieces + [[base_color, area, start_y, start_x, end_y, end_x]],
                    solution_count,
                    solution_pieces
                )
            
            if solution_count > 1:
                return 2, solution_pieces
    else:
        return solution_count, solution_pieces



def main():
    while True:
        grid_width, grid_height, num_pieces = map(int, input().split())
        if grid_width == 0:
            break
        
        piece_base_area_list = sorted([list(map(int, input().split())) for _ in range(num_pieces)])
        grid_state = [list(map(int, input().split())) for _ in range(grid_height)]
        
        # Collect all cells with non-zero value and sort them by number, y, x ascending
        cells_with_numbers_sorted = sorted(
            [ [grid_state[i][j], i, j] for i, j in product(range(grid_height), range(grid_width)) if grid_state[i][j] ],
            key=lambda cell: cell[0]
        )
        
        # Prepare combined list with piece info and coordinates per their order
        combined_piece_coord_list = [
            piece_base_area_list[i] + cells_with_numbers_sorted[i][1:]
            for i in range(num_pieces)
        ]
        
        # Prepare bitmap of the grid: 1 if cell occupied, 0 else
        occupied_string = "".join(
            "".join("1" if grid_state[i][j] else "0" for j in range(grid_width))
            for i in range(grid_height)
        )
        
        current_solution_count, solution_placements = place_piece(
            grid_width,
            grid_height,
            int(occupied_string, 2),
            combined_piece_coord_list,
            [],
            0,
            0
        )
        
        if current_solution_count > 1 or current_solution_count == 0:
            print("NA")
        else:
            output_grid = [[0] * grid_width for _ in range(grid_height)]
            for index, _, start_y, start_x, end_y, end_x in solution_placements:
                for row_index in range(start_y, end_y + 1):
                    output_grid[row_index][start_x:end_x + 1] = [index] * (end_x - start_x + 1)
            for row in output_grid:
                print(" ".join(str(cell) for cell in row))


if __name__ == "__main__":
    main()