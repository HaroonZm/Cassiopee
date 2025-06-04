class Position:
    __slots__ = ('x', 'y')
    def __init__(self, x:int, y:int): self.x, self.y = x, y
    def __eq__(self, other): return (self.x, self.y) == (other.x, other.y)
    def __hash__(self): return hash((self.x, self.y))
    def __add__(self, other): return Position(self.x + other.x, self.y + other.y)
    def is_within_bounds(self) -> bool: return 0 <= self.x <= 9 and 0 <= self.y <= 9

class JumpSet:
    def __init__(self, deltas):
        self.moves = [Position(dx, dy) for (dx, dy) in deltas]
    def next_positions(self, pos):
        for m in self.moves:
            np = pos + m
            if np.is_within_bounds():
                yield np

class Sprinkler:
    def __init__(self, pos:Position):
        self.pos = pos
        self.coverage = self.calc_coverage()
    def calc_coverage(self):
        # Around position, range is self plus 8 neighbours (up to 9 pos)
        neighbors = [Position(dx, dy) for dx in [-1,0,1] for dy in [-1,0,1]]
        return {self.pos + n for n in neighbors if (self.pos + n).is_within_bounds()}
    def covers(self, pos:Position) -> bool:
        return pos in self.coverage

class SprinklerSequence:
    def __init__(self, sprinklers):
        self.sprinklers = sprinklers
    def length(self): return len(self.sprinklers)
    def sprinkler_at(self, idx): return self.sprinklers[idx]

class PyonkichiMovementModel:
    # Jump pattern fixed as in problem
    def __init__(self):
        # From diagram (b) jump range: manhattan 3 with no intermediate, deltas:
        deltas = [
            (+3,0), (-3,0), (0,+3), (0,-3),
            (+2,+2), (+2,-2), (-2,+2), (-2,-2)
        ]
        self.jumps = JumpSet(deltas)
    def valid_moves(self, pos): return self.jumps.next_positions(pos)

class SurvivalSolver:
    def __init__(self, initial_pos:Position, sprinklers_positions):
        self.initial_pos = initial_pos
        self.sprinkler_seq = SprinklerSequence([Sprinkler(Position(x,y)) for x,y in sprinklers_positions])
        self.movement_model = PyonkichiMovementModel()
        self.cache = {}
    def can_survive(self):
        # We assume a path for p steps (number of sprinklers)
        # State (pos, idx): idx = which sprinkler is running
        # On sprinkler i: pyonkichi must be in coverage of sprinkler i
        # Once sprinkler i stops and i+1 starts,
        # He can jump once to a position that covers next sprinkler i+1 coverage.
        return self._dfs(self.initial_pos, 0, True)
    def _dfs(self, pos, idx, must_jump):
        if idx == self.sprinkler_seq.length():
            # All sprinklers done, survived
            return True
        key = (pos.x, pos.y, idx, must_jump)
        if key in self.cache:
            return self.cache[key]
        current_sprinkler = self.sprinkler_seq.sprinkler_at(idx)
        if must_jump:
            # Must jump once now to a coverage of current sprinkler
            for next_pos in self.movement_model.valid_moves(pos):
                if current_sprinkler.covers(next_pos):
                    # After jump, pyonkichi stays there until sprinkler stops
                    if self._dfs(next_pos, idx, False):
                        self.cache[key] = True
                        return True
            self.cache[key] = False
            return False
        else:
            # Wait until sprinkler stops, check if current pos is covered
            if not current_sprinkler.covers(pos):
                self.cache[key] = False
                return False
            # Next sprinkler starts, must jump once to coverage of next sprinkler or end if last
            result = self._dfs(pos, idx+1, True)
            self.cache[key] = result
            return result

def readints():
    return list(map(int, input().split()))

def main():
    import sys
    inputiter = iter(sys.stdin.read().strip().split('\n'))
    while True:
        try:
            px_py = next(inputiter)
        except StopIteration:
            break
        if not px_py.strip():
            break
        px, py = map(int, px_py.split())
        if px == 0 and py == 0:
            break
        n = int(next(inputiter))
        coords_line = next(inputiter).strip()
        coords = list(map(int, coords_line.split()))
        sprinklers_positions = [(coords[i], coords[i+1]) for i in range(0, 2*n, 2)]
        # According to problem, initial jump is on sprinkler 1 (index 0) start
        # So in model, must_jump=True at idx=0 state
        solver = SurvivalSolver(Position(px, py), sprinklers_positions)
        print("OK" if solver.can_survive() else "NA")

if __name__ == "__main__":
    main()