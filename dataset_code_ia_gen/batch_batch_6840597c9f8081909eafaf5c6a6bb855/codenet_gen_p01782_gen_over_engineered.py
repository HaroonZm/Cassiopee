class CharacterSelector:
    def __init__(self, plate_matrix):
        self.matrix = plate_matrix
        self.N = len(plate_matrix)
        self.selected_columns = set()
        self.current_selection = []
        self.best_selection = None

    def is_column_available(self, col):
        return col not in self.selected_columns

    def select(self, row, col):
        self.current_selection.append(self.matrix[row][col])
        self.selected_columns.add(col)

    def unselect(self, col):
        self.current_selection.pop()
        self.selected_columns.remove(col)

    def current_string(self):
        return ''.join(self.current_selection)

    def update_best(self):
        candidate = self.current_string()
        if self.best_selection is None or candidate < self.best_selection:
            self.best_selection = candidate

class DecoderState:
    def __init__(self, plate_matrix):
        self.N = len(plate_matrix)
        self.selector = CharacterSelector(plate_matrix)
        # Precompute per row sorted columns by character for early pruning and ordering
        self.sorted_cols_per_row = [sorted(range(self.N), key=lambda c: plate_matrix[r][c]) for r in range(self.N)]

class MessageDecoder:
    def __init__(self, plate_matrix):
        self.state = DecoderState(plate_matrix)

    def decode(self):
        self._search(0)
        return self.state.selector.best_selection

    def _search(self, row):
        # If all rows processed, update best solution
        if row == self.state.N:
            self.state.selector.update_best()
            return

        for col in self.state.sorted_cols_per_row[row]:
            if self.state.selector.is_column_available(col):
                self.state.selector.select(row, col)
                curr_str = self.state.selector.current_string()

                # Prune if current string prefix can't be better than best
                best = self.state.selector.best_selection
                if best is None or curr_str < best[:len(curr_str)]:
                    self._search(row + 1)
                self.state.selector.unselect(col)

class PlateParser:
    @staticmethod
    def parse_input():
        N = int(input())
        matrix = [list(input().strip()) for _ in range(N)]
        return matrix

class AncientMessageDecoderApp:
    def __init__(self):
        self.plate_matrix = None
        self.decoder = None

    def run(self):
        self._prepare()
        message = self.decoder.decode()
        print(message)

    def _prepare(self):
        self.plate_matrix = PlateParser.parse_input()
        self.decoder = MessageDecoder(self.plate_matrix)

if __name__ == "__main__":
    AncientMessageDecoderApp().run()