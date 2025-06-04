import sys
from abc import ABC, abstractmethod
from typing import List, Tuple


class Cylinder:
    def __init__(self, base_area: float, height: float):
        self.base_area = base_area
        self.height = height

    def volume(self) -> float:
        return self.base_area * self.height


class Pot(ABC):
    @abstractmethod
    def max_height(self) -> float:
        pass

    @abstractmethod
    def volume_up_to_height(self, h: float) -> float:
        pass

    @abstractmethod
    def height_for_volume(self, v: float) -> float:
        pass


class CylindricalPot(Pot):
    def __init__(self, cylinders: List[Cylinder]):
        self.cylinders = cylinders
        self.prefix_heights = []
        self.prefix_volumes = []
        self.total_height = 0.0
        self.total_volume = 0.0
        self._precompute()

    def _precompute(self):
        # Precompute prefix sums of heights and volumes for O(log K) queries
        accum_h = 0.0
        accum_v = 0.0
        self.prefix_heights.append(accum_h)
        self.prefix_volumes.append(accum_v)
        for c in self.cylinders:
            accum_h += c.height
            accum_v += c.volume()
            self.prefix_heights.append(accum_h)
            self.prefix_volumes.append(accum_v)
        self.total_height = accum_h
        self.total_volume = accum_v

    def max_height(self) -> float:
        return self.total_height

    def volume_up_to_height(self, h: float) -> float:
        # Compute volume occupied when water level is at height h
        # Find the last cylinder index fully filled or partly filled by h
        if h >= self.total_height:
            return self.total_volume
        # Binary search over prefix_heights to find cylinder index
        left, right = 0, len(self.prefix_heights) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_heights[mid] <= h:
                left = mid + 1
            else:
                right = mid
        idx = left - 1
        # Volume = sum of fully filled cylinders + partial volume of next cylinder
        volume = self.prefix_volumes[idx]
        partial_height = h - self.prefix_heights[idx]
        volume += self.cylinders[idx].base_area * partial_height
        return volume

    def height_for_volume(self, v: float) -> float:
        # Compute water height level when volume v is poured into this pot
        if v >= self.total_volume:
            return self.total_height
        # Binary search to find the cylinder where v is lying
        left, right = 0, len(self.prefix_volumes) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_volumes[mid] <= v:
                left = mid + 1
            else:
                right = mid
        idx = left - 1
        remaining_volume = v - self.prefix_volumes[idx]
        height_in_cylinder = remaining_volume / self.cylinders[idx].base_area
        return self.prefix_heights[idx] + height_in_cylinder


class WaterDistributor:
    def __init__(self, pots: List[Pot], total_volume: float):
        self.pots = pots
        self.M = total_volume

    def _total_water_volume_for_height(self, h: float) -> float:
        # sum of volume required to raise all pots to height h (capped by pot max height)
        total = 0.0
        for pot in self.pots:
            h_in_pot = min(h, pot.max_height())
            total += pot.volume_up_to_height(h_in_pot)
        return total

    def maximize_sum_of_heights(self) -> float:
        # We want max sum of water heights across pots given total volume M
        # The sum of heights is sum of min(h, max_height_i)
        # We use binary search on candidate height h to find max sum of heights s.t total volume ≤ M

        # maximum possible height is max of pot max_height (upper bound)
        max_possible_height = max(pot.max_height() for pot in self.pots)

        low, high = 0.0, max_possible_height
        for _ in range(100):  # enough iterations for 1e-7 precision or better
            mid = (low + high) / 2
            volume_needed = self._total_water_volume_for_height(mid)
            if volume_needed <= self.M:
                low = mid
            else:
                high = mid

        # low is the maximum fill height level
        # sum of min(h, max_height_i) is sum over pots of min(low, max_height_i)
        sum_heights = sum(min(low, pot.max_height()) for pot in self.pots)
        return sum_heights


def parse_input() -> Tuple[int, float, List[Pot]]:
    input = sys.stdin.read().strip().split()
    N = int(input[0])
    M = float(input[1])
    idx = 2
    pots = []
    for _ in range(N):
        K = int(input[idx])
        idx += 1
        cylinders = []
        for __ in range(K):
            S = float(input[idx])
            H = float(input[idx + 1])
            idx += 2
            cylinders.append(Cylinder(S, H))
        pot = CylindricalPot(cylinders)
        pots.append(pot)
    return N, M, pots


def main():
    N, M, pots = parse_input()
    distributor = WaterDistributor(pots, M)
    ans = distributor.maximize_sum_of_heights()
    print(f"{ans:.8f}")


if __name__ == "__main__":
    main()