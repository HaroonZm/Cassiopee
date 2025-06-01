from typing import List, Tuple, Iterator
import sys

class Pedestrian:
    def __init__(self, weight: int, start: int, end: int):
        self.weight = weight
        self.start = start
        self.end = end

class BridgeWeightMonitor:
    def __init__(self, max_load: int = 150):
        self.max_load = max_load
        self.current_load = 0

    def can_add(self, weight: int) -> bool:
        return self.current_load + weight <= self.max_load

    def add_pedestrian(self, weight: int):
        self.current_load += weight

    def remove_pedestrian(self, weight: int):
        self.current_load -= weight

class BridgeStatus:
    OK = "OK"
    NG = "NG"

class BridgeSimulator:
    def __init__(self, pedestrians: List[Pedestrian], max_load: int = 150):
        self.pedestrians = pedestrians
        self.max_load = max_load
        self.monitor = BridgeWeightMonitor(max_load)

    def _generate_timeline(self) -> Iterator[Tuple[int, int]]:
        events = []
        # We adopt an event-driven approach: (time, weight_change)
        # At start time a_i, person steps onto bridge => weight +m_i
        # At end time b_i, person steps off bridge => weight -m_i
        # Important: at a_i person is on bridge; at b_i not on bridge.
        for p in self.pedestrians:
            events.append((p.start, p.weight))
            events.append((p.end, -p.weight))
        # Sort by time ascending, but in case of tie start events before end events,
        # so that we add weight before removing at the same timestamp if needed.
        # Actually, from problem, a_i < b_i always, but just in case:
        events.sort(key=lambda x: (x[0], -x[1]))
        for event in events:
            yield event

    def simulate(self) -> str:
        for time, delta_weight in self._generate_timeline():
            if delta_weight > 0:
                if not self.monitor.can_add(delta_weight):
                    return BridgeStatus.NG
                self.monitor.add_pedestrian(delta_weight)
            else:
                self.monitor.remove_pedestrian(-delta_weight)
        return BridgeStatus.OK

class DataSetLoader:
    def __init__(self, input_source):
        self.input_source = input_source

    def _read_int(self) -> int:
        line = next(self.input_source).strip()
        while line == '':
            line = next(self.input_source).strip()
        return int(line)

    def datasets(self) -> Iterator[List[Pedestrian]]:
        while True:
            try:
                n = self._read_int()
                if n == 0:
                    break
                pedestrians = []
                for _ in range(n):
                    line = next(self.input_source).strip()
                    while line == '':
                        line = next(self.input_source).strip()
                    m_str, a_str, b_str = line.split()
                    m, a, b = int(m_str), int(a_str), int(b_str)
                    pedestrians.append(Pedestrian(m, a, b))
                yield pedestrians
            except StopIteration:
                break

def main():
    loader = DataSetLoader(iter(sys.stdin))
    for dataset in loader.datasets():
        simulator = BridgeSimulator(dataset)
        result = simulator.simulate()
        print(result)

if __name__ == "__main__":
    main()