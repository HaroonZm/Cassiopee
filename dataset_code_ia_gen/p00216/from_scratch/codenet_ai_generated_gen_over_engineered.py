from abc import ABC, abstractmethod
from typing import List


class WaterChargeTier(ABC):
    @abstractmethod
    def applicable_volume(self, volume: int) -> int:
        pass

    @abstractmethod
    def charge_for(self, volume: int) -> int:
        pass


class Tier1(WaterChargeTier):
    def __init__(self):
        self.basic_charge = 1150
        self.max_volume = 10

    def applicable_volume(self, volume: int) -> int:
        return min(volume, self.max_volume)

    def charge_for(self, volume: int) -> int:
        # For Tier 1, charge is fixed basic charge regardless usage up to 10 m3
        if volume > 0:
            return self.basic_charge
        else:
            return 0  # no charge if no usage


class Tier2(WaterChargeTier):
    def __init__(self):
        self.unit_price = 125
        self.start = 10
        self.end = 20

    def applicable_volume(self, volume: int) -> int:
        if volume <= self.start:
            return 0
        return min(volume, self.end) - self.start

    def charge_for(self, volume: int) -> int:
        v = self.applicable_volume(volume)
        return v * self.unit_price


class Tier3(WaterChargeTier):
    def __init__(self):
        self.unit_price = 140
        self.start = 20
        self.end = 30

    def applicable_volume(self, volume: int) -> int:
        if volume <= self.start:
            return 0
        return min(volume, self.end) - self.start

    def charge_for(self, volume: int) -> int:
        v = self.applicable_volume(volume)
        return v * self.unit_price


class Tier4(WaterChargeTier):
    def __init__(self):
        self.unit_price = 160
        self.start = 30

    def applicable_volume(self, volume: int) -> int:
        if volume <= self.start:
            return 0
        return volume - self.start

    def charge_for(self, volume: int) -> int:
        v = self.applicable_volume(volume)
        return v * self.unit_price


class WaterChargeCalculator:
    def __init__(self):
        self.tiers: List[WaterChargeTier] = [Tier1(), Tier2(), Tier3(), Tier4()]
        self.last_month_charge = 4280

    def calculate(self, volume: int) -> int:
        # sum charges from all tiers
        total = 0
        # Note: Tier1 returns basic charge only if volume > 0 to avoid charging if 0 usage
        # So order matters as Tier1 fixed charge is always there if usage positive
        total += self.tiers[0].charge_for(volume)
        for tier in self.tiers[1:]:
            total += tier.charge_for(volume)
        return total

    def calculate_savings(self, volume: int) -> int:
        current_charge = self.calculate(volume)
        return self.last_month_charge - current_charge


class InputHandler:
    def __init__(self, calculator: WaterChargeCalculator):
        self.calculator = calculator

    def process(self):
        while True:
            line = input().strip()
            if line == '-1':
                break
            try:
                w = int(line)
                if not (0 <= w <= 100):
                    # per problem constraint, but skip or ignore invalid inputs
                    continue
            except ValueError:
                continue
            savings = self.calculator.calculate_savings(w)
            print(savings)


def main():
    calculator = WaterChargeCalculator()
    handler = InputHandler(calculator)
    handler.process()


if __name__ == "__main__":
    main()