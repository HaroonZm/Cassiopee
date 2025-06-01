class Interval:
    def __init__(self, base_value: int):
        self.base_value = base_value
        self.adjusted_value = base_value
        self.increment = 0

    def adjust_to_multiple(self, target):
        if target < self.base_value:
            raise ValueError("Target interval cannot be less than base interval")
        self.increment = target - self.base_value
        self.adjusted_value = target

    def __repr__(self):
        return f"Interval(base={self.base_value}, adjusted={self.adjusted_value}, increment={self.increment})"


class IntervalSet:
    def __init__(self, intervals):
        self.intervals = [Interval(val) for val in intervals]

    def total_increment(self):
        return sum(interval.increment for interval in self.intervals)

    def max_base(self):
        return max(interval.base_value for interval in self.intervals)

    def find_minimum_sum_of_increments(self):
        max_base = self.max_base()
        max_search_limit = max_base * 2  # arbitrary upper bound for search in worst case

        best_total_increment = None
        best_target = None

        for candidate in range(max_base, max_search_limit + 1):
            # Check if candidate can be LCM after increments (candidate must be multiple of all adjusted intervals)
            total_inc = 0
            feasible = True
            for interval in self.intervals:
                if candidate < interval.base_value:
                    feasible = False
                    break
                remainder = candidate % interval.base_value
                increment = (interval.base_value - remainder) if remainder != 0 else 0
                # candidate must be divisible by adjusted interval = base + increment
                adjusted = interval.base_value + increment
                if candidate % adjusted != 0:
                    feasible = False
                    break
                total_inc += increment
                if best_total_increment is not None and total_inc > best_total_increment:
                    # Early stop if already worse
                    feasible = False
                    break
            if feasible:
                if best_total_increment is None or total_inc < best_total_increment:
                    best_total_increment = total_inc
                    best_target = candidate
                if best_total_increment == 0:
                    break  # can't do better than zero

        # now adjust intervals according to found target
        for interval in self.intervals:
            adjusted_val = (best_target // interval.base_value) * interval.base_value
            if adjusted_val < interval.base_value:
                adjusted_val = interval.base_value
            # find minimal multiple of base_value >= best_target
            multiplier = (best_target + interval.base_value - 1) // interval.base_value
            interval.adjust_to_multiple(multiplier * interval.base_value)

        return best_total_increment


class Solution:
    def __init__(self):
        self.interval_set = None

    def read_input(self):
        n = int(input().strip())
        intervals = [int(input().strip()) for _ in range(n)]
        self.interval_set = IntervalSet(intervals)

    def solve(self):
        result = self.interval_set.find_minimum_sum_of_increments()
        print(result)

if __name__ == "__main__":
    solution = Solution()
    solution.read_input()
    solution.solve()