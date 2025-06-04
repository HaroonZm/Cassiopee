class Fence:
    def __init__(self, width: int):
        self.width = width
        self.occupied_spaces = IntervalManager(width)

    def try_sleep(self, cat_id: int, cat_width: int) -> int | None:
        position = self.occupied_spaces.find_gap(cat_width)
        if position is not None:
            self.occupied_spaces.occupy(position, position + cat_width, cat_id)
        return position

    def wake_up(self, cat_id: int):
        self.occupied_spaces.release_cat(cat_id)

class IntervalManager:
    def __init__(self, width: int):
        self.width = width
        self.intervals: list[Interval] = []  # list of occupied intervals sorted by start

    def find_gap(self, required_width: int) -> int | None:
        if not self.intervals:
            if required_width <= self.width:
                return 0
            return None

        # check before first interval
        if self.intervals[0].start >= required_width:
            return 0

        # check gaps between intervals
        for i in range(len(self.intervals) - 1):
            gap_start = self.intervals[i].end
            gap_end = self.intervals[i + 1].start
            gap_size = gap_end - gap_start
            if gap_size >= required_width:
                return gap_start

        # check after last interval
        last_end = self.intervals[-1].end
        if self.width - last_end >= required_width:
            return last_end

        return None

    def occupy(self, start: int, end: int, cat_id: int):
        new_interval = Interval(start, end, cat_id)
        # insert keeping sorted order by start
        import bisect
        positions = [iv.start for iv in self.intervals]
        pos = bisect.bisect_left(positions, new_interval.start)
        self.intervals.insert(pos, new_interval)

    def release_cat(self, cat_id: int):
        # remove interval with that cat_id
        for i, interval in enumerate(self.intervals):
            if interval.cat_id == cat_id:
                self.intervals.pop(i)
                break

class Interval:
    __slots__ = ('start', 'end', 'cat_id')
    def __init__(self, start: int, end: int, cat_id: int):
        self.start = start
        self.end = end
        self.cat_id = cat_id

class ObservationRecord:
    def __init__(self, fence: Fence):
        self.fence = fence
        self.cats_sleeping: dict[int, int] = {}

    def process_sleep(self, cat_id: int, cat_width: int) -> str:
        position = self.fence.try_sleep(cat_id, cat_width)
        if position is None:
            return "impossible"
        self.cats_sleeping[cat_id] = position
        return str(position)

    def process_wakeup(self, cat_id: int):
        if cat_id in self.cats_sleeping:
            self.fence.wake_up(cat_id)
            del self.cats_sleeping[cat_id]

class InputParser:
    def __init__(self):
        self.current_observation: ObservationRecord | None = None

    def parse_line(self, line: str) -> str | None:
        parts = line.split()
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            # New dataset
            W, Q = map(int, parts)
            if W == 0 and Q == 0:
                # end of all datasets
                return None
            self.current_observation = ObservationRecord(Fence(W))
            self.remaining_queries = Q
            return "NEW"  # special signal
        elif self.current_observation is None:
            return None
        elif parts[0] == 's':
            _, cat_id_str, cat_width_str = parts
            cat_id = int(cat_id_str)
            cat_width = int(cat_width_str)
            self.remaining_queries -= 1
            return self.current_observation.process_sleep(cat_id, cat_width)
        elif parts[0] == 'w':
            _, cat_id_str = parts
            cat_id = int(cat_id_str)
            self.current_observation.process_wakeup(cat_id)
            self.remaining_queries -= 1
            return None
        else:
            return None

def main():
    import sys
    parser = InputParser()
    end_of_all = False
    first_dataset = True
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        result = parser.parse_line(line)
        if result is None:
            if parser.current_observation is None:
                continue
        elif result == "NEW":
            if not first_dataset:
                print("END")
            else:
                first_dataset = False
            # start new dataset; just continue
            continue
        else:
            print(result)
    # after all inputs, print END for last dataset if any
    if not first_dataset:
        print("END")

if __name__ == "__main__":
    main()