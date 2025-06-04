from typing import List, Tuple, Dict, Set, Iterator
from collections import deque
from dataclasses import dataclass

class Position:
    def __init__(self, row: int, col: int):
        if not (0 <= row < 4 and 0 <= col < 4):
            raise ValueError("Position out of bounds")
        self.row = row
        self.col = col

    def __eq__(self, other):
        return isinstance(other, Position) and self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def move(self, dr: int, dc: int) -> 'Position':
        nr, nc = self.row + dr, self.col + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            return Position(nr, nc)
        else:
            return None

    def to_index(self) -> int:
        return self.row * 4 + self.col

    @staticmethod
    def from_index(idx: int) -> 'Position':
        return Position(idx // 4, idx % 4)

class Area:
    def __init__(self, idx: int):
        if not (0 <= idx < 16):
            raise ValueError("Area index out of range")
        self.idx = idx
        self.position = Position.from_index(idx)

    def row(self) -> int:
        return self.position.row

    def col(self) -> int:
        return self.position.col

    def __hash__(self):
        return hash(self.idx)

    def __eq__(self, other):
        return isinstance(other, Area) and self.idx == other.idx

class CloudPosition:
    def __init__(self, top_row: int, left_col: int):
        if not (0 <= top_row <= 2 and 0 <= left_col <= 2):
            raise ValueError("Cloud position out of range")
        self.top_row = top_row
        self.left_col = left_col

    def covered_areas(self) -> Set[int]:
        # Covered 2x2 areas indices
        covered = set()
        for dr in range(2):
            for dc in range(2):
                r = self.top_row + dr
                c = self.left_col + dc
                covered.add(r * 4 + c)
        return covered

    def possible_moves(self) -> Iterator['CloudPosition']:
        # Moves by 0, 1 or 2 in N, S, E, W, or no move
        # No diagonal moves allowed, movement is at beginning of day
        dirs = [(0,0),(1,0),(2,0),(-1,0),(-2,0),(0,1),(0,2),(0,-1),(0,-2)]
        for dr, dc in dirs:
            nr = self.top_row + dr
            nc = self.left_col + dc
            if 0 <= nr <= 2 and 0 <= nc <= 2:
                # no diagonal: dr and dc not both nonzero except (0,0)
                if (dr == 0 or dc == 0):
                    yield CloudPosition(nr, nc)

    def __eq__(self, other):
        return isinstance(other, CloudPosition) and self.top_row == other.top_row and self.left_col == other.left_col

    def __hash__(self):
        return hash((self.top_row, self.left_col))

@dataclass(frozen=True)
class State:
    day: int
    cloud_pos: CloudPosition
    # For each area, how many consecutive days without rain (0 to 6 max)
    # Stored as a tuple of length 16
    no_rain_counts: Tuple[int, ...]


class WeatherForecastProblem:
    def __init__(self, n_days: int, schedule: List[List[int]]):
        # schedule: daily list of 16 ints (0 or 1)
        self.n_days = n_days
        self.schedule = schedule
        # Precompute which areas require sun = market/festival == 1
        # and which require rain = 0
        # Actually, rain is required if no market/festival, and also in general we have the 6-days no rain max
        # We must never let an area be rainless for 7 full days

    def initial_state(self) -> State:
        # On day 0 (first day), rain under cloud fixed at 6,7,10,11 areas
        cloud_pos = CloudPosition(1, 2)  # The cloud on day 1 is in center 6,7,10,11 (0-based indices)
        # Initialize no_rain_counts:
        # All areas get rain or not:
        # Areas 6,7,10,11 under cloud: no_rain_counts=0
        # others: since day before period rains everywhere, they have 0 previous no-rain days.
        no_rain_counts = [0]*16
        covered = cloud_pos.covered_areas()
        for a in range(16):
            if a in covered:
                no_rain_counts[a] = 0
            else:
                no_rain_counts[a] = 0  # Because day before period rained everywhere (rain reset)
        return State(0, cloud_pos, tuple(no_rain_counts))

    def is_sunny(self, day: int, area_idx: int) -> bool:
        # Market or festival
        return self.schedule[day][area_idx] == 1

    def can_satisfy(self) -> int:
        # BFS or DP over days and states
        # state keys: day, cloud_pos, no_rain_counts
        # the no_rain_counts tuple length 16, values 0-6

        # We track visited states to avoid cycles
        visited: Set[State] = set()
        init_state = self.initial_state()
        queue = deque([init_state])

        while queue:
            state = queue.popleft()
            if state.day == self.n_days - 1:
                # If final day reached successfully, solution exists
                return 1

            next_day = state.day + 1

            # Try all cloud moves (including no move)
            for next_cloud_pos in state.cloud_pos.possible_moves():
                # update no_rain_counts
                new_counts = []
                covered = next_cloud_pos.covered_areas()
                # For each area i:
                for i in range(16):
                    rain_today = (i in covered)
                    # special initial condition day 0 done already
                    # We must check condition: areas with market/festival require sun today
                    # so these areas cannot be under rain cloud at that day
                    if self.is_sunny(next_day, i):
                        # must be sun => area i not under cloud at day i
                        if rain_today:
                            break  # invalid move: raining on market/festival day
                        new_counts.append(0)  # sun resets no_rain_counts to zero for rain? No, no rain increases count, so 0 days no rain resets no_rain counts? Actually no increment if sunny, but relevant is max 6 days no rain. The problem counts no rain consecutive days if no rain, so sunny days count as no rain ?
                    else:
                        # No market/festival -> area needs rain at least once every 7 days.
                        # We must not let no_rain_counts reach 7.
                        # If rain today, resets to 0
                        if rain_today:
                            new_counts.append(0)
                        else:
                            c = state.no_rain_counts[i] + 1
                            if c >= 7:
                                break  # fails max 6 days no rain constraint
                            new_counts.append(c)
                else:
                    # all areas ok: produce new state
                    new_state = State(next_day, next_cloud_pos, tuple(new_counts))
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
        return 0

class InputParser:
    def __init__(self):
        self.results = []

    def parse_and_solve(self):
        import sys

        while True:
            line = ''
            while line.strip() == '':
                line = sys.stdin.readline()
                if line == '':
                    return
            n = line.strip()
            if n == '0':
                break
            n_days = int(n)
            schedule = []
            read = 0
            while read < n_days:
                parts = []
                while len(parts) < 16:
                    l2 = sys.stdin.readline()
                    if l2 == '':
                        break
                    parts.extend(l2.strip().split())
                day_data = list(map(int, parts[:16]))
                schedule.append(day_data)
                read += 1
            problem = WeatherForecastProblem(n_days, schedule)
            answer = problem.can_satisfy()
            print(answer)

def main():
    parser = InputParser()
    parser.parse_and_solve()

if __name__ == '__main__':
    main()