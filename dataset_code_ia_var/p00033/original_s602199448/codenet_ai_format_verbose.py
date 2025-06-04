class DepthFirstSearchSolver:
    def __init__(self, input_sequence):
        self.input_sequence = input_sequence
        self.solution_found = False

    def depth_first_search(self, left_group, right_group, elements_remaining):
        if len(elements_remaining) == 0:
            self.solution_found = True
            return

        current_element = elements_remaining[0]

        if current_element > max(left_group):
            self.depth_first_search(
                left_group + [current_element],
                right_group,
                elements_remaining[1:]
            )

        if current_element > max(right_group):
            self.depth_first_search(
                left_group,
                right_group + [current_element],
                elements_remaining[1:]
            )

    def execute_search(self):
        initial_left_group = [-1]
        initial_right_group = [-1]
        self.depth_first_search(initial_left_group, initial_right_group, self.input_sequence)

if __name__ == '__main__':
    number_of_test_cases = int(input())

    for test_case_index in range(number_of_test_cases):
        sequence_of_numbers = list(map(int, input().split()))

        search_solver = DepthFirstSearchSolver(sequence_of_numbers)
        search_solver.execute_search()

        if search_solver.solution_found:
            print('YES')
        else:
            print('NO')