class VisitorInterval:
    def __init__(self, arrival_time: int):
        self.start = arrival_time
        self.end = arrival_time + 1

    def length(self) -> int:
        return self.end - self.start

class HeatingSchedule:
    def __init__(self, intervals):
        self.intervals = intervals
        self.gaps = self._calculate_gaps()
    
    def _calculate_gaps(self):
        gaps = []
        for i in range(len(self.intervals) - 1):
            gap = self.intervals[i + 1].start - self.intervals[i].end
            gaps.append(gap)
        return gaps
    
    def initial_heating_time(self) -> int:
        return self.intervals[-1].end - self.intervals[0].start
    
    def minimize_heating_time(self, max_ignitions: int) -> int:
        # We want to turn the stove on at most max_ignitions times
        # Initially, consider keeping stove on for all intervals contiguously:
        total_time = self.initial_heating_time()

        # Sort gaps descending to pick largest gaps to NOT heat (to save time)
        # Since reducing the number of ignitions by merging intervals means skipping heating during some gaps
        sorted_gaps = sorted(self.gaps, reverse=True)

        # We can skip heating during (max_ignitions - 1) largest gaps to minimize total heating time
        gaps_to_skip = max_ignitions - 1
        for i in range(gaps_to_skip):
            if i < len(sorted_gaps):
                total_time -= sorted_gaps[i]

        return total_time

class StoveController:
    def __init__(self, n_visitors: int, max_matches: int, arrival_times: list):
        self.n_visitors = n_visitors
        self.max_matches = max_matches
        self.arrival_times = arrival_times
        self.visitor_intervals = self._create_intervals()

    def _create_intervals(self):
        return [VisitorInterval(t) for t in self.arrival_times]

    def compute_minimum_heating_time(self) -> int:
        heating_schedule = HeatingSchedule(self.visitor_intervals)
        return heating_schedule.minimize_heating_time(self.max_matches)

class InputParser:
    @staticmethod
    def parse_input():
        n, k = map(int, input().split())
        arrival_times = [int(input().strip()) for _ in range(n)]
        return n, k, arrival_times

def main():
    n, k, arrival_times = InputParser.parse_input()
    stove_controller = StoveController(n, k, arrival_times)
    result = stove_controller.compute_minimum_heating_time()
    print(result)

if __name__ == "__main__":
    main()