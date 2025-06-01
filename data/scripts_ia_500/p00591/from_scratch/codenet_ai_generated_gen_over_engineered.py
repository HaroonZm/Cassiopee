class Matrix:
    def __init__(self, size, data):
        self._size = size
        self._data = data

    @property
    def size(self):
        return self._size

    def get_row(self, i):
        return self._data[i]

    def get_col(self, j):
        return [self._data[i][j] for i in range(self._size)]

    def get_element(self, i, j):
        return self._data[i][j]

class HandRaiser:
    def __init__(self, matrix):
        self._matrix = matrix
        self._left_hand_rows = []
        self._right_hand_cols = []

    def find_left_hand_indices(self):
        # indices of shortest students in each row who raise left hand
        self._left_hand_rows = []
        for i in range(self._matrix.size):
            row = self._matrix.get_row(i)
            min_height = min(row)
            # multiple shortest possible; include all
            indices = [idx for idx, h in enumerate(row) if h == min_height]
            self._left_hand_rows.append( (i, set(indices)) )

    def find_right_hand_indices(self):
        # indices of tallest students in each column who raise right hand
        self._right_hand_cols = []
        for j in range(self._matrix.size):
            col = self._matrix.get_col(j)
            max_height = max(col)
            # multiple tallest possible; include all
            indices = [idx for idx, h in enumerate(col) if h == max_height]
            self._right_hand_cols.append( (j, set(indices)) )

    def find_target_student(self):
        # find the student who has both hands up
        # i,j such that (i,j) shortest in row i and tallest in col j
        # we have left_hand_rows as list of (i, set_of_col_indices)
        # and right_hand_cols as list of (j, set_of_row_indices)
        left_hand_positions = set()
        for i, cols in self._left_hand_rows:
            for j in cols:
                left_hand_positions.add((i,j))

        right_hand_positions = set()
        for j, rows in self._right_hand_cols:
            for i in rows:
                right_hand_positions.add((i,j))

        intersect = left_hand_positions & right_hand_positions
        if not intersect:
            return 0

        # If multiple, return the height of one of them
        # According to problem, there is only one such student really, but not enforced
        i, j = intersect.pop()
        height = self._matrix.get_element(i,j)
        return height

class AdvancedAlgorithmClass:
    def __init__(self):
        self.cases = []

    def read_input(self):
        while True:
            n = int(input())
            if n == 0:
                break
            data = []
            for _ in range(n):
                row = list(map(int, input().strip().split()))
                data.append(row)
            self.cases.append( Matrix(n, data) )

    def process_cases(self):
        results = []
        for matrix in self.cases:
            hr = HandRaiser(matrix)
            hr.find_left_hand_indices()
            hr.find_right_hand_indices()
            result = hr.find_target_student()
            results.append(result)
        return results

def main():
    app = AdvancedAlgorithmClass()
    app.read_input()
    results = app.process_cases()
    for res in results:
        print(res)

if __name__ == "__main__":
    main()