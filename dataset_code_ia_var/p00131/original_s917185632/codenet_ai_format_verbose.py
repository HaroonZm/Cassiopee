layer_masks = (
    [(512, 768, 512)] +
    [(256 >> bit_shift, 896 >> bit_shift, 256 >> bit_shift) for bit_shift in xrange(9)]
)

def apply_flip_mask(bitmask_rows, column_index, row_index):
    for affected_row, bitmask in zip(xrange(row_index - 1, row_index + 2), layer_masks[column_index]):
        bitmask_rows[affected_row] = bitmask_rows[affected_row] ^ bitmask

def solve_lights_out(initial_bitmask_rows):
    for first_row_flip_pattern in xrange(1 << 10):
        board_state = [0] + initial_bitmask_rows[:] + [0]
        flips_recorded = []
        # Apply flips for the first row according to current pattern
        for column_index in (idx for idx in xrange(10) if (1 << idx) & first_row_flip_pattern):
            apply_flip_mask(board_state, column_index, 1)
            flips_recorded.append((column_index, 0))
        board_state.pop(0)
        # Work down the rows to resolve on-state lights
        for row_index in xrange(9):
            for column_index in (idx for idx in xrange(10) if (1 << (9 - idx)) & board_state[row_index]):
                apply_flip_mask(board_state, column_index, row_index + 1)
                flips_recorded.append((column_index, row_index + 1))
        if board_state[9] == 0:
            return flips_recorded

for _ in xrange(input()):
    input_bitmask_rows = [
        int(raw_input().replace(" ", ""), 2)
        for _ in xrange(10)
    ]
    solution_flip_positions = solve_lights_out(input_bitmask_rows)
    print "\n".join([
        " ".join(
            "1" if (column_index, row_index) in solution_flip_positions else "0"
            for column_index in xrange(10)
        )
        for row_index in xrange(10)
    ])