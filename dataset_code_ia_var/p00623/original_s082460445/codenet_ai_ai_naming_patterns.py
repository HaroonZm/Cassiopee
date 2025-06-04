class LogicalTreeNode:
    def __init__(self):
        self.child_left = [0]
        self.child_right = [0]
    def build_left(self, expr, inputs_list):
        depth = 0
        for idx in range(len(expr)):
            char = expr[idx]
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            elif depth == 0 and char.isdigit():
                self.child_left = [inputs_list[int(char) - 1]]
            elif char == ' ' and depth == 1:
                left_subtree = LogicalTreeNode()
                left_expr = expr[1:idx]
                right_expr = expr[idx+1:len(expr)-1]
                left_subtree.build_left(left_expr, inputs_list)
                left_subtree.build_right(right_expr, inputs_list)
                self.child_left = left_subtree
    def build_right(self, expr, inputs_list):
        depth = 0
        for idx in range(len(expr)):
            char = expr[idx]
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            elif depth == 0 and char.isdigit():
                self.child_right = [inputs_list[int(char) - 1]]
            elif char == ' ' and depth == 1:
                right_subtree = LogicalTreeNode()
                left_expr = expr[1:idx]
                right_expr = expr[idx+1:len(expr)-1]
                right_subtree.build_left(left_expr, inputs_list)
                right_subtree.build_right(right_expr, inputs_list)
                self.child_right = right_subtree
    def compute_possibilities(self):
        results_left = self.child_left
        results_right = self.child_right
        if isinstance(self.child_left, LogicalTreeNode):
            results_left = self.child_left.compute_possibilities()
        if isinstance(self.child_right, LogicalTreeNode):
            results_right = self.child_right.compute_possibilities()
        return [l & r for l in results_left for r in results_right] + \
               [l | r for l in results_left for r in results_right] + \
               [l ^ r for l in results_left for r in results_right]

while True:
    expr_input = raw_input()
    if expr_input == 'END':
        break
    input_count = int(raw_input())
    binary_values_list = []
    for index in range(input_count):
        binary_value = int(''.join(raw_input().split()), 2)
        binary_values_list.append(binary_value)
    operation_depth = 0
    tree_root = LogicalTreeNode()
    for idx in range(len(expr_input)):
        char = expr_input[idx]
        if char == '(':
            operation_depth += 1
        elif char == ')':
            operation_depth -= 1
        elif char == ' ' and operation_depth == 1:
            left_expr = expr_input[1:idx]
            right_expr = expr_input[idx+1:len(expr_input)-1]
            tree_root.build_left(left_expr, binary_values_list)
            tree_root.build_right(right_expr, binary_values_list)
    result_possibilities = tree_root.compute_possibilities()
    number_of_target_results = result_possibilities.count(15)
    print number_of_target_results