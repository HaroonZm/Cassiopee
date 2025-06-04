class Station:
    def __init__(self, index: int):
        self.index = index

class RailRing:
    def __init__(self, station_count: int):
        self.station_count = station_count

    def distance(self, from_station: Station, to_station: Station) -> int:
        diff = abs(from_station.index - to_station.index)
        return 100 * min(diff, self.station_count - diff)

class ShoppingTour:
    def __init__(self, rail_ring: RailRing, start_station: Station, shopping_stations: list[Station]):
        self.rail_ring = rail_ring
        self.start_station = start_station
        self.shopping_stations = shopping_stations

    def compute_min_cost(self) -> int:
        all_stations = self.shopping_stations + [self.start_station]
        indices = [s.index for s in all_stations]
        leftmost = min(indices)
        rightmost = max(indices)
        N = self.rail_ring.station_count
        # Possible minimal cost candidates initialization
        candidates = []

        # Clockwise and anticlockwise costs if we wrap over the ring
        clockwise_span = (rightmost - leftmost) * 100
        anticlockwise_span = (N - (rightmost - leftmost)) * 100

        # Compute cost visiting all shopping stations on the shortest segment of the ring
        # Case 1: go from start to leftmost, then rightmost
        cost1 = self.rail_ring.distance(self.start_station, Station(leftmost)) + clockwise_span
        candidates.append(cost1)
        # Case 2: go from start to rightmost, then leftmost going counterclockwise
        cost2 = self.rail_ring.distance(self.start_station, Station(rightmost)) + clockwise_span
        candidates.append(cost2)
        # Case 3: similar but using anticlockwise span of the ring 
        cost3 = self.rail_ring.distance(self.start_station, Station(leftmost)) + anticlockwise_span
        candidates.append(cost3)
        cost4 = self.rail_ring.distance(self.start_station, Station(rightmost)) + anticlockwise_span
        candidates.append(cost4)

        # The minimal cost is the minimum of the above candidates
        return min(candidates)

def parse_input() -> ShoppingTour:
    import sys
    input = sys.stdin.readline
    N, M, p = map(int, input().split())
    shopping_indices = [int(input()) for _ in range(M)]
    rail_ring = RailRing(N)
    start_station = Station(p)
    shopping_stations = [Station(idx) for idx in shopping_indices]
    return ShoppingTour(rail_ring, start_station, shopping_stations)

def main():
    tour = parse_input()
    print(tour.compute_min_cost())

if __name__ == "__main__":
    main()