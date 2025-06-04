from collections import deque
from typing import List, Tuple, Dict, Optional, Set, FrozenSet


class ParkingLineEnd:
    WEST = 'W'
    EAST = 'E'


class ParkingLine:
    def __init__(self, index: int, train: str):
        self.index = index
        self.train = train if train != '-' else ''

    def __str__(self):
        return self.train

    def is_empty(self):
        return len(self.train) == 0


class ExchangeLineEnd:
    def __init__(self, line_idx: int, end: str):
        self.line_idx = line_idx
        self.end = end

    def __hash__(self):
        return hash((self.line_idx, self.end))

    def __eq__(self, other):
        return (self.line_idx, self.end) == (other.line_idx, other.end)

    def __repr__(self):
        return f'{self.line_idx}{self.end}'


class ExchangeLine:
    def __init__(self, end1: ExchangeLineEnd, end2: ExchangeLineEnd):
        self.end1 = end1
        self.end2 = end2

    def connects(self, e: ExchangeLineEnd) -> Optional[ExchangeLineEnd]:
        if e == self.end1:
            return self.end2
        elif e == self.end2:
            return self.end1
        else:
            return None


class TrainState:
    def __init__(self, parking_lines: Tuple[str, ...]):
        self.parking_lines = parking_lines

    def __hash__(self):
        return hash(self.parking_lines)

    def __eq__(self, other):
        return self.parking_lines == other.parking_lines

    def __repr__(self):
        return str(self.parking_lines)


class TrainYard:
    def __init__(self, parking_lines: List[ParkingLine], exchange_lines: List[ExchangeLine]):
        self.parking_lines = parking_lines
        self.exchange_lines = exchange_lines

        # Map from each end to the list of connected ends for quick retrieval
        self.adj: Dict[ExchangeLineEnd, List[ExchangeLineEnd]] = {}
        for eline in exchange_lines:
            self.adj.setdefault(eline.end1, []).append(eline.end2)
            self.adj.setdefault(eline.end2, []).append(eline.end1)

    def get_possible_moves(self, state: TrainState) -> List[TrainState]:
        # Generates all possible states reachable from current state by one legal move
        result_states = []
        lines = list(state.parking_lines)
        n = len(lines)

        # We try for each parking line and for each end whether we can move some contiguous subtrain
        # to the connected lines.
        for from_idx in range(n):
            train = lines[from_idx]
            if len(train) == 0:
                continue
            # Possible splits: from 0 (whole train) up to len(train)-1 (last car alone)
            length = len(train)
            # A move can be done either from West end or East end
            # for each connected end, try sending either prefix or suffix subtrain
            # The direction of the train doesn't matter, but the cars order does.
            for side in [ParkingLineEnd.WEST, ParkingLineEnd.EAST]:
                from_end = ExchangeLineEnd(from_idx, side)

                if from_end not in self.adj:
                    continue
                connected_ends = self.adj[from_end]

                # Splits: the subtrain moved must be at the end side of the parking line as indicated
                # by the end (W means prefix of train, E means suffix)

                if side == ParkingLineEnd.WEST:
                    # subtrain is a prefix of length split_len
                    # We try all lengths 1..length to split off
                    for split_len in range(1, length + 1):
                        prefix = train[:split_len]
                        suffix = train[split_len:]
                        for to_end in connected_ends:
                            to_idx = to_end.line_idx
                            to_line_train = lines[to_idx]
                            # We attach the subtrain at 'to_end' side:
                            # If to_end is W, attach prefix of moved train at front
                            # If to_end is E, attach suffix of moved train at end

                            # Merging trains is concatenating strings; the end where we attach determines order
                            if to_end.end == ParkingLineEnd.WEST:
                                # Attach at west end: new train = moved train + old train
                                new_train = prefix + to_line_train
                            else:
                                # Attach at east end: new train = old train + moved train
                                new_train = to_line_train + prefix

                            # New state trains
                            new_lines = list(lines)
                            new_lines[from_idx] = suffix
                            new_lines[to_idx] = new_train

                            result_states.append(TrainState(tuple(new_lines)))
                else:
                    # side == EAST
                    # subtrain is a suffix of length split_len
                    for split_len in range(1, length + 1):
                        prefix = train[:length - split_len]
                        suffix = train[length - split_len:]
                        for to_end in connected_ends:
                            to_idx = to_end.line_idx
                            to_line_train = lines[to_idx]
                            if to_end.end == ParkingLineEnd.WEST:
                                new_train = suffix + to_line_train
                            else:
                                new_train = to_line_train + suffix

                            new_lines = list(lines)
                            new_lines[from_idx] = prefix
                            new_lines[to_idx] = new_train

                            result_states.append(TrainState(tuple(new_lines)))

        return result_states


class TrainReconfigurationSolver:
    def __init__(self, parking_lines: List[ParkingLine], exchange_lines: List[ExchangeLine],
                 initial_state: TrainState, target_state: TrainState):
        self.yard = TrainYard(parking_lines, exchange_lines)
        self.initial_state = initial_state
        self.target_state = target_state

    def solve(self) -> int:
        # BFS from initial_state to find minimal moves to target_state
        if self.initial_state == self.target_state:
            return 0

        visited: Set[TrainState] = set()
        queue = deque()
        queue.append((self.initial_state, 0))
        visited.add(self.initial_state)

        while queue:
            current_state, dist = queue.popleft()
            if dist >= 6:
                # According to problem, min moves between 1 and 6 inclusive,
                # We prune searches longer than 6.
                continue
            for next_state in self.yard.get_possible_moves(current_state):
                if next_state not in visited:
                    if next_state == self.target_state:
                        return dist + 1
                    visited.add(next_state)
                    queue.append((next_state, dist + 1))
        # According to problem, there's always a solution, so should never reach here
        return -1


def parse_exchange_line(line: str) -> Tuple[ExchangeLineEnd, ExchangeLineEnd]:
    # line like "0W 1W" or "0E 2W"
    parts = line.split()
    def make_end(s: str) -> ExchangeLineEnd:
        idx = int(s[:-1])
        end = s[-1]
        return ExchangeLineEnd(idx, end)
    return make_end(parts[0]), make_end(parts[1])


def process_dataset(x: int, y: int, exchange_lines_data: List[str],
                    arrival_data: List[str], departure_data: List[str]) -> int:
    # Parse parking lines (empty or string)
    parking_lines_arrival = [ParkingLine(i, line.strip()) for i, line in enumerate(arrival_data)]
    parking_lines_departure = [ParkingLine(i, line.strip()) for i, line in enumerate(departure_data)]

    exchange_lines = []
    for line in exchange_lines_data:
        e1, e2 = parse_exchange_line(line.strip())
        exchange_lines.append(ExchangeLine(e1, e2))

    initial_state = TrainState(tuple(pl.train for pl in parking_lines_arrival))
    target_state = TrainState(tuple(pl.train for pl in parking_lines_departure))

    solver = TrainReconfigurationSolver(parking_lines_arrival, exchange_lines, initial_state, target_state)
    min_moves = solver.solve()
    return min_moves


def main():
    import sys
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        line = input_lines[idx].strip()
        if line == '':
            idx += 1
            continue
        x_y = line.split()
        if len(x_y) != 2:
            idx += 1
            continue
        x, y = map(int, x_y)
        if x == 0 and y == 0:
            break
        idx += 1
        exchange_lines_data = []
        for _ in range(y):
            exchange_lines_data.append(input_lines[idx])
            idx += 1
        arrival_data = []
        for _ in range(x):
            arrival_data.append(input_lines[idx])
            idx += 1
        departure_data = []
        for _ in range(x):
            departure_data.append(input_lines[idx])
            idx += 1

        res = process_dataset(x, y, exchange_lines_data, arrival_data, departure_data)
        print(res)


if __name__ == '__main__':
    main()