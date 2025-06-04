class BusStop:
    def __init__(self, number: int):
        self.number = number
        self.connected_forward = None
        self.connected_backward = None

    def __repr__(self):
        return f"BusStop({self.number})"

class CircularRoute:
    def __init__(self, stops):
        self.stops = stops
        n = len(stops)
        for i, stop in enumerate(stops):
            stop.connected_forward = stops[(i + 1) % n]
            stop.connected_backward = stops[(i - 1) % n]

    def shortest_path(self, start: BusStop, end: BusStop):
        if start == end:
            return [start.number]
        # Travel forwards
        path_fw = []
        current = start
        while True:
            path_fw.append(current.number)
            if current == end:
                break
            current = current.connected_forward
        # Travel backwards
        path_bw = []
        current = start
        while True:
            path_bw.append(current.number)
            if current == end:
                break
            current = current.connected_backward
        if len(path_fw) <= len(path_bw):
            return path_fw
        else:
            return path_bw

class LineSegment:
    def __init__(self, stops):
        self.stops = stops
        # Link stops in linear fashion
        for i in range(len(stops) -1):
            stops[i].connected_forward = stops[i+1]
            stops[i+1].connected_backward = stops[i]

    def path_forward(self, start: BusStop, end: BusStop):
        path = []
        current = start
        while True:
            path.append(current.number)
            if current == end:
                break
            current = current.connected_forward
        return path

    def path_backward(self, start: BusStop, end: BusStop):
        path = []
        current = start
        while True:
            path.append(current.number)
            if current == end:
                break
            current = current.connected_backward
        return path

    def shortest_path(self, start: BusStop, end: BusStop):
        # Check direction: forward if start < end
        # backward otherwise
        if start.number <= end.number:
            return self.path_forward(start,end)
        else:
            return self.path_backward(start,end)

class BusNetwork:
    def __init__(self):
        # Create all 10 stops
        self.stops = {i: BusStop(i) for i in range(10)}

        # Create main linear route from 0 to 5 with turnaround at 0
        linear_stops = [self.stops[i] for i in range(6)]
        self.linear_route = LineSegment(linear_stops)

        # Create circular route 5->6->7->8->9->5
        circular_stops = [self.stops[i] for i in range(5,10)]
        self.circular_route = CircularRoute(circular_stops)

        # Special handlings:
        # At stop 0: only turnaround, no backward stop
        self.stops[0].connected_forward = self.stops[1]
        self.stops[0].connected_backward = None

        # At stop 5: belongs to both linear and circular routes
        # For linear route 5 connected backward to 4
        # For circular route 5 connected forward to 6 and backward to 9
        # We will manage connections accordingly later as needed

    def get_route_for_trip(self, start_num: int, end_num: int):
        start = self.stops[start_num]
        end = self.stops[end_num]

        # Define range sets for areas:
        # Linear: 0-5
        # Circular: 5-9

        in_linear = lambda x: 0 <= x <=5
        in_circular = lambda x: 5 <= x <= 9

        # Cases

        # Case 0: both start and end in 0-5 (linear section)
        if in_linear(start_num) and in_linear(end_num):
            # From stops 1-5, both directions possible, choose shortest path on line
            # since line is linear, path forward or backward:
            # if start < end: go forward else backward
            path = self.linear_route.shortest_path(start, end)
            return path

        # Case 1: both start and end in 5-9 (circular section)
        elif in_circular(start_num) and in_circular(end_num):
            # shortest path on circular route
            path = self.circular_route.shortest_path(start, end)
            return path

        # Case 2: start in 0-5 and end in 5-9
        elif in_linear(start_num) and in_circular(end_num):
            # Need to pass through 5, switching from linear to circular at 5

            # From start to 5 on linear route
            path_to_5 = self.linear_route.shortest_path(start, self.stops[5])

            # From 5 to end on circular route
            path_5_to_end = self.circular_route.shortest_path(self.stops[5], end)

            # Concatenate but remove duplicate 5
            full_path = path_to_5 + path_5_to_end[1:]
            return full_path

        # Case 3: start in 5-9 and end in 0-5
        elif in_circular(start_num) and in_linear(end_num):
            # Need to pass through 5, switching from circular to linear at 5

            # From start to 5 on circular route
            path_start_to_5 = self.circular_route.shortest_path(start, self.stops[5])

            # From 5 to end on linear route
            path_5_to_end = self.linear_route.shortest_path(self.stops[5], end)

            # Combine removing duplicate 5
            full_path = path_start_to_5 + path_5_to_end[1:]
            return full_path

        else:
            raise ValueError("Invalid stop numbers")

def main():
    import sys
    input = sys.stdin.readline
    bus_network = BusNetwork()

    n = int(input())
    for _ in range(n):
        s, e = map(int, input().split())
        path = bus_network.get_route_for_trip(s, e)
        print(" ".join(map(str,path)))

if __name__ == "__main__":
    main()