class Coordinate:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __hash__(self):
        return hash((self._x, self._y))

    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            return False
        return self._x == other._x and self._y == other._y


class Plant:
    def __init__(self, position: Coordinate, height: int = 0):
        self._position = position
        self._height = height

    @property
    def position(self):
        return self._position

    @property
    def height(self):
        return self._height

    def grow(self, increment: int = 1):
        self._height += increment


class FertilizerEvent:
    def __init__(self, position: Coordinate, time: int):
        self._position = position
        self._time = time

    @property
    def position(self):
        return self._position

    @property
    def time(self):
        return self._time


class Field:
    def __init__(self, width: int, height: int, plants_map: list[list[int]]):
        self._width = width
        self._height = height
        self._plants = {}
        for y in range(height):
            for x in range(width):
                if plants_map[y][x] == 1:
                    coord = Coordinate(x, y)
                    self._plants[coord] = Plant(coord)

    def apply_fertilizer(self, fertilize_coord: Coordinate):
        plant = self._plants.get(fertilize_coord)
        if plant:
            plant.grow()

    def total_height(self) -> int:
        return sum(plant.height for plant in self._plants.values())


class FertilizerSchedule:
    def __init__(self):
        self._events = []

    def add_event(self, event: FertilizerEvent):
        self._events.append(event)

    def get_events_up_to(self, time: int):
        return [e for e in self._events if e.time < time]


class FarmSimulator:
    def __init__(self, field: Field, schedule: FertilizerSchedule, max_time: int):
        self._field = field
        self._schedule = schedule
        self._max_time = max_time

    def simulate(self):
        # sort events by time to simulate in chronological order
        events = sorted(self._schedule.get_events_up_to(self._max_time), key=lambda e: e.time)
        for event in events:
            self._field.apply_fertilizer(event.position)

    def result(self) -> int:
        return self._field.total_height()


def main():
    import sys
    input = sys.stdin.readline

    W, H, T = map(int, input().split())
    p = int(input())

    schedule = FertilizerSchedule()
    for _ in range(p):
        x_i, y_i, t_i = map(int, input().split())
        schedule.add_event(FertilizerEvent(Coordinate(x_i, y_i), t_i))

    plants_map = []
    for _ in range(H):
        row = list(map(int, input().split()))
        plants_map.append(row)

    field = Field(W, H, plants_map)
    simulator = FarmSimulator(field, schedule, T)
    simulator.simulate()
    print(simulator.result())


if __name__ == "__main__":
    main()