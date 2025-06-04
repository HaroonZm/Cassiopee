class RouterId:
    def __init__(self, id_value: int):
        self.id_value = id_value

    def __eq__(self, other):
        if isinstance(other, RouterId):
            return self.id_value == other.id_value
        return False

    def __hash__(self):
        return hash(self.id_value)

    def __repr__(self):
        return f"RouterId({self.id_value})"


class Packet:
    def __init__(self, source: RouterId, destination: RouterId, ttl: int):
        self.source = source
        self.destination = destination
        self.ttl = ttl


class Network:
    def __init__(self, size: int):
        self.size = size
        self.adjacency = {RouterId(i): [] for i in range(1, size + 1)}

    def add_connection(self, from_router: RouterId, to_router: RouterId):
        self.adjacency[from_router].append(to_router)

    def shortest_path_length(self, start: RouterId, goal: RouterId) -> int | None:
        # Returns the minimal number of routers traversed from start to goal including start and goal
        from collections import deque

        queue = deque([(start, 1)])  # store (current_router, count of routers so far)
        visited = {start}

        while queue:
            current, length = queue.popleft()
            if current == goal:
                return length
            for neighbor in self.adjacency.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, length + 1))
        return None


class PacketRouter:
    def __init__(self, network: Network):
        self.network = network

    def minimal_hops_for_packet(self, packet: Packet) -> str:
        # Calculate minimal hops from packet.source to packet.destination
        path_len = self.network.shortest_path_length(packet.source, packet.destination)
        if path_len is None:
            return "NA"

        # TTL must be at least path_len - 1 to reach destination because TTL is decremented at each router
        # except the destination router (no decrement at destination).
        # The number of routers traveled includes both source and destination.
        ttl_needed = path_len - 1
        if packet.ttl >= ttl_needed:
            return str(path_len)
        else:
            return "NA"


class InputParser:
    @staticmethod
    def parse_input() -> tuple[Network, list[Packet]]:
        import sys
        input_iter = iter(sys.stdin.read().strip().split())
        n = int(next(input_iter))
        network = Network(n)
        for _ in range(n):
            r = RouterId(int(next(input_iter)))
            k = int(next(input_iter))
            for _ in range(k):
                to_id = RouterId(int(next(input_iter)))
                network.add_connection(r, to_id)

        p = int(next(input_iter))
        packets = []
        for _ in range(p):
            s = RouterId(int(next(input_iter)))
            d = RouterId(int(next(input_iter)))
            v = int(next(input_iter))
            packets.append(Packet(s, d, v))
        return network, packets


class OutputHandler:
    @staticmethod
    def output_results(results: list[str]) -> None:
        for res in results:
            print(res)


def main():
    network, packets = InputParser.parse_input()
    router = PacketRouter(network)
    results = [router.minimal_hops_for_packet(packet) for packet in packets]
    OutputHandler.output_results(results)


if __name__ == "__main__":
    main()