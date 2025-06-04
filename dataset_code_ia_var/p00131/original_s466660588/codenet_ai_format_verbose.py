layer_flip_bitmasks = (
    [(512, 768, 512)] +
    [
        (256 >> shift_amount, 896 >> shift_amount, 256 >> shift_amount)
        for shift_amount in xrange(9)
    ]
)

def apply_flip_mask_to_grid(grid_rows, flip_x, flip_y):
    for target_row_index, bitmask in zip(
        xrange(flip_y - 1, flip_y + 2),
        layer_flip_bitmasks[flip_x]
    ):
        grid_rows[target_row_index] = grid_rows[target_row_index] ^ bitmask

def find_solution_for_initial_grid(initial_grid_rows):
    for first_row_flip_combination in xrange(1 << 10):
        # Pad grid with zeros at both ends for boundary management
        current_grid_rows = [0] + initial_grid_rows + [0]
        flip_positions_sequence = []

        # Handle flips in the first row
        for flip_x in (x for x in xrange(10) if (1 << x) & first_row_flip_combination):
            apply_flip_mask_to_grid(current_grid_rows, flip_x, 1)
            flip_positions_sequence.append((flip_x, 0))

        # Remove the padding after first row handled
        current_grid_rows.pop(0)

        # Iterate through subsequent rows to clear any set bits in grid
        for row_index in xrange(9):
            for flip_x in (x for x in xrange(10) if (1 << (9 - x)) & current_grid_rows[row_index]):
                apply_flip_mask_to_grid(current_grid_rows, flip_x, row_index + 1)
                flip_positions_sequence.append((flip_x, row_index + 1))

        # If the bottom row is all cleared, this is a solution
        if current_grid_rows[9] == 0:
            return flip_positions_sequence

for test_case_index in xrange(input()):
    initial_grid_rows = [
        int(raw_input().replace(" ", ""), 2)
        for _ in xrange(10)
    ]
    solution_flip_positions = find_solution_for_initial_grid(initial_grid_rows)
    for output_row_index in xrange(10):
        print " ".join(
            "1" if (flip_x, output_row_index) in solution_flip_positions else "0"
            for flip_x in xrange(10)
        )