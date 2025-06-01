from typing import List, Tuple, Iterator


class Section:
    def __init__(self, index: int, length: int):
        self.index = index
        self.length = length


class Train:
    def __init__(self, velocity: int):
        self.velocity = velocity  # km/h

    def position_at(self, time: float) -> float:
        """Calculates position after time hours."""
        return self.velocity * time


class RailwayLine:
    def __init__(self, sections: List[Section]):
        self.sections = sections
        self.total_length = sum(section.length for section in sections)
        self.cumulative_distances = self._calc_cumulative_distances()

    def _calc_cumulative_distances(self) -> List[int]:
        cumulative = [0]
        for section in self.sections:
            cumulative.append(cumulative[-1] + section.length)
        return cumulative

    def locate_section(self, position: float) -> int:
        """
        Given a position from the left terminal in km,
        returns the section index where the position lies.
        If position is exactly on a boundary station between sections i and i+1,
        returns the smaller section number i.
        """
        # Binary search for efficiency and abstraction
        low, high = 0, len(self.cumulative_distances) - 1
        while low < high:
            mid = (low + high) // 2
            if self.cumulative_distances[mid] == position:
                # On station: return smaller of adjacent sections
                return max(mid - 1, 0)
            elif self.cumulative_distances[mid] < position:
                low = mid + 1
            else:
                high = mid
        return low - 1


class MeetingAnalyzer:
    def __init__(self, railway_line: RailwayLine, train1: Train, train2: Train):
        self.line = railway_line
        self.train1 = train1
        self.train2 = train2

    def find_meeting_section(self) -> int:
        # Total length of the railway line
        L = self.line.total_length

        # Using relative motion, position from train 1 terminal at time t:
        # train1 position: v1 * t
        # train2 position from left terminal: L - v2 * t
        # Trains meet when positions are equal or overlap:
        # v1 * t = L - v2 * t  => t = L / (v1 + v2)
        t_meet = L / (self.train1.velocity + self.train2.velocity)

        # Position of meeting from train 1 terminal
        meet_pos = self.train1.position_at(t_meet)

        # Locate which section contains the meeting point
        section_index = self.line.locate_section(meet_pos)
        # section_index is zero-based; problem section numbering starts at 1
        return section_index + 1


class DataSetParser:
    @staticmethod
    def parse_line(line: str) -> Tuple[List[int], int, int]:
        parts = line.strip().split(',')
        if len(parts) != 12:
            raise ValueError("Invalid input line: must have 12 comma separated values")
        lengths = list(map(int, parts[:10]))
        v1, v2 = map(int, parts[10:])
        return lengths, v1, v2


def main_loop(lines: Iterator[str]) -> Iterator[int]:
    for line in lines:
        if not line.strip():
            continue
        lengths, v1, v2 = DataSetParser.parse_line(line)
        sections = [Section(i + 1, length) for i, length in enumerate(lengths)]
        railway = RailwayLine(sections)
        train1 = Train(v1)
        train2 = Train(v2)
        analyzer = MeetingAnalyzer(railway, train1, train2)
        yield analyzer.find_meeting_section()


if __name__ == "__main__":
    import sys

    results = main_loop(sys.stdin)
    for res in results:
        print(res)