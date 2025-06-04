from typing import Dict, List, Tuple, Optional, Iterator
import sys
import math
import heapq

class Station:
    def __init__(self, name: str):
        self.name = name
        self.edges: List['RailLink'] = []

    def add_edge(self, edge: 'RailLink'):
        self.edges.append(edge)

class RailLink:
    def __init__(self, station_a: 'Station', station_b: 'Station', distance: int, delay: int):
        self.station_a = station_a
        self.station_b = station_b
        self.distance = distance
        self.delay = delay

    def other_side(self, current: 'Station') -> 'Station':
        if current == self.station_a:
            return self.station_b
        elif current == self.station_b:
            return self.station_a
        raise ValueError(f"Station {current.name} not connected to this rail link")

    def travel_time(self) -> float:
        return self.distance / 40 + self.delay

class RailwayNetwork:
    def __init__(self):
        self.stations: Dict[str, Station] = {}

    def get_or_create_station(self, name: str) -> Station:
        if name not in self.stations:
            self.stations[name] = Station(name)
        return self.stations[name]

    def add_link(self, a_name: str, b_name: str, distance: int, delay: int):
        station_a = self.get_or_create_station(a_name)
        station_b = self.get_or_create_station(b_name)
        link = RailLink(station_a, station_b, distance, delay)
        station_a.add_edge(link)
        station_b.add_edge(link)

class RoutePlanner:
    def __init__(self, network: RailwayNetwork):
        self.network = network

    def shortest_time(self, start_name: str, end_name: str) -> Optional[float]:
        if start_name not in self.network.stations or end_name not in self.network.stations:
            return None
        start = self.network.stations[start_name]
        end = self.network.stations[end_name]

        dist_map: Dict[Station, float] = {station: math.inf for station in self.network.stations.values()}
        dist_map[start] = 0.0
        priority_queue: List[Tuple[float, Station]] = [(0.0, start)]

        while priority_queue:
            current_dist, current_station = heapq.heappop(priority_queue)
            if dist_map[current_station] < current_dist:
                continue
            if current_station == end:
                return current_dist
            for edge in current_station.edges:
                neighbor = edge.other_side(current_station)
                travel = edge.travel_time()
                new_dist = current_dist + travel
                if new_dist < dist_map[neighbor]:
                    dist_map[neighbor] = new_dist
                    heapq.heappush(priority_queue, (new_dist, neighbor))

        return None

class InputParser:
    def __init__(self, input_stream: Iterator[str]):
        self.input_stream = input_stream

    def parse_next_dataset(self) -> Optional[Tuple[int,int,str,str,str,List[Tuple[str,str,int,int]]]]:
        # Read n,m
        while True:
            try:
                line = next(self.input_stream).strip()
                if not line:
                    continue
                n_m = line.split()
                if len(n_m) < 2:
                    continue
                n, m = map(int, n_m)
                if n == 0 and m == 0:
                    return None
                break
            except StopIteration:
                return None
        # Read s,p,g
        while True:
            try:
                line = next(self.input_stream).strip()
                if line:
                    s, p, g = line.split()
                    break
            except StopIteration:
                return None

        edges = []
        for _ in range(m):
            while True:
                try:
                    line = next(self.input_stream).strip()
                    if line:
                        a, b, d, t = line.split()
                        edges.append((a,b,int(d),int(t)))
                        break
                except StopIteration:
                    return None
        return n,m,s,p,g,edges

class Seishun18Solver:
    def __init__(self):
        self.network = RailwayNetwork()

    def build_network(self, edges: List[Tuple[str,str,int,int]]):
        self.network = RailwayNetwork()
        for a,b,d,t in edges:
            self.network.add_link(a,b,d,t)

    def compute_arrival_time(self, s: str, p: str, g: str) -> int:
        planner = RoutePlanner(self.network)
        # shortest time from s to p
        time_sp = planner.shortest_time(s,p)
        # shortest time from p to g
        time_pg = planner.shortest_time(p,g)
        if time_sp is None or time_pg is None:
            raise RuntimeError("No path found in guaranteed reachable graph")
        total_time = time_sp + time_pg
        # Round up to nearest integer hour according to sample output
        return math.ceil(total_time)

def main():
    parser = InputParser(iter(sys.stdin))
    solver = Seishun18Solver()
    while True:
        dataset = parser.parse_next_dataset()
        if dataset is None:
            break
        n,m,s,p,g,edges = dataset
        solver.build_network(edges)
        result = solver.compute_arrival_time(s,p,g)
        print(result)

if __name__ == '__main__':
    main()