from itertools import product

def place_piece(board_width, board_height, current_bitmap, remaining_pieces, placed_pieces, solution_count, solutions):
    
    if not remaining_pieces:
        return solution_count + 1, placed_pieces
    
    if solution_count > 1:
        return 2, placed_pieces
    
    piece_id, piece_area, anchor_y, anchor_x = remaining_pieces[-1]
    
    possible_dimensions = set([
        (piece_area // i, piece_area // (piece_area // i))
        for i in range(1, min(board_width + 1, piece_area + 1))
        if not (piece_area // i) * (piece_area // (piece_area // i)) - piece_area
    ])
    
    for piece_height, piece_width in possible_dimensions:
        
        start_y = max(0, anchor_y - piece_height + 1)
        end_y = min(board_height - piece_height + 1, anchor_y + 1)
        
        start_x = max(0, anchor_x - piece_width + 1)
        end_x = min(board_width - piece_width + 1, anchor_x + 1)
        
        for top_y, left_x in product(range(start_y, end_y), range(start_x, end_x)):
            
            bottom_y = top_y + piece_height - 1
            right_x = left_x + piece_width - 1
            
            piece_bitmap = (
                sum([
                    (2 ** (right_x - left_x + 1) - 1) << row_index * board_width
                    for row_index in range(bottom_y - top_y + 1)
                ]) << (board_width - right_x - 1)
            ) << (board_height - bottom_y - 1) * board_width
            
            anchor_mark = (1 << (board_width - anchor_x - 1)) << (board_height - anchor_y - 1) * board_width
            
            if not (current_bitmap & piece_bitmap) ^ anchor_mark:
                new_bitmap = current_bitmap | piece_bitmap
                new_placed_pieces = placed_pieces + [[piece_id, piece_area, top_y, left_x, bottom_y, right_x]]
                solution_count, solutions = place_piece(
                    board_width,
                    board_height,
                    new_bitmap,
                    remaining_pieces[:-1],
                    new_placed_pieces,
                    solution_count,
                    solutions
                )
            
            if solution_count > 1:
                return 2, solutions
    
    return solution_count, solutions


def main():
    while True:
        board_width, board_height, number_of_pieces = map(int, input().split())
        
        if board_width == 0:
            break
        
        piece_base_data = sorted([list(map(int, input().split())) for _ in range(number_of_pieces)])
        
        board_status_rows = [list(map(int, input().split())) for _ in range(board_height)]
        
        active_cells = sorted([
            [board_status_rows[row][col], row, col]
            for row, col in product(range(board_height), range(board_width))
            if board_status_rows[row][col]
        ])
        
        combined_data = [piece_base_data[i] + active_cells[i][1:] for i in range(number_of_pieces)]
        
        bitmap_string = "".join([
            "".join(["1" if board_status_rows[row][col] else "0" for col in range(board_width)])
            for row in range(board_height)
        ])
        
        bitmap_integer = int(bitmap_string, 2)
        
        total_solutions, solutions_found = place_piece(
            board_width,
            board_height,
            bitmap_integer,
            combined_data,
            [],
            0,
            0
        )
        
        if total_solutions > 1:
            print("NA")
        elif total_solutions == 1:
            output_grid = [[0] * board_width for _ in range(board_height)]
            for piece_info in solutions_found:
                piece_identifier, _, start_row, start_col, end_row, end_col = piece_info
                for row_index in range(start_row, end_row + 1):
                    output_grid[row_index][start_col:end_col + 1] = [piece_identifier] * (end_col - start_col + 1)
            
            for row in output_grid:
                print(" ".join(str(cell) for cell in row))
        else:
            print("NA")


if __name__ == "__main__":
    main()