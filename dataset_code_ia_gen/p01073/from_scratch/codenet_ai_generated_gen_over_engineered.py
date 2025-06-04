from typing import List, Tuple, Iterable
from itertools import combinations
import abc


class PotatoFieldInterface(abc.ABC):
    @abc.abstractmethod
    def max_plantable(self) -> int:
        pass

    @abc.abstractmethod
    def yield_per_potato(self) -> int:
        pass


class PotatoField(PotatoFieldInterface):
    def __init__(self, yield_per_potato: int, max_plantable: int):
        self._yield_per_potato = yield_per_potato
        self._max_plantable = max_plantable

    def max_plantable(self) -> int:
        return self._max_plantable

    def yield_per_potato(self) -> int:
        return self._yield_per_potato


class PlantingStrategyInterface(abc.ABC):
    @abc.abstractmethod
    def optimal_plant_distribution(self, fields: List[PotatoFieldInterface], max_fields: int, max_potatoes: int) -> int:
        pass


class ExhaustivePlantingStrategy(PlantingStrategyInterface):
    def optimal_plant_distribution(self, fields: List[PotatoFieldInterface], max_fields: int, max_potatoes: int) -> int:
        max_yield = 0
        n = len(fields)

        # Enumerate all subsets of fields of size at most max_fields
        for r in range(1, max_fields + 1):
            for subset_indices in combinations(range(n), r):
                subset_fields = [fields[i] for i in subset_indices]
                # Dynamic programming to allocate potatoes optimally across these fields
                # dp[i][p] = max yield using first i fields with p potatoes planted
                dp = [[-1] * (max_potatoes + 1) for _ in range(len(subset_fields) + 1)]
                dp[0][0] = 0

                for i, field in enumerate(subset_fields, start=1):
                    yield_per_p = field.yield_per_potato()
                    max_plant = field.max_plantable()
                    for p in range(max_potatoes + 1):
                        if dp[i - 1][p] < 0:
                            continue
                        # For each possible planting count in this field
                        max_plant_here = min(max_plant, max_potatoes - p)
                        for plant_count in range(max_plant_here + 1):
                            new_p = p + plant_count
                            new_yield = dp[i - 1][p] + plant_count * yield_per_p
                            if dp[i][new_p] < new_yield:
                                dp[i][new_p] = new_yield
                max_yield_subset = max(dp[len(subset_fields)])
                if max_yield < max_yield_subset:
                    max_yield = max_yield_subset

        return max_yield


class PotatoFarm:
    def __init__(self, fields: List[PotatoFieldInterface], max_manageable_fields: int, max_total_potatoes: int,
                 strategy: PlantingStrategyInterface):
        self.fields = fields
        self.max_manageable_fields = max_manageable_fields
        self.max_total_potatoes = max_total_potatoes
        self.strategy = strategy

    def maximize_harvest(self) -> int:
        return self.strategy.optimal_plant_distribution(self.fields, self.max_manageable_fields, self.max_total_potatoes)


class InputParser:
    @staticmethod
    def parse_input() -> Tuple[int, int, int, List[int], List[int]]:
        # Read integers
        N, M, K = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        return N, M, K, a, b


def main():
    N, M, K, a_list, b_list = InputParser.parse_input()
    fields = [PotatoField(a, b) for a, b in zip(a_list, b_list)]
    strategy = ExhaustivePlantingStrategy()
    farm = PotatoFarm(fields, K, M, strategy)
    max_harvest = farm.maximize_harvest()
    print(max_harvest)


if __name__ == '__main__':
    main()