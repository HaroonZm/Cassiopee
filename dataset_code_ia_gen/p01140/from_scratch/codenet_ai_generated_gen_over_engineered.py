class DistanceSequence:
    def __init__(self, distances):
        self.distances = distances
        self.prefix_sums = self._compute_prefix_sums(distances)

    def _compute_prefix_sums(self, distances):
        prefix = [0]
        for d in distances:
            prefix.append(prefix[-1] + d)
        return prefix

    def length(self):
        return len(self.distances)

    def segment_length(self, start_index, length):
        # length: number of segments (edges) to sum
        return self.prefix_sums[start_index + length] - self.prefix_sums[start_index]


class SquareCounter:
    def __init__(self, vertical_gaps, horizontal_gaps):
        self.vertical = DistanceSequence(vertical_gaps)
        self.horizontal = DistanceSequence(horizontal_gaps)

    def count_squares(self):
        count = 0
        max_size = min(self.vertical.length(), self.horizontal.length())
        v_len = self.vertical.length()
        h_len = self.horizontal.length()
        # For each possible square size (length in edges)
        for size in range(1, max_size + 1):
            # Collect all vertical side lengths of size 'size'
            vertical_lengths = set()
            for i in range(v_len - size + 1):
                length = self.vertical.segment_length(i, size)
                vertical_lengths.add(length)
            # For each horizontal segment of size 'size', check if length in vertical_lengths
            for j in range(h_len - size + 1):
                length = self.horizontal.segment_length(j, size)
                if length in vertical_lengths:
                    count += 1
        return count


class SquareRouteSolver:
    def __init__(self):
        self.data_sets = []

    def add_data_set(self, n, m, vertical_distances, horizontal_distances):
        self.data_sets.append((n, m, vertical_distances, horizontal_distances))

    def solve(self):
        results = []
        for n, m, vertical_distances, horizontal_distances in self.data_sets:
            counter = SquareCounter(vertical_distances, horizontal_distances)
            results.append(counter.count_squares())
        return results


class InputHandler:
    def __init__(self):
        self.solver = SquareRouteSolver()

    def process_input(self):
        import sys
        input_iter = iter(sys.stdin.read().strip().split())
        while True:
            try:
                n = int(next(input_iter))
                m = int(next(input_iter))
            except StopIteration:
                break
            if n == 0 and m == 0:
                break
            vertical_distances = [int(next(input_iter)) for _ in range(n)]
            horizontal_distances = [int(next(input_iter)) for _ in range(m)]
            self.solver.add_data_set(n, m, vertical_distances, horizontal_distances)

    def print_results(self):
        results = self.solver.solve()
        for res in results:
            print(res)


def main():
    input_handler = InputHandler()
    input_handler.process_input()
    input_handler.print_results()


if __name__ == "__main__":
    main()