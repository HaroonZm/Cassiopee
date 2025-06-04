class GridProcessor:
    def __init__(self):
        self.grid_data = []

    def load_grid(self, row_count, col_count):
        self.row_count, self.col_count = row_count, col_count
        for row_idx in range(self.row_count):
            raw_row = raw_input()
            row_list = []
            for col_idx in range(len(raw_row)):
                row_list.append(raw_row[col_idx])
            self.grid_data.append(row_list)

    def process_grid(self):
        pos_row, pos_col = 0, 0

        while True:
            current_cell = self.grid_data[pos_row][pos_col]
            if current_cell == ">":
                self.grid_data[pos_row][pos_col] = "#"
                pos_col += 1
            elif current_cell == "<":
                self.grid_data[pos_row][pos_col] = "#"
                pos_col -= 1
            elif current_cell == "^":
                self.grid_data[pos_row][pos_col] = "#"
                pos_row -= 1
            elif current_cell == "v":
                self.grid_data[pos_row][pos_col] = "#"
                pos_row += 1
            elif current_cell == ".":
                print pos_col, pos_row
                break
            else:
                print "LOOP"
                break

def execute_grid_handler():
    while True:
        input_dims = raw_input().split()
        row_count, col_count = map(int, input_dims)
        if row_count == 0 and col_count == 0:
            break
        grid_instance = GridProcessor()
        grid_instance.load_grid(row_count, col_count)
        grid_instance.process_grid()

if __name__ == "__main__":
    execute_grid_handler()