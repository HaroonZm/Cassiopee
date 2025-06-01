from typing import List, Tuple, Optional
from itertools import permutations, product
import operator

class Expression:
    def __init__(self, value: int, expr_str: str, depth: int, parentheses: int):
        self.value = value            # Computed integer value of the expression
        self.expr_str = expr_str      # String representation of the expression
        self.depth = depth            # Depth of expression tree (not strictly necessary here but useful for extensions)
        self.parentheses = parentheses  # Number of pairs of parentheses used

    def __str__(self):
        return self.expr_str

class Operator:
    ADD = ('+', operator.add)
    SUB = ('-', operator.sub)
    MUL = ('*', operator.mul)

    @staticmethod
    def all_ops():
        return [Operator.ADD, Operator.SUB, Operator.MUL]

class ExpressionBuilder:
    MAX_PARENS = 3
    TARGET = 10
    MAX_LENGTH = 1024

    def __init__(self, numbers: List[int]):
        self.numbers = numbers
        self.memo = {}

    def build_all_expressions(self, nums: Tuple[int, ...]) -> List[Expression]:
        """
        Recursively build all expressions from the tuple of numbers
        """
        if nums in self.memo:
            return self.memo[nums]

        # Base case: single number
        if len(nums) == 1:
            expr = Expression(nums[0], str(nums[0]), 1, 0)
            self.memo[nums] = [expr]
            return [expr]

        results = []
        for i in range(1, len(nums)):
            left_parts = self.build_all_expressions(nums[:i])
            right_parts = self.build_all_expressions(nums[i:])
            # Combine each left and right expression with each operator
            for left_expr in left_parts:
                for right_expr in right_parts:
                    for op_sym, op_func in Operator.all_ops():
                        try:
                            val = op_func(left_expr.value, right_expr.value)
                        except Exception:
                            continue
                        if not isinstance(val, int):
                            # Skip non-integer result, but in this context no floats due to no division
                            continue
                        # Count parentheses pairs used if adding parentheses here
                        parens_used = left_expr.parentheses + right_expr.parentheses + 1
                        if parens_used > self.MAX_PARENS:
                            continue
                        # Create string with parentheses carefully
                        # Add parentheses around combined expr always to control evaluation order
                        expr_str = "({} {} {})".format(left_expr.expr_str, op_sym, right_expr.expr_str)
                        if len(expr_str) > self.MAX_LENGTH:
                            continue
                        expr = Expression(val, expr_str, max(left_expr.depth, right_expr.depth) + 1, parens_used)
                        results.append(expr)

        self.memo[nums] = results
        return results

    def find_expression_for_target(self) -> Optional[Expression]:
        # Try all permutations of the numbers
        for perm in permutations(self.numbers):
            all_exprs = self.build_all_expressions(perm)
            for expr in all_exprs:
                if expr.value == self.TARGET:
                    # Return the first expression found that evaluates to target
                    return expr
        return None


class InputProcessor:
    def __init__(self):
        self.datasets = []

    def parse_input(self, raw_inputs: List[str]) -> None:
        """
        Parses the raw input lines into datasets of four integers until 0 0 0 0 appears
        """
        for line in raw_inputs:
            parts = line.strip().split()
            if len(parts) != 4:
                continue
            a, b, c, d = map(int, parts)
            if a == b == c == d == 0:
                break
            self.datasets.append([a, b, c, d])


def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    processor = InputProcessor()
    processor.parse_input(input_lines)
    for numbers in processor.datasets:
        builder = ExpressionBuilder(numbers)
        expr = builder.find_expression_for_target()
        if expr is None:
            print(0)
        else:
            print(expr.expr_str)

if __name__ == "__main__":
    main()