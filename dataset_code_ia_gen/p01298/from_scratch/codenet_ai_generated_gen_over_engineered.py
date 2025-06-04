from abc import ABC, abstractmethod
from typing import List, Tuple, Iterator
import sys

class Schedule:
    """Represents a single water usage schedule."""
    def __init__(self, start: int, end: int, usage_rate: int) -> None:
        self.start = start
        self.end = end
        self.usage_rate = usage_rate
        self.duration = end - start
        self.total_usage = self.duration * self.usage_rate

class ScheduleTable:
    """Holds multiple schedules representing one day's water consumption pattern."""
    DAY_DURATION = 86400

    def __init__(self, schedules: List[Schedule], tank_capacity: int) -> None:
        self.schedules = schedules
        self.tank_capacity = tank_capacity

    def intervals(self) -> Iterator[Tuple[int, int, int]]:
        """Generate tuples of (start_time, end_time, net_usage_rate) for all continuous intervals including idle times.
        The usage_rate is positive for consumption."""
        pos = 0
        for sched in self.schedules:
            if pos < sched.start:
                # Idle interval, usage rate 0
                yield (pos, sched.start, 0)
            yield (sched.start, sched.end, sched.usage_rate)
            pos = sched.end
        if pos < self.DAY_DURATION:
            # Tail idle interval
            yield (pos, self.DAY_DURATION, 0)

class ConsumptionModel(ABC):
    @abstractmethod
    def minimal_pump_rate(self, schedule_table: ScheduleTable) -> float:
        """Calculates minimal pump flow needed."""
        pass

class TankConsumptionModel(ConsumptionModel):
    """Simulate the tank water level evolution to find minimal pump speed."""

    def minimal_pump_rate(self, schedule_table: ScheduleTable) -> float:
        L = schedule_table.tank_capacity
        intervals = list(schedule_table.intervals())

        # Lower and upper bounds for binary search of pump speed:
        # Lower bound cannot be less than 0
        # Upper bound could be max usage rate in the schedules or more
        max_usage = max((interval[2] for interval in intervals), default=0)
        low, high = 0.0, max_usage

        def check(pump_rate: float) -> bool:
            # Returns True if pump_rate keeps tank never empty during the day
            tank_level = L
            for start, end, rate in intervals:
                length = end - start
                net_rate = pump_rate - rate
                tank_level += net_rate * length
                if tank_level < 0:
                    return False
                # Cap water to max tank capacity (overflow ignored, but no point going above)
                if tank_level > L:
                    tank_level = L
            return True

        # We want minimal pump_rate with error tolerance of 1e-7 to ensure output precision better than 1e-6
        for _ in range(60):  # about 60 iterations good for double precision binary search
            mid = (low + high) / 2
            if check(mid):
                high = mid
            else:
                low = mid
        return high

class InputParser:
    """Parses multiple datasets from stdin for ScheduleTable(s)."""

    @staticmethod
    def parse() -> Iterator[ScheduleTable]:
        lines = sys.stdin
        while True:
            line = ''
            while line.strip() == '':
                line = next(lines).strip()
            if line == '0 0':
                break
            N_str, L_str = line.split()
            N, L = int(N_str), int(L_str)
            schedules = []
            for _ in range(N):
                s, t, u = map(int, next(lines).strip().split())
                schedules.append(Schedule(s, t, u))
            yield ScheduleTable(schedules, L)

class OutputFormatter:
    """Formats output to required precision."""

    @staticmethod
    def format_pump_rate(rate: float) -> str:
        return f"{rate:.6f}"

def main():
    parser = InputParser()
    model = TankConsumptionModel()
    for schedule_table in parser.parse():
        answer = model.minimal_pump_rate(schedule_table)
        print(OutputFormatter.format_pump_rate(answer))

if __name__ == "__main__":
    main()