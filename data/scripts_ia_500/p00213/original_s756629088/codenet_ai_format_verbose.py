from itertools import product

def place_piece(grid_width, grid_height, occupied_bitmap, remaining_pieces, placed_pieces, num_solutions, solution_pieces, fin_flag):
    
    if fin_flag:
        return num_solutions, solution_pieces
    
    if not remaining_pieces:
        solution_pieces = placed_pieces
        return num_solutions + 1, solution_pieces
    
    if num_solutions > 1:
        return 2, placed_pieces
    
    piece_id, piece_area, original_y, original_x = remaining_pieces[-1]
    
    possible_dimensions = set()
    for divisor_candidate in range(1, min(grid_width + 1, piece_area + 1)):
        height_candidate = divisor_candidate
        width_candidate = piece_area // divisor_candidate
        if height_candidate * width_candidate == piece_area:
            possible_dimensions.add((height_candidate, width_candidate))
    
    for piece_height, piece_width in possible_dimensions:
        
        start_y_range = range(max(0, original_y - piece_height + 1), min(grid_height - piece_height + 1, original_y + 1))
        start_x_range = range(max(0, original_x - piece_width + 1), min(grid_width - piece_width + 1, original_x + 1))
        
        for placement_top, placement_left in product(start_y_range, start_x_range):
            
            placement_bottom = placement_top + piece_height - 1
            placement_right = placement_left + piece_width - 1
            
            horizontal_mask = (2 ** (placement_right - placement_left + 1)) - 1
            vertical_mask = 0
            for row_offset in range(placement_bottom - placement_top + 1):
                vertical_mask |= horizontal_mask << (row_offset * grid_width)
            
            aligned_mask = (vertical_mask << (grid_width - 1 - placement_right)) << ((grid_height - 1 - placement_bottom) * grid_width)
            
            check_mark = (1 << (grid_width - 1 - original_x)) << ((grid_height - 1 - original_y) * grid_width)
            
            if not (occupied_bitmap & aligned_mask) ^ check_mark:
                num_solutions, solution_pieces = place_piece(
                    grid_width,
                    grid_height,
                    occupied_bitmap | aligned_mask,
                    remaining_pieces[:-1],
                    placed_pieces + [[piece_id, piece_area, placement_top, placement_left, placement_bottom, placement_right]],
                    num_solutions,
                    solution_pieces,
                    False
                )
            
            if num_solutions > 1:
                return 2, solution_pieces
                
    return num_solutions, solution_pieces


def main():
    
    while True:
        
        grid_width, grid_height, num_pieces = map(int, input().split())
        
        if grid_width == 0:
            break
        
        pieces_with_area = sorted([list(map(int, input().split())) for _ in range(num_pieces)])
        
        grid_row_values = [list(map(int, input().split())) for _ in range(grid_height)]
        
        cells_with_values = sorted(
            [
                [grid_row_values[row][col], row, col]
                for row, col in product(range(grid_height), range(grid_width))
                if grid_row_values[row][col]
            ]
        )
        
        pieces_with_positions = [
            pieces_with_area[i] + cells_with_values[i][1:]
            for i in range(num_pieces)
        ]
        
        binary_grid_string = "".join(
            [
                "".join(["1" if grid_row_values[row][col] else "0" for col in range(grid_width)])
                for row in range(grid_height)
            ]
        )
        
        num_solutions_found, solution_pieces = place_piece(
            grid_width,
            grid_height,
            int(binary_grid_string, 2),
            pieces_with_positions,
            [],
            0,
            0,
            False
        )
        
        if num_solutions_found > 1:
            print("NA")
        elif num_solutions_found == 1:
            output_grid = [[0] * grid_width for _ in range(grid_height)]
            
            for piece_info in solution_pieces:
                piece_index, _, start_y, start_x, end_y, end_x = piece_info
                
                for row in range(start_y, end_y + 1):
                    output_grid[row][start_x:end_x + 1] = [piece_index] * (end_x - start_x + 1)
            
            for row in output_grid:
                print(" ".join(str(cell) for cell in row))
        else:
            print("NA")


if __name__ == "__main__":
    main()