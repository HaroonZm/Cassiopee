from typing import List, Tuple, Protocol, runtime_checkable, Iterator
import heapq
import sys

@runtime_checkable
class IntervalProvider(Protocol):
    def intervals(self) -> Iterator[Tuple[int, int]]:
        ...

class PassengerTravelData:
    """
    Represents the passengers' travel data as intervals along stations.
    """
    def __init__(self, journey_segments: List[Tuple[int, int]]) -> None:
        self._segments = journey_segments

    def intervals(self) -> Iterator[Tuple[int, int]]:
        for segment in self._segments:
            yield segment

class IntervalEndpointOrganizer:
    """
    Organizes endpoints of intervals separately for event-driven processing.
    """
    def __init__(self, intervals: Iterator[Tuple[int, int]]) -> None:
        self._start_points: List[int] = []
        self._end_points: List[int] = []
        self._load_intervals(intervals)

    def _load_intervals(self, intervals: Iterator[Tuple[int, int]]) -> None:
        # Decompose intervals into start and end points separately
        for a, b in intervals:
            self._start_points.append(a)
            self._end_points.append(b)
        # Sort endpoints independently
        self._start_points.sort()
        self._end_points.sort()

    @property
    def start_points(self) -> List[int]:
        return self._start_points

    @property
    def end_points(self) -> List[int]:
        return self._end_points

class IntervalOverlapAnalyzer:
    """
    Analyzes intervals for maximum overlaps and related properties.
    """

    @staticmethod
    def max_concurrent_overlaps(starts: List[int], ends: List[int]) -> int:
        """
        Calculates the maximum number of intervals overlapping at any station.
        This corresponds to the maximum concurrency in interval coverage.
        """
        max_overlap = 0
        current_overlap = 0
        i, j = 0, 0
        n_starts, n_ends = len(starts), len(ends)
        while i < n_starts and j < n_ends:
            if starts[i] < ends[j]:
                current_overlap += 1
                max_overlap = max(max_overlap, current_overlap)
                i += 1
            else:
                current_overlap -= 1
                j += 1
        # In case any starts remain
        while i < n_starts:
            current_overlap += 1
            max_overlap = max(max_overlap, current_overlap)
            i += 1
        # No need to process ends remaining for max overlap
        return max_overlap

class SeatRequirementPolicy1:
    """
    Computes the required seats for policy-1:
    Passengers may choose any free seat at reservation time.
    The calculation must consider all permutation orders.
    The worst case is the maximum number of intervals overlapping at any point.
    """

    @classmethod
    def compute_required_seats(cls, travel_data: IntervalProvider) -> int:
        endpoints = IntervalEndpointOrganizer(travel_data.intervals())
        # Under policy-1 the worst case is the maximum number of passengers concurrently traveling
        concurrent = IntervalOverlapAnalyzer.max_concurrent_overlaps(
            endpoints.start_points,
            endpoints.end_points
        )
        return concurrent

class SeatRequirementPolicy2:
    """
    Computes the required seats for policy-2:
    Seat assignments are decided after all reservations are completed (offline).
    Corresponds to the chromatic number in interval graph (minimum number of colors needed).
    Can be obtained by scheduling intervals greedily on minimum resources.
    """

    @classmethod
    def compute_required_seats(cls, travel_data: IntervalProvider) -> int:
        intervals_sorted_by_start = sorted(travel_data.intervals(), key=lambda x: x[0])
        # Min-heap to store end times of intervals currently assigned a seat
        min_heap: List[int] = []
        for (start, end) in intervals_sorted_by_start:
            if min_heap and min_heap[0] <= start:
                # Reuse the seat with the earliest freeing time
                heapq.heapreplace(min_heap, end)
            else:
                # Need a new seat
                heapq.heappush(min_heap, end)
        return len(min_heap)

class ScenicRailroadSeatEstimator:
    """
    Main orchestrator class estimating seat requirements for both policies.
    """
    def __init__(self, passenger_travel_intervals: List[Tuple[int, int]]) -> None:
        self.travel_data = PassengerTravelData(passenger_travel_intervals)

    def estimate(self) -> Tuple[int, int]:
        s1 = SeatRequirementPolicy1.compute_required_seats(self.travel_data)
        s2 = SeatRequirementPolicy2.compute_required_seats(self.travel_data)
        return s1, s2

class InputParser:
    """
    Abstract input parser for passenger travel data.
    """
    @staticmethod
    def parse_input(raw_input: List[str]) -> List[Tuple[int, int]]:
        n = int(raw_input[0])
        intervals = []
        for i in range(1, n + 1):
            a, b = map(int, raw_input[i].split())
            intervals.append((a, b))
        return intervals

def main() -> None:
    input_lines = sys.stdin.read().strip().split('\n')
    passenger_intervals = InputParser.parse_input(input_lines)
    estimator = ScenicRailroadSeatEstimator(passenger_intervals)
    s1, s2 = estimator.estimate()
    print(s1, s2)

if __name__ == "__main__":
    main()