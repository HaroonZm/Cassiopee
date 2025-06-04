from typing import List, Tuple, Iterator
import sys


class TrackSection:
    def __init__(self, length: int, number: int):
        self.length = length
        self.number = number


class Station:
    def __init__(self, index: int):
        self.index = index
        self.position = 0  # position from start of line


class Train:
    def __init__(self, velocity: int, start_position: float):
        self.velocity = velocity
        self.position = start_position

    def position_at(self, time: float) -> float:
        return self.position + self.velocity * time


class RailwayLine:
    def __init__(self, sections: List[TrackSection]):
        self.sections = sections
        self.stations = self._calc_stations()

    def _calc_stations(self) -> List[Station]:
        # 11 stations, station 0 at position 0, station 10 at end
        stations = [Station(i) for i in range(11)]
        pos = 0
        stations[0].position = 0
        for i, section in enumerate(self.sections, start=1):
            pos += section.length
            stations[i].position = pos
        return stations

    def total_length(self) -> int:
        return sum(s.length for s in self.sections)


class TrainSimulator:
    def __init__(self, railway: RailwayLine, train1: Train, train2: Train):
        self.railway = railway
        self.train1 = train1
        self.train2 = train2

    def find_meeting_section(self) -> int:
        # Solve time t where position1 = position2
        # Train1 starts at 0 going forward: position = v1 * t
        # Train2 starts at total_length going backward: position = total_length - v2 * t
        # meeting when position1 == position2
        total_length = self.railway.total_length()
        v1 = self.train1.velocity
        v2 = self.train2.velocity

        t_meet = total_length / (v1 + v2)
        meet_position = v1 * t_meet

        # If meet_position is exactly a station position, output smaller of adjacent sections
        stations_positions = [st.position for st in self.railway.stations]
        for i, pos in enumerate(stations_positions):
            if abs(meet_position - pos) < 1e-9:
                # edge case: at station i
                # If station 0 or 10 (terminus)
                if i == 0:
                    return 1
                elif i == len(stations_positions) - 1:
                    return len(self.railway.sections)
                else:
                    # output smaller of two adjacent section numbers
                    left_section_number = i  # section on left of station i has number i
                    right_section_number = i + 1  # section on right has number i+1
                    return min(left_section_number, right_section_number)

        # Else find which section meet_position belongs to
        position_acc = 0
        for section in self.railway.sections:
            position_acc += section.length
            if meet_position < position_acc:
                return section.number

        # fallback (should not reach here)
        return self.railway.sections[-1].number


class InputParser:
    @staticmethod
    def parse_line(line: str) -> Tuple[List[int], int, int]:
        # line like "1,1,1,1,1,1,1,1,1,1,40,60"
        parts = list(map(int, line.strip().split(',')))
        lengths = parts[:10]
        v1 = parts[10]
        v2 = parts[11]
        return lengths, v1, v2

    @staticmethod
    def parse_input() -> Iterator[Tuple[List[int], int, int]]:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            yield InputParser.parse_line(line)


def main():
    for lengths, v1, v2 in InputParser.parse_input():
        sections = [TrackSection(length=l, number=i + 1) for i, l in enumerate(lengths)]
        railway = RailwayLine(sections)
        # Train1 starts at position 0 going right, Train2 starts at total_length going left
        total_length = railway.total_length()
        train1 = Train(velocity=v1, start_position=0)
        train2 = Train(velocity=-v2, start_position=total_length)
        # We will simulate with train1 moving forward, train2 moving backward by using velocities accordingly:
        # In find_meeting_section we avoided direction sign issue by calculation.

        sim = TrainSimulator(railway, train1, train2)
        meeting_section = sim.find_meeting_section()
        print(meeting_section)


if __name__ == "__main__":
    main()