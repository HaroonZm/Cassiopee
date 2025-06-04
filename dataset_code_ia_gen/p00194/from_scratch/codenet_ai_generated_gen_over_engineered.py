from collections import defaultdict, deque
import sys
import heapq

# Abstraction for a 2D grid coordinate system using named roads
class Coordinate:
    def __init__(self, east_west: str, north_south: int):
        self.east_west = east_west
        self.north_south = north_south

    @staticmethod
    def from_str(s: str):
        # parse strings like 'a-1'
        ew, ns = s.split('-')
        return Coordinate(ew, int(ns))

    def __str__(self):
        return f"{self.east_west}-{self.north_south}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            return False
        return self.east_west == other.east_west and self.north_south == other.north_south

    def __hash__(self):
        return hash((self.east_west, self.north_south))

    # For sorting or comparisons
    def __lt__(self, other):
        if self.east_west != other.east_west:
            return self.east_west < other.east_west
        return self.north_south < other.north_south

# Represents a traffic signal with a cycle
class TrafficSignal:
    def __init__(self, coord: Coordinate, cycle: int):
        self.coord = coord
        self.cycle = cycle

    def is_green_at(self, direction: str, time: int) -> bool:
        # Direction: one of 'N', 'S', 'E', 'W'
        # Initial state at t=0: NS green, EW red.
        # signal toggles every k minutes; green for NS then EW alternating.
        # Return True if green on approach direction at given time.
        phase_time = time % (2 * self.cycle)
        ns_green = phase_time < self.cycle
        if direction in ('N', 'S'):
            return ns_green
        else:
            return not ns_green

# Represents a road between two intersections
class Road:
    def __init__(self, coord1: Coordinate, coord2: Coordinate, base_time: int):
        self.coord1 = coord1
        self.coord2 = coord2
        self.base_time = base_time
        self.congested_delay = 0
        self.closed = False

    def travel_time(self):
        if self.closed:
            return None
        return self.base_time + self.congested_delay

    def connects(self, c1: Coordinate, c2: Coordinate) -> bool:
        return (self.coord1 == c1 and self.coord2 == c2) or (self.coord1 == c2 and self.coord2 == c1)

    def other_end(self, c: Coordinate) -> Coordinate:
        if c == self.coord1:
            return self.coord2
        elif c == self.coord2:
            return self.coord1
        else:
            return None

# Encapsulates the whole city map, roads and signals
class CityMap:
    def __init__(self, M: int, N: int, base_travel_time: int):
        self.M = M
        self.N = N
        self.base_travel_time = base_travel_time
        self.signals = dict()  # Coordinate -> TrafficSignal
        self.roads = dict()    # frozenset{Coordinate, Coordinate} -> Road
        # Adjacent intersections by coordinate
        self.adjacency = defaultdict(list)
        # Precompute valid intersections for grid
        self.valid_intersections = set()
        ew_roads = [chr(ord('a') + i) for i in range(M)]
        ns_roads = [i + 1 for i in range(N)]
        for ew in ew_roads:
            for ns in ns_roads:
                self.valid_intersections.add(Coordinate(ew, ns))

        # Construct full grid roads (all connections between adjacent intersections)
        self._build_all_roads()

    def _build_all_roads(self):
        # Add roads connecting adjacent intersections East-West and North-South
        for coord in self.valid_intersections:
            # East neighbor
            ew_ord = ord(coord.east_west)
            east_ew_ord = ew_ord + 1
            if east_ew_ord < ord('a') + self.M:
                east_coord = Coordinate(chr(east_ew_ord), coord.north_south)
                self.add_road(coord, east_coord, self.base_travel_time)
            # South neighbor
            south_ns = coord.north_south + 1
            if south_ns <= self.N:
                south_coord = Coordinate(coord.east_west, south_ns)
                self.add_road(coord, south_coord, self.base_travel_time)

    def add_road(self, c1: Coordinate, c2: Coordinate, base_time: int):
        key = frozenset([c1, c2])
        if key not in self.roads:
            road = Road(c1, c2, base_time)
            self.roads[key] = road
            self.adjacency[c1].append(c2)
            self.adjacency[c2].append(c1)
        else:
            # Possibly update base_time if different?
            pass

    def set_signal(self, coord: Coordinate, cycle: int):
        self.signals[coord] = TrafficSignal(coord, cycle)

    def close_road(self, c1: Coordinate, c2: Coordinate):
        key = frozenset([c1, c2])
        if key in self.roads:
            self.roads[key].closed = True

    def set_congested_delay(self, c1: Coordinate, c2: Coordinate, delay: int):
        key = frozenset([c1, c2])
        if key in self.roads:
            self.roads[key].congested_delay = delay

    def get_road_between(self, c1: Coordinate, c2: Coordinate) -> Road:
        key = frozenset([c1, c2])
        return self.roads.get(key, None)

    def has_signal(self, coord: Coordinate) -> bool:
        return coord in self.signals

    def get_signal(self, coord: Coordinate) -> TrafficSignal:
        return self.signals.get(coord, None)

# Enumeration to represent movement directions
class Direction:
    # Mappings for coordinate axis changes
    EAST = 'E'
    WEST = 'W'
    NORTH = 'N'
    SOUTH = 'S'

    @staticmethod
    def between(c_from: Coordinate, c_to: Coordinate):
        # Determine direction of movement from c_from to c_to
        if c_from.east_west == c_to.east_west:
            if c_from.north_south < c_to.north_south:
                return Direction.SOUTH
            else:
                return Direction.NORTH
        elif c_from.north_south == c_to.north_south:
            if c_from.east_west < c_to.east_west:
                return Direction.EAST
            else:
                return Direction.WEST
        else:
            return None

    @staticmethod
    def opposite(direction: str):
        return {'N':'S', 'S':'N', 'E':'W', 'W':'E'}[direction]

# State for Dijkstra's with directions and time
class State:
    def __init__(self, coordinate: Coordinate, facing: str, time: int):
        self.coordinate = coordinate
        self.facing = facing
        self.time = time

    def __lt__(self, other):
        return self.time < other.time

# A complex car navigation system encapsulation
class CarNavigationSystem:
    def __init__(self, city_map: CityMap, start: Coordinate, destination: Coordinate):
        self.city_map = city_map
        self.start = start
        self.destination = destination
        self.max_time_limit = 100  # given problem constraint

    def compute_shortest_time(self) -> int:
        # Use Dijkstra but state includes facing direction and current intersection and time
        # Facing direction at start = East, time=0
        # At each intersection, cannot do U-turn

        # Distances dictionary: (Coordinate, facing) -> minimum time
        dist = dict()

        # Priority queue: (time, Coordinate, facing)
        heap = []
        start_facing = Direction.EAST
        start_state = State(self.start, start_facing, 0)
        dist[(self.start, start_facing)] = 0
        heapq.heappush(heap, (0, start_state))

        while heap:
            current_time, current_state = heapq.heappop(heap)
            c = current_state.coordinate
            f = current_state.facing
            t = current_state.time
            if (c, f) not in dist or dist[(c, f)] < t:
                continue
            if c == self.destination:
                # Destination reached
                return t

            # Explore neighbors
            for neighbor in self.city_map.adjacency[c]:
                road = self.city_map.get_road_between(c, neighbor)
                if road is None or road.closed:
                    continue

                travel_time = road.travel_time()
                if travel_time is None:
                    continue

                # Determine direction from c to neighbor
                move_dir = Direction.between(c, neighbor)
                if move_dir is None:
                    continue

                # No U-turn
                if Direction.opposite(f) == move_dir:
                    continue

                # Calculate arrival time at neighbor
                depart_time = t

                arrival_time = depart_time + travel_time

                # Must check signal at neighbor at arrival_time for movement direction
                # The direction we arrive from is opposite of move_dir
                # Because signal controls arrival into intersection
                if self.city_map.has_signal(neighbor):
                    signal = self.city_map.get_signal(neighbor)
                    arrive_dir = Direction.opposite(move_dir)  # direction from which we arrive
                    # If red at arrival time, must wait until green
                    if not signal.is_green_at(arrive_dir, arrival_time):
                        # Wait until next green
                        cycle = signal.cycle
                        # calculate wait time until green for arrive_dir
                        # cycle: green time is first k, red next k, repeat
                        # if arrive_dir is NS, green in [0,k), red in [k,2k)
                        # if arrive_dir is EW, inverse
                        time_in_cycle = arrival_time % (2*cycle)
                        if arrive_dir in ('N','S'):
                            # NS green if time_in_cycle < k
                            wait = 0
                            if time_in_cycle >= cycle:
                                wait = (2*cycle) - time_in_cycle
                        else:
                            # EW green if time_in_cycle >= k
                            wait = 0
                            if time_in_cycle < cycle:
                                wait = cycle - time_in_cycle
                        arrival_time += wait

                # After arriving, can face any direction except the opposite direction of arrival_dir
                # But from problem: truck can only turn directions at intersection
                # It can face N, S, E, W as long as not the direction of coming back (u-turn)
                # For next edge, facing is the direction truck will go,
                # So set facing = move_dir (direction to neighbor)
                new_facing = move_dir

                # Check dist and update
                key = (neighbor, new_facing)
                if key not in dist or dist[key] > arrival_time:
                    dist[key] = arrival_time
                    if arrival_time <= self.max_time_limit:
                        heapq.heappush(heap, (arrival_time, State(neighbor, new_facing, arrival_time)))

        # If no path found within limit, problem states reachable within 100 minutes.
        # So return something large or no solution fallback
        return -1

# Main input/output processing and calculation engine
class Solver:
    def __init__(self):
        self.results = []

    def solve(self):
        input_lines = sys.stdin.read().strip().split('\n')
        idx = 0
        while idx < len(input_lines):
            line = input_lines[idx].strip()
            if line == "0 0":
                break
            if not line:
                idx += 1
                continue
            M, N = map(int, line.split())
            idx += 1
            D = int(input_lines[idx].strip())
            idx += 1
            ns = int(input_lines[idx].strip())
            idx += 1

            city_map = CityMap(M, N, D)

            # Signals
            for _ in range(ns):
                parts = input_lines[idx].strip().split()
                idx += 1
                coord = Coordinate.from_str(parts[0])
                cycle = int(parts[1])
                city_map.set_signal(coord, cycle)

            nc = int(input_lines[idx].strip())
            idx += 1
            # Closed roads
            for _ in range(nc):
                parts = input_lines[idx].strip().split()
                idx += 1
                c1 = Coordinate.from_str(parts[0])
                c2 = Coordinate.from_str(parts[1])
                city_map.close_road(c1, c2)

            nj = int(input_lines[idx].strip())
            idx += 1
            # Congested roads
            for _ in range(nj):
                parts = input_lines[idx].strip().split()
                idx += 1
                c1 = Coordinate.from_str(parts[0])
                c2 = Coordinate.from_str(parts[1])
                delay = int(parts[2])
                city_map.set_congested_delay(c1, c2, delay)

            # Start and destination coordinates
            sd = input_lines[idx].strip().split()
            idx += 1
            start = Coordinate.from_str(sd[0])
            destination = Coordinate.from_str(sd[1])

            nav = CarNavigationSystem(city_map, start, destination)
            shortest_time = nav.compute_shortest_time()
            self.results.append(str(shortest_time))

        # Output results
        print('\n'.join(self.results))


if __name__ == "__main__":
    Solver().solve()