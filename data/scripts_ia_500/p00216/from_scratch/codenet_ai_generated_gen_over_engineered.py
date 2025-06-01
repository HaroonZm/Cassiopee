from abc import ABC, abstractmethod
from typing import List, Optional


class WaterRateTier(ABC):
    @abstractmethod
    def calculate_charge(self, usage: int) -> int:
        pass


class BaseChargeTier(WaterRateTier):
    def __init__(self, base_fee: int, limit: int):
        self.base_fee = base_fee
        self.limit = limit

    def calculate_charge(self, usage: int) -> int:
        # Base charge applies regardless of usage, up to limit
        return self.base_fee if usage > 0 else 0


class UsageChargeTier(WaterRateTier):
    def __init__(self, lower_limit: int, upper_limit: Optional[int], rate_per_m3: int):
        self.lower_limit = lower_limit  # exclusive lower bound
        self.upper_limit = upper_limit  # inclusive upper bound or None
        self.rate_per_m3 = rate_per_m3

    def calculate_charge(self, usage: int) -> int:
        if usage <= self.lower_limit:
            return 0
        upper = self.upper_limit if self.upper_limit is not None else usage
        applicable_volume = min(usage, upper) - self.lower_limit
        if applicable_volume < 0:
            return 0
        return applicable_volume * self.rate_per_m3


class WaterFeeCalculator:
    def __init__(self, tiers: List[WaterRateTier]):
        self.tiers = tiers

    def calculate(self, usage: int) -> int:
        total = 0
        for tier in self.tiers:
            total += tier.calculate_charge(usage)
        return total


class WaterUsageDataset:
    def __init__(self, last_month_fee: int):
        self.last_month_fee = last_month_fee
        self.calculator = WaterFeeCalculator([
            BaseChargeTier(base_fee=1150, limit=10),
            UsageChargeTier(lower_limit=10, upper_limit=20, rate_per_m3=125),
            UsageChargeTier(lower_limit=20, upper_limit=30, rate_per_m3=140),
            UsageChargeTier(lower_limit=30, upper_limit=None, rate_per_m3=160),
        ])

    def calculate_savings(self, this_month_usage: int) -> int:
        current_fee = self.calculator.calculate(this_month_usage)
        return self.last_month_fee - current_fee


class WaterUsageProcessor:
    def __init__(self, last_month_fee: int):
        self.dataset = WaterUsageDataset(last_month_fee=last_month_fee)

    def process_usages(self, usages: List[int]) -> List[int]:
        results = []
        for usage in usages:
            savings = self.dataset.calculate_savings(usage)
            results.append(savings)
        return results


def main():
    import sys

    last_month_fee = 4280
    processor = WaterUsageProcessor(last_month_fee)

    usages = []
    for line in sys.stdin:
        line = line.strip()
        if line == '-1':
            break
        if line.isdigit():
            w = int(line)
            usages.append(w)

    results = processor.process_usages(usages)
    for res in results:
        print(res)


if __name__ == "__main__":
    main()