import sys
import math
from typing import List, Tuple, Dict, Set, Optional, Iterator


class VelocitySegment:
    def __init__(self, start_time: int, vx: float, vy: float, end_time: Optional[int] = None):
        self.start_time = start_time
        self.vx = vx
        self.vy = vy
        self.end_time = end_time  # To be set later

    def __repr__(self):
        return f"Segment(t={self.start_time}..{self.end_time}, vx={self.vx}, vy={self.vy})"


class PositionSample:
    def __init__(self, time: int, x: float, y: float):
        self.time = time
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Pos(t={self.time}, x={self.x}, y={self.y})"


class RobotPath:
    def __init__(self, nickname: str, initial_pos: PositionSample, velocity_segments: List[VelocitySegment]):
        self.nickname = nickname
        self.initial_pos = initial_pos
        self.velocity_segments = velocity_segments
        self._set_end_times()

    def _set_end_times(self):
        # Make sure each velocity segment has end_time set properly
        for i in range(len(self.velocity_segments) - 1):
            self.velocity_segments[i].end_time = self.velocity_segments[i + 1].start_time
        if self.velocity_segments:
            self.velocity_segments[-1].end_time = None  # to be interpreted as last time in sim

    def position_at(self, t: float) -> Tuple[float, float]:
        # Locate relevant segment
        # t0 = initial_pos.time
        if t < self.initial_pos.time:
            return self.initial_pos.x, self.initial_pos.y  # no move before initial time
        pos_x, pos_y = self.initial_pos.x, self.initial_pos.y
        for i, seg in enumerate(self.velocity_segments):
            seg_end = seg.end_time
            if seg_end is None or t < seg_end:
                dt = t - seg.start_time
                # Position at seg.start_time:
                # Need to compute offset from initial pos using all previous velocity segments
                # We'll accumulate the increments from initial_pos to seg.start_time:
                pos_x_seg, pos_y_seg = self._position_at_segment_start(i)
                x = pos_x_seg + seg.vx * dt
                y = pos_y_seg + seg.vy * dt
                return (x, y)
        # If beyond all segments, keep last position
        last_seg = self.velocity_segments[-1]
        pos_x_seg, pos_y_seg = self._position_at_segment_start(len(self.velocity_segments) - 1)
        dt = (last_seg.end_time if last_seg.end_time is not None else t) - last_seg.start_time
        return pos_x_seg + last_seg.vx * dt, pos_y_seg + last_seg.vy * dt

    def _position_at_segment_start(self, seg_index: int) -> Tuple[float, float]:
        # Compute position at velocity_segments[seg_index].start_time
        # by summing displacements from initial_pos to that time using previous segments
        t = self.velocity_segments[seg_index].start_time
        pos_x = self.initial_pos.x
        pos_y = self.initial_pos.y
        prev_t = self.initial_pos.time
        for s in self.velocity_segments:
            if s.start_time >= t:
                break
            seg_end = s.end_time if s.end_time is not None else t
            duration = min(t, seg_end) - s.start_time
            if duration > 0:
                pos_x += s.vx * duration
                pos_y += s.vy * duration
            if seg_end >= t:
                break
        return pos_x, pos_y


class Robot:
    def __init__(self, path: RobotPath):
        self.path = path
        self.nickname = path.nickname

    def position_at(self, t: float) -> Tuple[float, float]:
        return self.path.position_at(t)

    def __repr__(self):
        return f"Robot({self.nickname})"


class CommunicationEvent:
    # Abstract the event of comm link between two robots appearing or disappearing at time t
    def __init__(self, time: float, robot1: Robot, robot2: Robot, status: bool):
        # status True means link started, False means link ended
        self.time = time
        self.robot1 = robot1
        self.robot2 = robot2
        self.status = status

    def __lt__(self, other):
        return self.time < other.time or (self.time == other.time and self.status and not other.status)

    def __repr__(self):
        return f"CommEvent(t={self.time:.8f}, pair=({self.robot1.nickname},{self.robot2.nickname}), status={'ON' if self.status else 'OFF'})"


class CommunicationNetwork:
    def __init__(self, robots: List[Robot], radius: float):
        self.robots = robots
        self.radius = radius
        self.N = len(robots)
        self.events: List[CommunicationEvent] = []
        self.links_state = [[False] * self.N for _ in range(self.N)]

    def build_events(self, T: int):
        # For every pair of robots, compute time intervals when distance <= radius, generate communication events
        eps = 1e-9
        for i in range(self.N):
            for j in range(i + 1, self.N):
                intervals = self._distance_intervals(self.robots[i], self.robots[j], T)
                # Intervals are list of (start, end) times where communication ON
                for (start, end) in intervals:
                    if start < T:
                        start_event = CommunicationEvent(start, self.robots[i], self.robots[j], True)
                        self.events.append(start_event)
                    if end <= T:
                        end_event = CommunicationEvent(end, self.robots[i], self.robots[j], False)
                        self.events.append(end_event)
        self.events.sort()

    def _distance_intervals(self, r1: Robot, r2: Robot, T: int) -> List[Tuple[float, float]]:
        # Compute intervals over [0,T] where dist(r1(t),r2(t)) <= radius
        # The movement is piecewise linear for each robot, so interval intersection is piecewise quadratic
        intervals: List[Tuple[float, float]] = []
        R = self.radius

        # Collect time breakpoints: union of segments breakpoints of both robots
        times_set = set()
        times_set.add(0)
        times_set.add(T)
        # segments start/end times for each robot
        def get_segment_boundaries(r: Robot) -> Iterator[int]:
            vsegs = r.path.velocity_segments
            yield r.path.initial_pos.time
            for seg in vsegs:
                yield seg.start_time
                if seg.end_time is not None:
                    yield seg.end_time
        times_set.update(t for t in get_segment_boundaries(r1) if 0 <= t <= T)
        times_set.update(t for t in get_segment_boundaries(r2) if 0 <= t <= T)
        times = sorted(times_set)

        # For each interval [times[k], times[k+1]), compute quadratic distance between two robots
        for k in range(len(times) - 1):
            start_t = times[k]
            end_t = times[k + 1]
            if end_t <= start_t:  # ignore empty or invalid intervals
                continue

            # Get v and x0,y0 of robots at start_t
            # We'll compute positions at start_t and velocities in this interval (constant)
            pos1_start = r1.position_at(start_t)
            pos2_start = r2.position_at(start_t)
            v1 = self._get_velocity_in_interval(r1.path, start_t)
            v2 = self._get_velocity_in_interval(r2.path, start_t)

            # Position difference at time t: (pos1_start + v1*(t - start_t)) - (pos2_start + v2*(t - start_t))
            # = (pos1_start - pos2_start) + (v1 - v2)*(t - start_t)
            dx0 = pos1_start[0] - pos2_start[0]
            dy0 = pos1_start[1] - pos2_start[1]
            dvx = v1[0] - v2[0]
            dvy = v1[1] - v2[1]

            # Distance squared = (dx0 + dvx * dt)^2 + (dy0 + dvy * dt)^2 <= R^2, dt = t - start_t
            # Quadratic in dt: a dt^2 + b dt + c <= R^2 with
            # d(t)^2 = (dx0^2 + 2*dx0*dvx*dt + dvx^2*dt^2) + (dy0^2 + 2*dy0*dvy*dt + dvy^2*dt^2)
            # = (dvx^2 + dvy^2)*dt^2 + 2*(dx0*dvx + dy0*dvy)*dt + (dx0^2 + dy0^2)
            a = dvx * dvx + dvy * dvy
            b = 2 * (dx0 * dvx + dy0 * dvy)
            c = dx0 * dx0 + dy0 * dy0 - R * R

            # Solve quadratic inequality: a*dt^2 + b*dt + c <= 0 (distance squared <= R^2)
            # and dt in [0, end_t - start_t]
            local_intervals = self._quadratic_inequality_intervals(a, b, c, 0.0, end_t - start_t)
            # Convert dt intervals to absolute time intervals
            for (dt_start, dt_end) in local_intervals:
                abs_start = start_t + dt_start
                abs_end = start_t + dt_end
                # Clip intervals to [0,T]
                if abs_end < 0 or abs_start > T:
                    continue
                abs_start = max(0.0, abs_start)
                abs_end = min(float(T), abs_end)
                if abs_start < abs_end:
                    intervals.append((abs_start, abs_end))
        # Merge overlapping intervals (might come from multiple pieces)
        intervals = self._merge_intervals(intervals)
        return intervals

    @staticmethod
    def _merge_intervals(intervals: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        if not intervals:
            return []
        intervals = sorted(intervals)
        merged = [intervals[0]]
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1] + 1e-14:
                merged[-1] = (last[0], max(last[1], current[1]))
            else:
                merged.append(current)
        return merged

    @staticmethod
    def _quadratic_inequality_intervals(a: float, b: float, c: float, left: float, right: float) -> List[Tuple[float, float]]:
        # Solve a x^2 + b x + c <= 0 for x in [left, right]
        # Returns list of intervals (start,end) inside domain satisfying inequality
        res = []
        # Handle constant case
        if abs(a) < 1e-14:
            # Linear or constant: bx + c <= 0
            if abs(b) < 1e-14:
                # c <= 0 constant inequality
                if c <= 0:
                    return [(left, right)]
                else:
                    return []
            else:
                sol = -c / b
                if b > 0:
                    # bx + c <= 0 => x <= sol
                    if sol >= left:
                        res.append((left, min(sol, right)))
                else:
                    # bx + c <= 0 => x >= sol
                    if sol <= right:
                        res.append((max(sol, left), right))
                return res
        # Quadratic case
        disc = b * b - 4 * a * c
        if disc < -1e-14:
            # No real roots
            if a > 0:
                # parabola opens upward
                # If c <= 0 at x=0, entire range may be <= 0 if c <= 0 at vertex? Let's check vertex minimum
                vertex = -b / (2 * a)
                value_at_vertex = a * vertex * vertex + b * vertex + c
                if value_at_vertex <= 0:
                    # Entire range or empty? Actually no roots, parabola always positive or always negative
                    # a>0 and no roots => always >0 or always <0 (if c>0, always >0)
                    # But c and vertex value disagree? theoretical no roots means positive always or negative always
                    # Here value_at_vertex ≤ 0 means negative parabola minimum ≤ 0, so entire parabola below x axis? No, because no roots.
                    # This generally won't happen, treat as no intervals
                    return []
                else:
                    return []
            else:
                # parabola opens downward
                vertex = -b / (2 * a)
                value_at_vertex = a * vertex * vertex + b * vertex + c
                if value_at_vertex <= 0:
                    return [(left, right)]
                else:
                    return []
        elif abs(disc) <= 1e-14:
            # One root
            root = -b / (2 * a)
            # Inequality ≤ 0 means ≤0 except maybe exactly root
            # So interval is one point? but intervals are open sets normally
            # We'll consider no interval or single-point intervals are negligible
            # So no interval for practical communication
            # Return empty
            return []
        else:
            sqrt_disc = math.sqrt(disc)
            r1 = (-b - sqrt_disc) / (2 * a)
            r2 = (-b + sqrt_disc) / (2 * a)
            if r1 > r2:
                r1, r2 = r2, r1
            if a > 0:
                # Between roots inequality ≤ 0
                low = max(left, r1)
                high = min(right, r2)
                if low < high:
                    res.append((low, high))
            else:
                # Outside roots inequality ≤ 0
                if left < r1:
                    res.append((left, min(r1, right)))
                if r2 < right:
                    res.append((max(r2, left), right))
            return res

    @staticmethod
    def _get_velocity_in_interval(path: RobotPath, t: float) -> Tuple[float, float]:
        # Return velocity (vx, vy) from velocity segments for time t (exact segment)
        for seg in path.velocity_segments:
            if seg.start_time <= t and (seg.end_time is None or t < seg.end_time):
                return seg.vx, seg.vy
        # If none found (after segments), use last segment velocity
        if path.velocity_segments:
            last = path.velocity_segments[-1]
            return last.vx, last.vy
        return 0.0, 0.0

    def simulate_spreading(self, T: int) -> Set[str]:
        # At time 0 only the first robot has data
        data_holders: Set[int] = {0}
        # Map nickname to index for convenience
        idx_map = {self.robots[i].nickname: i for i in range(self.N)}

        # Initially compute static links at t=0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                dist = self._distance_between(self.robots[i], self.robots[j], 0.0)
                if dist <= self.radius + 1e-12:
                    self.links_state[i][j] = True
                    self.links_state[j][i] = True

        # Apply transitive closure of initial connections (instantaneous communication)
        data_holders = self._spread_data_over_graph(data_holders, T=0)

        # Process events in time order to update links and propagate data dynamically
        for event in self.events:
            t = event.time
            if t > T + 1e-14:
                break
            i = self._robot_index(event.robot1.nickname)
            j = self._robot_index(event.robot2.nickname)
            self.links_state[i][j] = event.status
            self.links_state[j][i] = event.status
            data_holders = self._spread_data_over_graph(data_holders, time=t)

        # Return nicknames of robots who got initial robot's data by time T sorted dictionary order
        result = {self.robots[i].nickname for i in data_holders}
        return set(sorted(result))

    def _robot_index(self, nickname: str) -> int:
        for i, robot in enumerate(self.robots):
            if robot.nickname == nickname:
                return i
        raise KeyError(f"Robot with nickname {nickname} not found")

    def _spread_data_over_graph(self, data_holders: Set[int], T: float) -> Set[int]:
        # Since communication is instantaneous and wireless is symmetric,
        # data instantly propagate over connected components of the link graph at time T.

        # Build adjacency list from current links_state
        adjacency = [[] for _ in range(self.N)]
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if self.links_state[i][j]:
                    adjacency[i].append(j)
                    adjacency[j].append(i)

        # BFS starting from data_holders to propagate data
        queue = list(data_holders)
        known = set(data_holders)
        while queue:
            u = queue.pop()
            for w in adjacency[u]:
                if w not in known:
                    known.add(w)
                    queue.append(w)
        return known

    @staticmethod
    def _distance_between(r1: Robot, r2: Robot, t: float) -> float:
        x1, y1 = r1.position_at(t)
        x2, y2 = r2.position_at(t)
        return math.hypot(x1 - x2, y1 - y2)


class InputParser:
    def __init__(self, lines: Iterator[str]):
        self.lines = lines

    def parse_dataset(self) -> Optional[Tuple[int, int, int, List[Robot]]]:
        # Read N T R
        while True:
            try:
                line = next(self.lines)
            except StopIteration:
                return None
            if not line.strip():
                continue
            if line.count(' ') < 2:
                # partial or invalid, skip or unexpected
                continue
            NTR = line.strip().split()
            if len(NTR) != 3:
                continue
            N, T, R =