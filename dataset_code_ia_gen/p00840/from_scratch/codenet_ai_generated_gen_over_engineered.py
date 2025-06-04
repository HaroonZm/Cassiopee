from typing import List, Tuple, Optional, Dict, FrozenSet
from abc import ABC, abstractmethod
import sys

class Mobile(ABC):
    @abstractmethod
    def total_weight(self) -> int:
        pass

    @abstractmethod
    def width(self) -> float:
        pass

class Stone(Mobile):
    def __init__(self, weight: int):
        self._weight = weight

    def total_weight(self) -> int:
        return self._weight

    def width(self) -> float:
        return 0.0

    def __repr__(self):
        return f"Stone({self._weight})"

class Rod(Mobile):
    def __init__(self, left: Mobile, right: Mobile):
        self.left = left
        self.right = right
        self._weight_left = self.left.total_weight()
        self._weight_right = self.right.total_weight()
        # distances a and b satisfy n*a = m*b and a + b = 1
        total = self._weight_left + self._weight_right
        self._dist_left = self._weight_right / total
        self._dist_right = self._weight_left / total

    def total_weight(self) -> int:
        return self._weight_left + self._weight_right

    def width(self) -> float:
        # width = a + width(left) + b + width(right)
        # The problem states width = a + width(left) + b + width(right)
        # but from sample, the width is (a + width_left + b + width_right)
        # According to the figure and problem, the width is:
        # width = a + width(left) + b + width(right)
        # but since a + b =1 (rod length)
        # width = 1 + width(left) + width(right)
        # The example suggests width is (a + width_left + b + width_right)
        # So for generality, we use a + width_left + b + width_right
        # which is: dist_left + width_left + dist_right + width_right
        return self._dist_left + self.left.width() + self._dist_right + self.right.width()

    def __repr__(self):
        return f"Rod({repr(self.left)}, {repr(self.right)})"

class MobileFactory:
    def __init__(self, stones: List[int]):
        self.stones = stones
        self._memo_width: Dict[FrozenSet[int], float] = {}
        self._memo_mobiles: Dict[FrozenSet[int], List[Mobile]] = {}

    def _set_from_list(self, stones_list: List[int]) -> FrozenSet[int]:
        return frozenset((i, self.stones[i]) for i in stones_list)

    def generate_all_mobiles_for_indices(self, indices: Tuple[int, ...]) -> List[Mobile]:
        key = frozenset(indices)
        if key in self._memo_mobiles:
            return self._memo_mobiles[key]

        if len(indices) == 1:
            stone_index = indices[0]
            stone = Stone(self.stones[stone_index])
            self._memo_mobiles[key] = [stone]
            return [stone]

        mobiles: List[Mobile] = []
        # We try all possible partitions of indices into 2 non-empty sets without duplication
        indices_list = list(indices)
        n = len(indices_list)
        # To avoid duplicates, we generate subsets with indices sorted and only left < right partition
        # We'll generate all non-empty subsets as left part except the full set or empty
        # and right part is remaining indices
        from itertools import combinations

        for lsize in range(1, n // 2 + 1):
            for left_indices in combinations(indices_list, lsize):
                left_set = frozenset(left_indices)
                right_set = key - left_set
                for left_mobile in self.generate_all_mobiles_for_indices(tuple(sorted(left_set))):
                    for right_mobile in self.generate_all_mobiles_for_indices(tuple(sorted(right_set))):
                        # Compose rod
                        rod_mobile = Rod(left_mobile, right_mobile)
                        mobiles.append(rod_mobile)
                # If n is even and lsize == n - lsize, avoid double counting swap
                if n % 2 == 0 and lsize == n // 2:
                    continue
                # For bigger-sized left subsets (beyond half), permutation handled by symmetry

        self._memo_mobiles[key] = mobiles
        return mobiles

class MobileOptimizer:
    def __init__(self, stones: List[int], room_width: float):
        self.stones = stones
        self.room_width = room_width
        self.n = len(stones)
        self.factory = MobileFactory(stones)
        self._cached_best_width: Dict[FrozenSet[int], float] = {}

    def best_width_for_subset(self, indices: Tuple[int, ...]) -> float:
        key = frozenset(indices)
        if key in self._cached_best_width:
            return self._cached_best_width[key]

        if len(indices) == 1:
            # Only stone, width = 0.0
            self._cached_best_width[key] = 0.0
            return 0.0

        best_width = -1.0
        indices_list = list(indices)
        n = len(indices_list)

        from itertools import combinations

        for lsize in range(1, n // 2 + 1):
            for left_indices in combinations(indices_list, lsize):
                left_set = frozenset(left_indices)
                right_set = key - left_set
                left_width = self.best_width_for_subset(tuple(sorted(left_set)))
                right_width = self.best_width_for_subset(tuple(sorted(right_set)))
                n_w = sum(self.stones[i] for i in left_set)
                m_w = sum(self.stones[i] for i in right_set)
                total_w = n_w + m_w
                a = m_w / total_w
                b = n_w / total_w
                candidate_width = a + left_width + b + right_width
                if candidate_width < self.room_width and candidate_width > best_width:
                    best_width = candidate_width
                # Avoid double counting for even partition size
                if n % 2 == 0 and lsize == n // 2:
                    continue

        self._cached_best_width[key] = best_width
        return best_width

def parse_input() -> List[Tuple[float, List[int]]]:
    input_lines = sys.stdin.read().strip().split('\n')
    t = int(input_lines[0])
    pos = 1
    datasets = []
    for _ in range(t):
        r = float(input_lines[pos]); pos += 1
        s = int(input_lines[pos]); pos += 1
        w = [int(input_lines[pos + i]) for i in range(s)]
        pos += s
        datasets.append((r, w))
    return datasets

def main() -> None:
    datasets = parse_input()
    for (r, stones) in datasets:
        optimizer = MobileOptimizer(stones, r)
        n = len(stones)
        best = optimizer.best_width_for_subset(tuple(range(n)))
        if best < 0:
            print(-1)
        else:
            print(f"{best:.15f}")

if __name__ == "__main__":
    main()