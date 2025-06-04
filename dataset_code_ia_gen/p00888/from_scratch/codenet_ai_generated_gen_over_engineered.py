import math
from typing import List, Tuple, Optional, Dict


class Point:
    def __init__(self, x: float, y: float):
        self.x = x  # horizontal distance along the route from start
        self.y = y  # altitude relative to start

    def distance_to(self, other: "Point") -> float:
        # Euclidean distance on the surface
        return math.hypot(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


class RouteSegment:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.length = self.start.distance_to(self.end)

    def point_at(self, t: float) -> Point:
        # linear interpolation along segment for t in [0,1]
        x = self.start.x + t * (self.end.x - self.start.x)
        y = self.start.y + t * (self.end.y - self.start.y)
        return Point(x, y)

    def __repr__(self):
        return f"RouteSegment(start={self.start}, end={self.end}, length={self.length})"


class Route:
    def __init__(self, points: List[Point]):
        self.points = points
        self.segments: List[RouteSegment] = []
        self.lengths_prefix: List[float] = [0.0]
        self.total_length: float = 0.0
        self._build()

    def _build(self):
        # create segments and prefix sums of lengths
        for i in range(len(self.points) - 1):
            seg = RouteSegment(self.points[i], self.points[i + 1])
            self.segments.append(seg)
            self.lengths_prefix.append(self.lengths_prefix[-1] + seg.length)
        self.total_length = self.lengths_prefix[-1]

    def point_at_distance(self, d: float) -> Point:
        # locate the segment for distance d and return the point on the route
        if d < 0:
            return self.points[0]
        if d >= self.total_length:
            return self.points[-1]
        # binary search segment
        left, right = 0, len(self.segments) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.lengths_prefix[mid] <= d < self.lengths_prefix[mid + 1]:
                seg = self.segments[mid]
                t = (d - self.lengths_prefix[mid]) / seg.length
                return seg.point_at(t)
            elif d < self.lengths_prefix[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # fallback
        return self.points[-1]

    def altitude_at_distance(self, d: float) -> float:
        return self.point_at_distance(d).y


class MeetingAttemptSolver:
    def __init__(self, route: Route):
        self.route = route
        self.memo: Dict[Tuple[float, float], Optional[float]] = dict()
        # discretization tolerance for DP states
        self.eps = 1e-6
        # We solve on distances dA and dB from each start (0 -> total_length)
        self.L = self.route.total_length

    def altitude_equal(self, dA: float, dB: float) -> bool:
        # Check if altitudes are equal at respective distances (from respective ends)
        # dA measured from start point (x1,y1 = 0,0)
        # dB measured from end point backward, so route.L - dB from start
        altA = self.route.altitude_at_distance(dA)
        altB = self.route.altitude_at_distance(self.L - dB)
        return math.isclose(altA, altB, abs_tol=1e-9)

    def next_positions(self, dA: float, dB: float) -> List[Tuple[float, float]]:
        # Generate possible moves for both climbers:
        # each can move forward (+small step) or backward (-small step) along the route,
        # but distances must stay in [0, L].
        # However problem states climbers start at ends (0 and L) and cannot be below ground,
        # but they can move back and forth while keeping altitudes equal.
        #
        # To prevent infinite states, we consider a finite set of candidate positions.
        # We take all points of the route as possible stops.
        # We allow only moves to points with equal altitudes on both legs.
        #
        # The problem asks for minimal sum length of moves until meeting at same point.
        # The two climbers start at 0 and L respectively (in distance measure),
        # and must eventually meet at some distance d where d == L - d (=> d = L/2),
        # or more generally at same physical point on route,
        # which means their positions must correspond after reverse path for climber B.
        #
        # We try all road points and their reverse corresponding points,
        # and moves are between discrete points on the route.
        #
        # So next positions here generate all pairs (dA', dB') where dA' and dB' are points on route,
        # with altitude equal, and reachable from dA and dB by moving forward/backward along route.
        #
        # To not explode search space, we limit to route points + current positions.
        #
        candidates = []
        route_points_distances = self.route.lengths_prefix  # distances of all points

        # Prepare list of candidate dA and dB points
        possible_dA = []
        for dist in route_points_distances:
            if dist < -self.eps or dist > self.L + self.eps:
                continue
            if abs(dist - dA) > self.eps:  # allow standing still?
                possible_dA.append(dist)
        possible_dA.append(dA)  # allow standing still

        possible_dB = []
        for dist in route_points_distances:
            if dist < -self.eps or dist > self.L + self.eps:
                continue
            if abs(dist - dB) > self.eps:
                possible_dB.append(dist)
        possible_dB.append(dB)

        # Generate pairs where altitudes match
        for ndA in possible_dA:
            for ndB in possible_dB:
                if abs(ndA - dA) < self.eps and abs(ndB - dB) < self.eps:
                    continue  # skip no move
                # check if from current positions can move directly to these
                # moves along route must be continuous without gaps:
                # we allow forward/backward moves along route segments,
                # so if the difference is > segment length, we disallow
                # but for complexity, allow moves only to route points for now.
                # Also allow standing still for one and move in other?

                # Limit moves to steps (from current position) no bigger than max segment ~ max 1000 length 
                # but better limit to segment adjacents
                # So moves allowed only to neighbors on route or stay still.

                # Check neighbors of dA and dB in route points:
                neighbors_dA = []
                idxA = None
                for i, dist in enumerate(route_points_distances):
                    if abs(dist - dA) < self.eps:
                        idxA = i
                        break
                if idxA is None:
                    continue
                if idxA > 0:
                    neighbors_dA.append(route_points_distances[idxA - 1])
                neighbors_dA.append(route_points_distances[idxA])
                if idxA < len(route_points_distances) - 1:
                    neighbors_dA.append(route_points_distances[idxA + 1])

                neighbors_dB = []
                idxB = None
                for i, dist in enumerate(route_points_distances):
                    if abs(dist - dB) < self.eps:
                        idxB = i
                        break
                if idxB is None:
                    continue
                if idxB > 0:
                    neighbors_dB.append(route_points_distances[idxB - 1])
                neighbors_dB.append(route_points_distances[idxB])
                if idxB < len(route_points_distances) - 1:
                    neighbors_dB.append(route_points_distances[idxB + 1])

                if ndA not in neighbors_dA:
                    continue
                if ndB not in neighbors_dB:
                    continue

                # Check altitudes equal at ndA and ndB positions
                # Remember climber B pos dB is distance from end, so invert for altitude check:
                altA = self.route.altitude_at_distance(ndA)
                altB = self.route.altitude_at_distance(self.L - ndB)
                if abs(altA - altB) < 1e-9:
                    candidates.append((ndA, ndB))
        return candidates

    def solve(self) -> float:
        # The problem is to find minimal sum of lengths of moves until climbers meet at a point.
        # Possible meeting points correspond to distance dA == L - dB (i.e., same physical point)
        # and same altitude.
        #
        # We represent state as (dA, dB) with distances from each start point.
        # Start: (0, 0)
        # End: any position where dA == dB and altitude equal = where climbers physically meet.
        #
        # We'll do Dijkstra-like shortest path on states:
        # nodes = pairs (dA,dB), edges = moves to neighboring positions preserving altitude equality.
        #
        # To keep complexity manageable, states are discrete distance points = route vertices only.
        #
        # Initialize queue and distances dictionary.
        import heapq

        start = (0.0, 0.0)
        dist_map: Dict[Tuple[float, float], float] = {start: 0.0}
        heap = [(0.0, start)]

        route_points = self.route.lengths_prefix
        # Precompute all candidate states: pairs of route points (dA,dB) where altitudes equal
        candidates_states = []
        altitude_map = {}
        for dA in route_points:
            altitude_map[dA] = self.route.altitude_at_distance(dA)
        for dB in route_points:
            altitude_map[dB + self.L + 1] = self.route.altitude_at_distance(self.L - dB)
        candidate_pairs = []
        for dA in route_points:
            altA = altitude_map[dA]
            for dB in route_points:
                altB = altitude_map[dB + self.L + 1]
                if abs(altA - altB) < 1e-9:
                    candidate_pairs.append((dA, dB))

        # For quick neighbors lookup, create a set of all pairs for fast membership check
        candidate_set = set(candidate_pairs)

        # Precompute neighbors for each dA and dB point (route points neighbors)
        neighbors_map = {}
        for i, d in enumerate(route_points):
            neighbors = []
            if i > 0:
                neighbors.append(route_points[i - 1])
            neighbors.append(d)
            if i < len(route_points) - 1:
                neighbors.append(route_points[i + 1])
            neighbors_map[d] = neighbors

        while heap:
            cur_dist, (dA, dB) = heapq.heappop(heap)
            # If dA==dB and altitudes equal => meeting point
            if abs(dA - dB) < 1e-9:
                # They meet physically same point
                return cur_dist

            if dist_map[(dA, dB)] < cur_dist - 1e-15:
                continue

            # try all neighbors of dA and dB from candidates that preserve altitude equality
            for ndA in neighbors_map[dA]:
                for ndB in neighbors_map[dB]:
                    if (ndA, ndB) in candidate_set:
                        # cost is sum of distances moved by each climber along the route surface
                        cost = self.route.point_at_distance(dA).distance_to(self.route.point_at_distance(ndA)) + \
                               self.route.point_at_distance(self.L - dB).distance_to(self.route.point_at_distance(self.L - ndB))
                        next_dist = cur_dist + cost
                        if (ndA, ndB) not in dist_map or dist_map[(ndA, ndB)] > next_dist + 1e-15:
                            dist_map[(ndA, ndB)] = next_dist
                            heapq.heappush(heap, (next_dist, (ndA, ndB)))

        # theoretically unreachable if input guaranteed solvable
        return float('inf')


class InputReader:
    def __init__(self):
        pass

    def read_datasets(self) -> List[Route]:
        routes = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line.strip() == '':
                continue
            n = int(line)
            if n == 0:
                break
            points = []
            for _ in range(n):
                x, y = map(int, input().split())
                points.append(Point(x, y))
            routes.append(Route(points))
        return routes


class OutputWriter:
    def __init__(self):
        pass

    def write_results(self, results: List[float]) -> None:
        for res in results:
            # output with no more than 0.01 error
            print(f"{res:.10f}".rstrip('0').rstrip('.') if '.' in f"{res:.10f}" else f"{res:.10f}")


def main():
    reader = InputReader()
    routes = reader.read_datasets()
    solver_results = []
    for route in routes:
        solver = MeetingAttemptSolver(route)
        result = solver.solve()
        solver_results.append(result)
    writer = OutputWriter()
    writer.write_results(solver_results)


if __name__ == "__main__":
    main()