class Car:
    def __init__(self, number: int):
        self.number = number

class Lane:
    def __init__(self, lane_id: int):
        self.lane_id = lane_id
        self.queue = []

    def add_car(self, car: Car):
        self.queue.append(car)

    def remove_front_car(self) -> Car:
        if self.queue:
            return self.queue.pop(0)
        raise IndexError("Trying to remove a car from an empty lane")

    def car_count(self) -> int:
        return len(self.queue)

    def front_car_number(self) -> int:
        if self.queue:
            return self.queue[0].number
        raise IndexError("No car at front")

class LaneSelectorStrategy:
    def select_lane(self, lanes: list[Lane]) -> Lane:
        raise NotImplementedError()

class MinLengthThenMinIdSelector(LaneSelectorStrategy):
    def select_lane(self, lanes: list[Lane]) -> Lane:
        # Select lane with fewest cars; if tie, smallest lane ID
        min_count = min(lane.car_count() for lane in lanes)
        candidate_lanes = [lane for lane in lanes if lane.car_count() == min_count]
        candidate_lanes.sort(key=lambda l: l.lane_id)
        return candidate_lanes[0]

class GasStation:
    def __init__(self, lane_count: int, selector: LaneSelectorStrategy):
        self.lanes = [Lane(i+1) for i in range(lane_count)]
        self.selector = selector
        self.car_to_lane = {}

    def car_enters(self, car_number: int):
        car = Car(car_number)
        lane = self.selector.select_lane(self.lanes)
        lane.add_car(car)
        self.car_to_lane[car_number] = lane.lane_id

    def fueling_finished(self, lane_id: int) -> int:
        lane = self.lanes[lane_id-1]
        car = lane.remove_front_car()
        return car.number

class InputParser:
    def __init__(self):
        self.N = 0
        self.M = 0
        self.commands = []

    def parse(self):
        import sys
        first_line = sys.stdin.readline()
        self.N, self.M = map(int, first_line.split())
        for _ in range(self.M):
            line = sys.stdin.readline()
            parts = line.split()
            cmd_type = int(parts[0])
            arg = int(parts[1])
            self.commands.append((cmd_type, arg))

class OutputHandler:
    def __init__(self):
        self.results = []

    def record(self, number: int):
        self.results.append(number)

    def flush(self):
        for number in self.results:
            print(number)

class GasStationApp:
    def __init__(self):
        self.parser = InputParser()
        self.output_handler = OutputHandler()
        self.gas_station = None

    def run(self):
        self.parser.parse()
        self.gas_station = GasStation(self.parser.N, MinLengthThenMinIdSelector())
        for cmd_type, arg in self.parser.commands:
            if cmd_type == 1:
                self.gas_station.car_enters(arg)
            elif cmd_type == 0:
                finished_car_number = self.gas_station.fueling_finished(arg)
                self.output_handler.record(finished_car_number)
        self.output_handler.flush()

if __name__ == "__main__":
    GasStationApp().run()