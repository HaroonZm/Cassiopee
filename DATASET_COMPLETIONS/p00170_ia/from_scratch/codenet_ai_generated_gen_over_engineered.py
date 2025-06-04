from typing import List, Tuple
from abc import ABC, abstractmethod
from functools import lru_cache


class FoodItem:
    def __init__(self, name: str, weight: int, strength: int) -> None:
        self.name = name
        self.weight = weight
        self.strength = strength

    def __repr__(self) -> str:
        return f"FoodItem({self.name}, w={self.weight}, s={self.strength})"


class StackArrangement(ABC):
    """抽象基底クラス: 食べ物の積み方を表す"""

    @abstractmethod
    def total_weight(self) -> int:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def weighted_positions(self) -> int:
        pass

    @abstractmethod
    def items_order(self) -> List[FoodItem]:
        pass


class FoodStack(StackArrangement):
    def __init__(self, items: List[FoodItem]) -> None:
        self._items = items

    def total_weight(self) -> int:
        return sum(item.weight for item in self._items)

    def is_valid(self) -> bool:
        # 底から順に積み重ねて条件s_i >= sum_(above) w_jを満たすか調べる
        suffix_sum = 0
        for item in reversed(self._items):
            if item.strength < suffix_sum:
                return False
            suffix_sum += item.weight
        return True

    def weighted_positions(self) -> int:
        # 重心計算の分子部分 Σ(i×w_i)
        return sum((i+1)*item.weight for i, item in enumerate(self._items))

    def items_order(self) -> List[FoodItem]:
        return self._items


class StackSolver:
    def __init__(self, foods: List[FoodItem]) -> None:
        self.foods = foods

    def solve(self) -> FoodStack:
        # 解は一意、かつnは最大10なので全探索で解く。
        # validな積み方の中で重心が最も低い (weighted_positions / total_weight 最小) を探す。

        best_stack: FoodStack = None
        best_score: float = float("inf")

        @lru_cache(maxsize=None)
        def can_stack(order: Tuple[int, ...]) -> bool:
            suffix = 0
            for idx in reversed(order):
                f = self.foods[idx]
                if f.strength < suffix:
                    return False
                suffix += f.weight
            return True

        from itertools import permutations

        n = len(self.foods)
        for order in permutations(range(n)):
            if can_stack(order):
                total_w = sum(self.foods[i].weight for i in order)
                weighted_pos = sum((i+1)*self.foods[idx].weight for i, idx in enumerate(order))
                center_of_gravity = weighted_pos / total_w
                if center_of_gravity < best_score:
                    best_score = center_of_gravity
                    best_stack = FoodStack([self.foods[i] for i in order])

        return best_stack


class InputParser:
    def __init__(self):
        pass

    def parse(self) -> List[List[FoodItem]]:
        datasets: List[List[FoodItem]] = []
        while True:
            n_line = input().strip()
            if n_line == "0":
                break
            n = int(n_line)
            items: List[FoodItem] = []
            for _ in range(n):
                line = input().strip()
                name, w_str, s_str = line.split()
                items.append(FoodItem(name, int(w_str), int(s_str)))
            datasets.append(items)
        return datasets


class OutputFormatter:
    def __init__(self):
        pass

    def format_stack(self, stack: FoodStack) -> List[str]:
        # 下から積み上げる順に食べ物名を返す
        return [item.name for item in stack.items_order()]


class LunchOrganizerFacade:
    def __init__(self):
        self.parser = InputParser()
        self.formatter = OutputFormatter()

    def run(self):
        datasets = self.parser.parse()
        for foods in datasets:
            solver = StackSolver(foods)
            solution = solver.solve()
            answers = self.formatter.format_stack(solution)
            print("\n".join(answers))


if __name__ == "__main__":
    organizer = LunchOrganizerFacade()
    organizer.run()