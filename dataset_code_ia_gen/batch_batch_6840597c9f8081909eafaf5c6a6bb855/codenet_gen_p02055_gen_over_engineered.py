class ColorAllocator:
    def __init__(self, length, red_count):
        self.length = length
        self.red_count = red_count
        self.blue_count = length - red_count
        self.colors = [None] * length  # store 'R' or 'B'

    def assign_colors(self):
        # We'll assign 'R' to first red_count positions,
        # 'B' to remaining
        for i in range(self.length):
            if i < self.red_count:
                self.colors[i] = 'R'
            else:
                self.colors[i] = 'B'

    def get_colors(self):
        return self.colors


class Sequence:
    def __init__(self, elements):
        self.elements = elements
        self.length = len(elements)
        self.sorted = sorted(elements)


class SortabilityEvaluator:
    def __init__(self, sequence: Sequence, allocator: ColorAllocator):
        self.sequence = sequence
        self.allocator = allocator

    def can_sort(self):
        color_assignment = [None] * self.sequence.length

        # The problem is:
        # We want to paint R exactly red_count elements, B others,
        # such that by swapping only elements of the same color,
        # we can get sorted sequence.

        # Since elements can be swapped only within the same color,
        # the elements at positions that share a color should be rearrangable to
        # match the sorted array at those positions.

        # Approach:
        # We assign colors to positions based on sorted array:
        # The first red_count elements in sorted array are 'R', rest 'B'.
        # We then check if for every element in original array, the color of the element
        # is consistent with the color of its position in the sorted array.

        # This means: for each element in sequence, find its position in sorted array,
        # check if color assigned to position equals color assigned to element's position.

        # Because positions can only swap with same color, elements must be colored so
        # that the original element color = sorted position color.

        # Let's create a mapping from element value to its sorted index.
        value_to_sorted_idx = {v: i for i, v in enumerate(self.sequence.sorted)}

        # Assign colors based on sorted index
        sorted_colors = ['R' if i < self.allocator.red_count else 'B' for i in range(self.sequence.length)]

        # Now, for each element in original sequence, the color must be consistent:
        # the color of the element at position i in the original must be the same as the color at its sorted position

        # Assign colors to original positions according to their element's sorted index color
        for i, val in enumerate(self.sequence.elements):
            sorted_idx = value_to_sorted_idx[val]
            color_assignment[i] = sorted_colors[sorted_idx]

        # Count how many are assigned 'R' in color_assignment; must be exactly red_count
        if color_assignment.count('R') != self.allocator.red_count:
            return False

        # Check if possible: equivalently yes, since all elements can swap with others of same color
        # So answer is yes if above condition met

        # Store result for potential future use
        self.allocator.colors = color_assignment
        return True


class SolutionFacade:
    def __init__(self):
        self.N = None
        self.R = None
        self.sequence = None
        self.allocator = None
        self.sequence_inst = None
        self.evaluator = None

    def read_input(self):
        import sys
        input_stream = sys.stdin
        self.N, self.R = map(int, input_stream.readline().split())
        elements = []
        read = 0
        while read < self.N:
            line = input_stream.readline()
            if not line:
                break
            line = line.strip()
            if line == '':
                continue
            parts = list(map(int, line.split()))
            elements.extend(parts)
            read += len(parts)
        self.sequence = elements

    def solve(self):
        self.sequence_inst = Sequence(self.sequence)
        self.allocator = ColorAllocator(self.N, self.R)
        self.evaluator = SortabilityEvaluator(self.sequence_inst, self.allocator)
        if self.evaluator.can_sort():
            print("Yes")
        else:
            print("No")

    def run(self):
        self.read_input()
        self.solve()


if __name__ == '__main__':
    SolutionFacade().run()