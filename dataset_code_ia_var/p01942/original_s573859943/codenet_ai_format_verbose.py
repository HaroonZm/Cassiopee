class TwoDimensionalFenwickTree:

    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.fenwick_tree_matrix = [
            [0] * (num_cols + 1) for _ in range(num_rows + 1)
        ]

    def initialize_with_matrix(self, input_matrix):
        for row_index in range(self.num_rows):
            for col_index in range(self.num_cols):
                self.add_value(row_index + 1, col_index + 1, input_matrix[row_index][col_index])

    def add_value(self, row, col, value_to_add):
        if row <= 0 or col <= 0:
            raise IndexError("Row and column indices must be positive (1-based).")
        current_row = row
        while current_row <= self.num_rows:
            current_col = col
            while current_col <= self.num_cols:
                self.fenwick_tree_matrix[current_row][current_col] += value_to_add
                current_col += (current_col & -current_col)
            current_row += (current_row & -current_row)

    def prefix_sum(self, row, col):
        if row < 0 or col < 0:
            raise IndexError("Row and column indices must be non-negative (1-based).")
        cumulative_sum = 0
        current_row = row
        while current_row > 0:
            current_col = col
            while current_col > 0:
                cumulative_sum += self.fenwick_tree_matrix[current_row][current_col]
                current_col -= (current_col & -current_col)
            current_row -= (current_row & -current_row)
        return cumulative_sum

    def rectangle_sum(self, top_row_exclusive, bottom_row_inclusive, left_col_exclusive, right_col_inclusive):
        """
        Args:
            top_row_exclusive: exclusive top row index (0-based)
            bottom_row_inclusive: inclusive bottom row index (1-based)
            left_col_exclusive: exclusive left column index (0-based)
            right_col_inclusive: inclusive right column index (1-based)
        Returns:
            Total sum within the rectangular area defined by rows [top_row_exclusive, bottom_row_inclusive)
            and columns [left_col_exclusive, right_col_inclusive)
        """
        return (
            self.prefix_sum(bottom_row_inclusive, right_col_inclusive)
            - self.prefix_sum(bottom_row_inclusive, left_col_exclusive)
            - self.prefix_sum(top_row_exclusive, right_col_inclusive)
            + self.prefix_sum(top_row_exclusive, left_col_exclusive)
        )


def main():
    import sys
    from collections import deque

    buffered_input = sys.stdin.buffer.readline

    num_rows, num_cols, baking_time, num_queries = (int(token) for token in buffered_input().split())

    not_baked_cakes_tree = TwoDimensionalFenwickTree(num_rows, num_cols)
    baked_cakes_tree = TwoDimensionalFenwickTree(num_rows, num_cols)

    scheduled_baking_times = deque()
    scheduled_baking_rows = deque()
    scheduled_baking_cols = deque()

    for _ in range(num_queries):
        query_parts = [int(token) for token in buffered_input().split()]
        current_time = query_parts[0]
        query_type = query_parts[1]
        remaining_data = query_parts[2:]

        # Handle baking schedule expiration
        while scheduled_baking_times and scheduled_baking_times[0] <= current_time:
            _ = scheduled_baking_times.popleft()
            baking_row = scheduled_baking_rows.popleft()
            baking_col = scheduled_baking_cols.popleft()
            not_baked_cakes_tree.add_value(baking_row, baking_col, -1)
            baked_cakes_tree.add_value(baking_row, baking_col, 1)

        if query_type == 0:
            # Register a new cake to bake
            cake_row, cake_col = remaining_data
            not_baked_cakes_tree.add_value(cake_row, cake_col, 1)
            scheduled_baking_times.append(current_time + baking_time)
            scheduled_baking_rows.append(cake_row)
            scheduled_baking_cols.append(cake_col)

        elif query_type == 1:
            # Eat a baked cake, if available
            cake_row, cake_col = remaining_data
            already_baked_count = baked_cakes_tree.rectangle_sum(
                cake_row - 1, cake_row, cake_col - 1, cake_col
            )
            if already_baked_count > 0:
                baked_cakes_tree.add_value(cake_row, cake_col, -1)

        else:
            # Query for total baked and not baked cakes in given rectangle
            top_row, left_col, bottom_row, right_col = remaining_data
            baked_cakes_count = baked_cakes_tree.rectangle_sum(
                top_row - 1, bottom_row, left_col - 1, right_col
            )
            not_baked_cakes_count = not_baked_cakes_tree.rectangle_sum(
                top_row - 1, bottom_row, left_col - 1, right_col
            )
            print(baked_cakes_count, not_baked_cakes_count)


if __name__ == '__main__':
    main()