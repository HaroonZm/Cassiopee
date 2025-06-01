class TrainType:
    def __init__(self, name: str, time_between_stations: int, stops: 'StopSet'):
        self.name = name
        self.time = time_between_stations
        self.stops = stops

class StopSet:
    """
    Abstract class for stops, implemented by specific collections.
    """
    def __init__(self, stops_sorted: list):
        self.stops = stops_sorted

    def contains(self, station: int) -> bool:
        # Binary search for membership
        import bisect
        index = bisect.bisect_left(self.stops, station)
        return index < len(self.stops) and self.stops[index] == station

    def __len__(self):
        return len(self.stops)

    def __getitem__(self,index):
        return self.stops[index]

class SemiexpressStops(StopSet):
    """
    Semiexpress stops: must include the express stops and have exactly K stops.
    We can add stops to maximize reachable stations within T.
    We choose other stops to best cover between express stops, minimizing semiexpress travel time.
    """
    def __init__(self, express_stops: list, K: int, N: int):
        self.N = N
        self.express_stops = express_stops
        self.K = K
        # Initial stops set is the express stops
        self.current_stops = list(express_stops)
        self.M = len(express_stops)
        self.additional_stop_limit = K - self.M
        # We will intelligently add stops
        self._plan_additional_stops()
        super().__init__(sorted(self.current_stops))

    def _plan_additional_stops(self):
        # The semiexpress train must stop at all express stops S_1 < ... < S_M
        # We can add (K - M) stops at stations in between
        # Goal: maximize number of reachable stations from station 1 within T minutes
        # Strategy:
        # - Semiexpress stops can reduce travel time on some segments compared to local
        # - We want to add stops to reduce long local hops
        # 
        # We'll add stops greedily on segments between express stops to create smaller sub-segments
        # since C < A (semiexpress is faster than local), stopping more allows more fast travel segments.
        #
        # With limited stops, add stops equidistantly on longest segments.

        segments = []
        for i in range(self.M - 1):
            left = self.express_stops[i]
            right = self.express_stops[i+1]
            length = right - left
            segments.append({'start': left, 'end': right, 'length': length, 'added_stops': []})

        # Total additional stops to distribute
        total_add = self.additional_stop_limit

        # Distribute additional stops to segments proportionally to their length (heuristic)
        lengths = [seg['length'] for seg in segments]
        length_sum = sum(lengths)
        allocated = [0]*len(segments)

        # first allocate minimum 0 stops
        # then distribute stops by length proportion rounded down, remaining distribute one by one largest segments
        for i, seg in enumerate(segments):
            allocated[i] = (total_add * seg['length']) // length_sum
        leftover = total_add - sum(allocated)

        # Distribute leftover one by one to largest segments first
        segments_sorted_idx = sorted(range(len(segments)), key=lambda i: segments[i]['length'], reverse=True)
        for i in segments_sorted_idx:
            if leftover <= 0:
                break
            allocated[i] += 1
            leftover -= 1

        # For each segment, place allocated[i] stops evenly
        for i, seg in enumerate(segments):
            count = allocated[i]
            if count == 0:
                continue
            start = seg['start']
            end = seg['end']
            length = seg['length']

            # Evenly place stops in (start+1, ..., end-1)
            # Use integer division to choose positions nearest to equal divisions
            for j in range(1, count + 1):
                # position = round(start + j * length / (count + 1))
                pos = start + (length * j) // (count + 1)
                seg['added_stops'].append(pos)

        # Add all stops decided to current_stops set
        added_stops = []
        for seg in segments:
            added_stops.extend(seg['added_stops'])
        # Remove duplicates and filter valid stations in [1,N]
        unique_added = sorted(set([s for s in added_stops if 1 < s < self.N]))
        # Combine express stops and added stops
        self.current_stops = sorted(set(self.express_stops) | set(unique_added))

class RailwayNetwork:
    def __init__(self, N:int, M:int, K:int, A:int, B:int, C:int, T:int, express_stops: list):
        self.N = N
        self.M = M
        self.K = K
        self.A = A
        self.B = B
        self.C = C
        self.T = T
        self.express_stops = express_stops

        self.local_stops = StopSet(list(range(1, N+1)))  # local stops at every station
        self.express_stops_set = StopSet(express_stops)
        self.semiexpress_stops = SemiexpressStops(express_stops, K, N)

        self.local_train = TrainType('local', A, self.local_stops)
        self.express_train = TrainType('express', B, self.express_stops_set)
        self.semiexpress_train = TrainType('semiexpress', C, self.semiexpress_stops)

        # Combine all stop sets for lookup
        self.all_stop_sets = [self.local_stops, self.express_stops_set, self.semiexpress_stops]

    def is_stop(self, train: TrainType, station: int) -> bool:
        return train.stops.contains(station)

    def min_travel_time(self, target_station: int) -> int:
        """
        Calculate minimal travel time from station 1 to target_station,
        using local, express, semiexpress trains with transfers only at common stops.
        Direction only from smaller to larger station number.
        """

        # Because N can be up to 10^9, we cannot do DP over stations.
        # But M,K <= 3000, semiexpress stops up to 3000, and there is structure.

        # Approach:
        # Use stations in 1..target_station only.
        # The stations where at least one train stops are local stops (all stations),
        # express stops (M stops), semiexpress stops (K stops).
        # At any station where multiple train stops intersect, transfer is possible.

        # But local train stops everywhere, so transfer can be done at any station.

        # Actually, this implies graph is a linear chain from 1 to target_station,
        # with edges having costs A,B,C depending on which trains run and whether they stop.

        # Take minimum time for each edge i->i+1:
        # Among trains stopping at i and i+1, pick minimal time per edge.

        # local train stops at all, time A
        # express train stops at express_stops, time B
        # semiexpress train stops at semiexpress_stops, time C

        # An edge i -> i+1 can be traveled by any train that stops at both i and i+1.
        # So for each edge, we'll check which trains stop at i and i+1, minimal time.

        # We'll process edges i=1 to target_station-1.

        # For efficient queries, prepare presence arrays for express and semiexpress stops
        # Local train is always available

        # Because target_station can be large (up to 10^9), we can't iterate all edges.
        # But semiexpress and express stops are small lists (<=3000).

        # We use interval partition:
        # For each train, the train operates only on intervals between its stops.

        # We'll build a unified partition of [1..target_station] into "segments" where minimal time per edge is constant.

        # Steps:
        # 1. Collect all stops (1 .. target_station) for express and semiexpress trains
        # 2. Combine stops of local (all stations), express, semiexpress
        # 3. For edges between these stops ranges, compute minimal travel time edge cost.

        # Let's do this:

        relevant_semiexpress_stops = [s for s in self.semiexpress_stops.stops if s <= target_station]
        relevant_express_stops = [s for s in self.express_stops if s <= target_station]

        # Merge all stops of express and semiexpress for partition points, plus target_station+1 as boundary
        partition_points = set()
        partition_points.update(relevant_express_stops)
        partition_points.update(relevant_semiexpress_stops)
        partition_points.add(1)
        partition_points.add(target_station+1)
        partition_points = sorted(partition_points)

        # We'll find minimal cost between adjacent stations.
        # Any station between partition_points[i] and partition_points[i+1]-1 is not a stop of express nor semiexpress,
        # so local only.

        total_time = 0
        for i in range(len(partition_points) - 1):
            left = partition_points[i]
            right = partition_points[i+1]
            length = right - left  # number of edges:

            if length <= 0:
                continue

            # We need to know minimal edge time in [left .. right-1]

            # Check if express stops both sides to use express speed B
            # Check if semiexpress stops both sides to use C
            # else local A

            # Note: distances between stops mean trains run on those segments at corresponding time.

            # For segment from left to right-1 (edges), find minimal edge time:
            # Check if this segment is covered by express train edges:
            # Express train runs on intervals between express stops

            # Check if left and left+1 are covered by express train (i.e. both stops in express set)
            # Actually, express train stops at express stops only,
            # so between S_i and S_{i+1} it's continuous express edges

            # Because express stops are sorted and discrete,
            # if left and right-1 are in an express interval, we can use express time

            # Similarly for semiexpress

            # Check the deepest train coverage

            def covers(train_stops: list, start: int, end: int) -> bool:
                # train_stops sorted
                # check if there exists i where train_stops[i] <= start < end <= train_stops[i+1]
                # meaning train covers interval [start,end]
                import bisect
                idx = bisect.bisect_right(train_stops, start) - 1
                if idx < 0 or idx+1 >= len(train_stops):
                    return False
                return train_stops[idx] <= start and end <= train_stops[idx+1]

            segment_start = left
            segment_end = right - 1 # last edge

            if covers(relevant_express_stops, segment_start, segment_end):
                best_time = self.B
            elif covers(relevant_semiexpress_stops, segment_start, segment_end):
                best_time = self.C
            else:
                best_time = self.A

            total_time += best_time * length

            if total_time > self.T:
                # no need to continue: we exceeded time
                break

        return total_time

    def max_reachable_stations(self) -> int:
        # We want max number of stations i (2 <= i <= N) reachable from 1 within T
        # Use binary search on i in [1..N] for max i reachable in T minutes.

        low = 1
        high = self.N

        while low < high:
            mid = (low + high + 1) // 2
            time = self.min_travel_time(mid)
            if time <= self.T:
                low = mid
            else:
                high = mid - 1
        # exclude station 1:
        return max(0, low - 1)

def main():
    import sys
    input = sys.stdin.readline

    N, M, K = map(int, input().split())
    A, B, C = map(int, input().split())
    T = int(input())
    express_stops = [int(input()) for _ in range(M)]

    rail = RailwayNetwork(N, M, K, A, B, C, T, express_stops)
    print(rail.max_reachable_stations())

if __name__ == "__main__":
    main()