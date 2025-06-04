from functools import total_ordering
from typing import List, Callable

class PowerTower:
    """
    Represents a power tower expression a1^(a2^(... (an)...))
    where evaluation is right-associative.
    """

    def __init__(self, bases: List[int]):
        self.bases = bases

    def evaluate(self) -> float:
        """
        Evaluate the tower height using floating approximations, mainly for possible future use.
        This won't be the comparator logic but can be used to debug or approximate.
        """
        return self._eval_recursive(0)

    def _eval_recursive(self, idx: int) -> float:
        if idx == len(self.bases) - 1:
            return float(self.bases[idx])
        base = float(self.bases[idx])
        exponent = self._eval_recursive(idx + 1)
        # 0^0 = 1 as per the problem statement
        if base == 0 and exponent == 0:
            return 1.0
        # To avoid math domain errors or float overflow, use log
        if base == 0:
            return 0.0
        # Cap too large exponents for float pow
        if exponent > 1e9:
            exponent = 1e9
        return base ** exponent

@total_ordering
class PowerTowerComparator:
    """
    Wraps bases list and enables comparisons based on the problem's criteria:
    Compare towers from left to right with power tower rules.
    """

    def __init__(self, bases: List[int]):
        self.bases = bases

    def __eq__(self, other: 'PowerTowerComparator') -> bool:
        return self.bases == other.bases

    def __lt__(self, other: 'PowerTowerComparator') -> bool:
        return self._compare(self.bases, other.bases) < 0

    @staticmethod
    def _compare(a: List[int], b: List[int]) -> int:
        """
        Compares two power tower lists a and b according to the problem's logic:
        - Calculate which tower results in a greater number.
        - If equal, lex order decides.
        This comparison is done recursively and uses special rules:
        Since direct power tower evaluation is infeasible for large exponents,
        we implement a custom comparison behavior.

        Returns:
            -1 if a < b
             0 if a == b
             1 if a > b
        """

        n = len(a)
        for i in range(n):
            if a[i] == b[i]:
                continue

            # base cases for comparing single elements:
            # - if towers shrink to one element, compare directly
            if i == n - 1:
                if a[i] < b[i]:
                    return -1
                elif a[i] > b[i]:
                    return 1
                else:
                    continue

            # Use recursive logic to compare a[i]^(rest_a) and b[i]^(rest_b)

            rest_a = a[i+1:]
            rest_b = b[i+1:]

            r = PowerTowerComparator._comparePower(a[i], rest_a, b[i], rest_b)
            if r != 0:
                return r

        return 0

    @staticmethod
    def _comparePower(base1: int, exp_list1: List[int], base2: int, exp_list2: List[int]) -> int:
        """
        Compare base1^(exp1) and base2^(exp2) where exp1 and exp2 are power towers defined by exp_list1 and exp_list2.
        Uses special rules and approximations:
        - 0^0 = 1 by problem statement
        - If both bases and exponents equal, towers are equal.
        - Uses heuristic and logarithmic comparisons to avoid overflow.
        """

        # Evaluate exponents ends:
        # If exponent empty, exponent is considered 1 by tower definition

        if len(exp_list1) == 0:
            exp1 = 1
        else:
            # Compare exponent towers recursively
            exp1 = PowerTower(exp_list1).evaluate()

        if len(exp_list2) == 0:
            exp2 = 1
        else:
            exp2 = PowerTower(exp_list2).evaluate()

        # Handle the 0^0 case as 1
        def val(base, exp):
            if base == 0 and exp == 0:
                return 1.0
            try:
                # For large exponents, use logs to compare size instead of numbers
                if base == 0:
                    return 0.0
                if exp > 1e9:
                    exp = 1e9
                return base ** exp
            except OverflowError:
                return float('inf')

        # Because direct calculation is impossible for large:
        # Instead, compare using logarithm rules: val1 = base1^exp1 > val2 = base2^exp2
        #
        # log(val1) = exp1 * log(base1)
        # log(val2) = exp2 * log(base2)
        #
        # Compare log(val1) and log(val2) carefully considering bases might be 0.

        import math

        # Handle 0^exp cases:
        if base1 == 0 and exp1 == 0:
            val1_ln = 0.0
        elif base1 == 0:
            val1_ln = float('-inf')
        else:
            try:
                val1_ln = exp1 * math.log(base1)
            except ValueError:
                # log(0) impossible, but handled above
                val1_ln = float('-inf')

        if base2 == 0 and exp2 == 0:
            val2_ln = 0.0
        elif base2 == 0:
            val2_ln = float('-inf')
        else:
            try:
                val2_ln = exp2 * math.log(base2)
            except ValueError:
                val2_ln = float('-inf')

        if abs(val1_ln - val2_ln) < 1e-12:
            # Almost equal, fallback to lex order on bases and exponents lists
            if base1 < base2:
                return -1
            elif base1 > base2:
                return 1
            else:
                # rec compare exponent towers lex order
                if exp_list1 < exp_list2:
                    return -1
                elif exp_list1 > exp_list2:
                    return 1
                else:
                    return 0

        if val1_ln > val2_ln:
            return 1
        else:
            return -1


class TowerSorter:
    """
    A class responsible for sorting arrays of integers into sequences that maximize the power tower result,
    following the problem rules and tie-breakers.
    """

    def __init__(self, array: List[int]):
        self.array = array

    def get_max_tower_sequence(self) -> List[int]:
        """
        Returns the rearranged list that yields the maximal right-associative power tower,
        with tie-breaking on lexicographical order.
        """

        # We cannot simply sort by value or naive comparator.
        # Instead, apply a custom comparator implementing the PowerTowerComparator.

        # We'll generate all permutations is impossible (N up to 100)
        # Instead: Sort using PowerTowerComparator based comparator with functools.cmp_to_key

        from functools import cmp_to_key

        def cmp_func(x, y):
            comp = PowerTowerComparator._compare([x], [y])
            # _compare returns -1 if x < y but we want descending order (max tower first)
            return -comp

        # Sort using cmp_func then resolve ties lex order in resulting sequence per problem statement
        # Actually, the problem says that among maximal sequences tie in tower value, pick lex smallest sequence.
        # Sorting ascending by cmp_func implements sorting descending by tower value, so lex order is automatically preserved in stable sort.

        sorted_arr = sorted(self.array, key=cmp_to_key(cmp_func))

        # For possible duplicates creating same power tower value,
        # we might want to verify if this sorted sequence is lex minimal maximal solution.
        # The sorting method picks one maximal solution with lex smallest due to stable sort.

        return sorted_arr


def main():
    import sys
    sys.setrecursionlimit(10**7)

    input = sys.stdin.readline
    N = int(input())
    A = [int(input()) for _ in range(N)]

    sorter = TowerSorter(A)
    ans = sorter.get_max_tower_sequence()

    for v in ans:
        print(v)

if __name__ == "__main__":
    main()