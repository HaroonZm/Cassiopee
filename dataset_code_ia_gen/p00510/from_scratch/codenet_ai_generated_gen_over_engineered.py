class TunnelTrafficData:
    def __init__(self, initial_time: int, initial_cars: int):
        self._n = initial_time
        self._m = initial_cars
        self._interval_data = []

    def add_interval_data(self, entering: int, leaving: int):
        if not (0 <= entering <= 100 and 0 <= leaving <= 100):
            raise ValueError("車の台数は 0 以上 100 以下でなければなりません")
        self._interval_data.append((entering, leaving))

    @property
    def n(self):
        return self._n

    @property
    def initial_cars(self):
        return self._m

    @property
    def intervals(self):
        return self._interval_data


class TrafficAnalyzer:
    def __init__(self, traffic_data: TunnelTrafficData):
        self._data = traffic_data

    def calculate_max_cars_in_tunnel(self) -> int:
        cars_in_tunnel = self._data.initial_cars
        max_cars = cars_in_tunnel

        for i, (entered, left) in enumerate(self._data.intervals, 1):
            cars_in_tunnel += entered - left
            if cars_in_tunnel < 0:
                return 0
            max_cars = max(max_cars, cars_in_tunnel)
        return max_cars


class TunnelTrafficProcessor:
    def __init__(self, input_lines):
        self._input_lines = input_lines

    def process(self) -> int:
        n = int(self._input_lines[0].strip())
        m = int(self._input_lines[1].strip())

        traffic_data = TunnelTrafficData(n, m)

        for line in self._input_lines[2:2 + n]:
            entered_str, left_str = line.strip().split()
            entered, left = int(entered_str), int(left_str)
            traffic_data.add_interval_data(entered, left)

        analyzer = TrafficAnalyzer(traffic_data)
        return analyzer.calculate_max_cars_in_tunnel()


def main():
    import sys
    input_lines = sys.stdin.readlines()
    processor = TunnelTrafficProcessor(input_lines)
    result = processor.process()
    print(result)


if __name__ == "__main__":
    main()