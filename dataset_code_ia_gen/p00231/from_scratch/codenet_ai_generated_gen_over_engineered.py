class Bridge:
    MAX_LOAD = 150

    def __init__(self):
        self._people = []
        self._events = []

    def add_person(self, person):
        self._people.append(person)

    def _collect_events(self):
        self._events.clear()
        for person in self._people:
            self._events.append(Event(person.start_time, Event.Type.ENTER, person.weight))
            self._events.append(Event(person.end_time, Event.Type.LEAVE, person.weight))
        self._events.sort()

    def is_safe(self):
        self._collect_events()
        current_weight = 0
        for event in self._events:
            if event.type == Event.Type.ENTER:
                current_weight += event.weight
                if current_weight > Bridge.MAX_LOAD:
                    return False
            elif event.type == Event.Type.LEAVE:
                current_weight -= event.weight
        return True


class Person:
    def __init__(self, weight, start_time, end_time):
        self.weight = weight
        self.start_time = start_time
        self.end_time = end_time


class Event:
    class Type:
        ENTER = 1
        LEAVE = 2

    def __init__(self, time, event_type, weight):
        self.time = time
        self.type = event_type
        self.weight = weight

    def __lt__(self, other):
        if self.time == other.time:
            # LEAVE events before ENTER events to avoid immediate overload at boundary
            return self.type < other.type
        return self.time < other.time


class InputParser:
    def __init__(self, input_source):
        self._input_source = input_source

    def __iter__(self):
        return self

    def __next__(self):
        line = self._input_source.readline()
        while line and line.strip() == '':
            line = self._input_source.readline()

        if not line:
            raise StopIteration

        n = int(line.strip())
        if n == 0:
            raise StopIteration

        bridge = Bridge()
        for _ in range(n):
            parts = []
            while len(parts) < 3:
                parts += self._input_source.readline().strip().split()
            weight, start, end = map(int, parts[:3])
            person = Person(weight, start, end)
            bridge.add_person(person)
        return bridge


def main():
    import sys
    parser = InputParser(sys.stdin)
    for bridge in parser:
        print("OK" if bridge.is_safe() else "NG")


if __name__ == "__main__":
    main()