class GameBoard:
    def __init__(self, board_size):
        self.board_size = board_size

        self.grid = [
            [None for _ in range(board_size)]
            for _ in range(board_size)
        ]

    def duplicate_board(self):
        duplicated_board = GameBoard(self.board_size)
        for row_index in range(self.board_size):
            current_row = self.grid[row_index]
            duplicated_board.grid[row_index] = current_row[:]
        return duplicated_board

    def set_cell_value(self, row_index, column_index, value):
        self.grid[row_index][column_index] = value

    def set_cells_in_group(self, group_of_cells, value):
        for cell_coordinates in group_of_cells:
            row_index, column_index = cell_coordinates
            self.grid[row_index][column_index] = value

    def calculate_points_for_cell_group(self, row_index, column_index, player_value):
        cell_value = self.grid[row_index][column_index]

        if cell_value == 0 or cell_value == -1:
            return 0

        connected_group_cells = set()
        self.find_connected_group(row_index, column_index, cell_value, connected_group_cells)

        is_group_adjacent_to_empty_cell = False
        for cell_coordinates in connected_group_cells:
            neighbor_row, neighbor_col = cell_coordinates
            if self.is_adjacent_to_zero(neighbor_row, neighbor_col):
                is_group_adjacent_to_empty_cell = True
                break

        self.set_cells_in_group(connected_group_cells, -1)

        if is_group_adjacent_to_empty_cell:
            return 0

        if cell_value == player_value:
            return len(connected_group_cells) * -1
        else:
            return len(connected_group_cells)

    def calculate_move_points(self, row_index, column_index, player_value):
        neighbor_cells = self.get_neighbor_coordinates(row_index, column_index)

        points = self.calculate_points_for_cell_group(row_index, column_index, player_value)

        for neighbor in neighbor_cells:
            neighbor_row, neighbor_col = neighbor
            points += self.calculate_points_for_cell_group(neighbor_row, neighbor_col, player_value)

        return points

    def get_neighbor_coordinates(self, row_index, column_index):
        neighbors = []
        if row_index < self.board_size - 1:
            neighbors.append((row_index + 1, column_index))
            neighbors.append((row_index + 1, column_index + 1))
        if column_index <= row_index - 1:
            neighbors.append((row_index, column_index + 1))
            neighbors.append((row_index - 1, column_index))
        if column_index > 0:
            neighbors.append((row_index, column_index - 1))
            neighbors.append((row_index - 1, column_index - 1))
        return neighbors

    def is_adjacent_to_zero(self, row_index, column_index):
        neighbor_cells = self.get_neighbor_coordinates(row_index, column_index)
        for neighbor in neighbor_cells:
            neighbor_row, neighbor_col = neighbor
            if self.grid[neighbor_row][neighbor_col] == 0:
                return True
        return False

    def find_connected_group(self, row_index, column_index, target_value, connected_cells_set):
        if (row_index, column_index) in connected_cells_set:
            return
        if self.grid[row_index][column_index] == target_value:
            connected_cells_set.add((row_index, column_index))
            neighbor_cells = self.get_neighbor_coordinates(row_index, column_index)
            for neighbor in neighbor_cells:
                neighbor_row, neighbor_col = neighbor
                self.find_connected_group(neighbor_row, neighbor_col, target_value, connected_cells_set)

if __name__ == '__main__':
    while True:
        user_input = input().strip().split()
        board_size, current_player_value = map(int, user_input)
        if board_size == 0 and current_player_value == 0:
            break

        game_board = GameBoard(board_size)
        available_empty_cells = []

        for row_index in range(board_size):
            row_input = input().strip().split(' ')
            row_values = [int(x) for x in row_input if x != '']
            for column_index, cell_value in enumerate(row_values):
                game_board.set_cell_value(row_index, column_index, cell_value)
                if cell_value == 0:
                    available_empty_cells.append((row_index, column_index))

        maximum_points_achievable = -999999999
        for empty_cell_coordinates in available_empty_cells:
            empty_row, empty_col = empty_cell_coordinates
            simulated_game_board = game_board.duplicate_board()
            simulated_game_board.set_cell_value(empty_row, empty_col, current_player_value)
            cell_points = simulated_game_board.calculate_move_points(empty_row, empty_col, current_player_value)
            maximum_points_achievable = max(maximum_points_achievable, cell_points)

        print(maximum_points_achievable)