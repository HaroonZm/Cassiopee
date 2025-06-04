from abc import ABC, abstractmethod
from typing import List, Tuple

class BalancedString(ABC):
    @abstractmethod
    def to_str(self) -> str:
        pass

    @abstractmethod
    def length(self) -> int:
        pass

class PrimitiveBalanced(BalancedString):
    def to_str(self) -> str:
        return "()"

    def length(self) -> int:
        return 2

class ConcatBalanced(BalancedString):
    def __init__(self, left: BalancedString, right: BalancedString):
        self.left = left
        self.right = right

    def to_str(self) -> str:
        return self.left.to_str() + self.right.to_str()

    def length(self) -> int:
        return self.left.length() + self.right.length()

class WrapBalanced(BalancedString):
    def __init__(self, inner: BalancedString):
        self.inner = inner

    def to_str(self) -> str:
        return '(' + self.inner.to_str() + ')'

    def length(self) -> int:
        return 2 + self.inner.length()

class DaveStringBuilder:
    """
    Builder class to produce the Dave's string satisfying swap cost A conditions.
    """

    def __init__(self, A: int):
        self.A = A
        self.result = ""

    def build(self) -> str:
        """
        Main builder function which computes and returns the desired string.
        """
        # For large A, we build the string according to a mathematical formula:
        # The minimum string length M and structure are derived based on the inversion count needed.
        # The string pattern used is a sequence of ')' in front and '(' at rear arranged carefully.
        # Returns the minimal lexicographical string of minimal length that requires exactly A swaps.
        n = 2
        while True:
            max_inversions = (n // 2) * (n - n // 2)  # max adjacent swaps needed to balance this length
            if max_inversions >= self.A:
                break
            n += 2

        left_count = n // 2  # '(' count
        right_count = n - left_count  # ')' count

        # We want to arrange the string of n characters with left_count '(' and right_count ')'
        # to have exactly self.A swaps needed to balance it.
        # The minimal lex string satisfying that is constructed by placing some ')' in front,
        # then some pattern to reach exact inversion self.A.
        # The core idea:
        # Let x be the number of leading ')' (inversion contribution: x * (n - x)),
        # among these x, there's an offset y to adjust to exactly A swaps.

        for x in range(right_count + 1):
            max_for_x = x * (n - x)
            if max_for_x >= self.A:
                y = max_for_x - self.A
                # lex minimum: ')' * x + '(' * (left_count - y) + ')' * (right_count - x) + '(' * y
                res = ')'*x + '('*(left_count - y) + ')'*(right_count - x) + '('*y
                self.result = res
                break

        return self.result


def main():
    import sys
    A = int(sys.stdin.readline())
    builder = DaveStringBuilder(A)
    print(builder.build())

if __name__ == "__main__":
    main()