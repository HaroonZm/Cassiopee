class TunnelTrafficObserver:
    class TunnelState:
        def __init__(self, initial_count: int):
            self.current_count = initial_count
            self.max_count = initial_count

        def update(self, entered: int, exited: int) -> bool:
            self.current_count += entered - exited
            if self.current_count < 0:
                return False
            if self.current_count > self.max_count:
                self.max_count = self.current_count
            return True

        def get_max_count(self) -> int:
            return self.max_count

    class TrafficDataProvider:
        def __init__(self, n: int, m: int, traffic_flow: list):
            self.n = n
            self.m = m
            self.traffic_flow = traffic_flow  # List of tuples (entered, exited)

        @classmethod
        def from_input(cls):
            import sys
            input_stream = sys.stdin
            n = int(input_stream.readline())
            m = int(input_stream.readline())
            traffic_flow = []
            for _ in range(n):
                entry, exit = map(int, input_stream.readline().split())
                traffic_flow.append((entry, exit))
            return cls(n, m, traffic_flow)

        def __iter__(self):
            return iter(self.traffic_flow)

    class TrafficAnalyzer:
        def __init__(self, data_provider: 'TunnelTrafficObserver.TrafficDataProvider'):
            self.data_provider = data_provider
            self.tunnel_state = TunnelTrafficObserver.TunnelState(self.data_provider.m)

        def analyze(self) -> int:
            for entered, exited in self.data_provider:
                if not self.tunnel_state.update(entered, exited):
                    return 0
            return self.tunnel_state.get_max_count()

    def __init__(self):
        self.data_provider = self.TrafficDataProvider.from_input()
        self.analyzer = self.TrafficAnalyzer(self.data_provider)

    def run(self):
        result = self.analyzer.analyze()
        print(result)


if __name__ == '__main__':
    TunnelTrafficObserver().run()