class Antenna:
    def __init__(self, x: float, y: float, r: float):
        self.x = x
        self.y = y
        self.r = r

    def coverage_square(self):
        # returns (xmin, xmax, ymin, ymax)
        return (self.x - self.r, self.x + self.r, self.y - self.r, self.y + self.r)


class Interval:
    def __init__(self, start: float, end: float):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start < other.start or (self.start == other.start and self.end < other.end)

    def merge(self, other):
        # merge if overlapping or contiguous
        if other.start <= self.end:
            self.end = max(self.end, other.end)
            return True
        return False


class IntervalSet:
    def __init__(self):
        self.intervals = []

    def add_interval(self, new_interval: Interval):
        # Efficiently merge intervals on insertion:
        inserted = False
        merged_intervals = []
        for iv in self.intervals:
            if iv.end < new_interval.start:
                merged_intervals.append(iv)
            elif new_interval.end < iv.start:
                if not inserted:
                    merged_intervals.append(new_interval)
                    inserted = True
                merged_intervals.append(iv)
            else:
                # merge overlap
                new_interval = Interval(min(new_interval.start, iv.start), max(new_interval.end, iv.end))
        if not inserted:
            merged_intervals.append(new_interval)
        self.intervals = merged_intervals

    def total_length(self) -> float:
        length = 0.0
        for iv in self.intervals:
            length += iv.end - iv.start
        return length


class CoverageCalculator:
    def __init__(self, antennas):
        self.antennas = antennas

    def calculate_coverage_area(self) -> float:
        # Implements a line sweep in y using events from intervals on x
        # We convert each antenna coverage into a square region defined by its limits
        # We process vertical scan lines at all y coordinates where coverage starts or ends
        events = []
        for ant in self.antennas:
            xmin, xmax, ymin, ymax = ant.coverage_square()
            events.append((ymin, 'start', xmin, xmax))
            events.append((ymax, 'end', xmin, xmax))

        # Sort events by y coordinate
        events.sort(key=lambda e: (e[0], 0 if e[1] == 'start' else 1))

        active_intervals = IntervalSet()
        prev_y = None
        total_area = 0.0

        for i, (y, kind, xmin, xmax) in enumerate(events):
            if prev_y is not None and y > prev_y:
                height = y - prev_y
                length = active_intervals.total_length()
                total_area += length * height

            if kind == 'start':
                active_intervals.add_interval(Interval(xmin, xmax))
            else:  # kind == 'end'
                # To "remove" the interval we rebuild excluding it, since intervals can overlap
                new_intervals = []
                for iv in active_intervals.intervals:
                    if iv.end <= xmin or iv.start >= xmax:
                        new_intervals.append(iv)
                    else:
                        # We may have partial overlaps - split intervals if needed:
                        if iv.start < xmin:
                            new_intervals.append(Interval(iv.start, xmin))
                        if iv.end > xmax:
                            new_intervals.append(Interval(xmax, iv.end))
                active_intervals.intervals = new_intervals

            prev_y = y

        return total_area


class InputOutputHandler:
    def __init__(self):
        self.dataset_number = 0

    def parse_antenna_data(self, n, lines):
        antennas = []
        for i in range(n):
            x, y, r = map(float, lines[i].split())
            antennas.append(Antenna(x, y, r))
        return antennas

    def process(self):
        import sys
        lines = sys.stdin.read().strip().split('\n')
        idx = 0
        while True:
            if idx >= len(lines):
                break
            n_line = lines[idx].strip()
            idx += 1
            if not n_line:
                continue
            n = int(n_line)
            if n == 0:
                break
            data_lines = lines[idx:idx+n]
            idx += n
            antennas = self.parse_antenna_data(n, data_lines)
            self.dataset_number += 1
            calc = CoverageCalculator(antennas)
            area = calc.calculate_coverage_area()
            print(f"{self.dataset_number} {area:.2f}")


if __name__ == '__main__':
    ioh = InputOutputHandler()
    ioh.process()