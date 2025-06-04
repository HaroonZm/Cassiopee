class TrapType:
    def __init__(self, symbol: str, damage: int):
        self.symbol = symbol
        self.damage = damage

class Potion:
    def __init__(self, heal_amount: int):
        self.heal_amount = heal_amount

class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
    def move(self, direction: str):
        moves = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
        dr, dc = moves[direction]
        return Position(self.row + dr, self.col + dc)
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    def __hash__(self):
        return hash((self.row, self.col))

class Cave:
    def __init__(self, rows, cols, layout, trap_types):
        self.rows = rows
        self.cols = cols
        self.layout = layout  # List[List[str]] trap symbol at each cell
        self.trap_types = trap_types  # dict symbol -> TrapType

    def get_trap_damage(self, pos: Position) -> int:
        trap_symbol = self.layout[pos.row][pos.col]
        if trap_symbol in self.trap_types:
            return self.trap_types[trap_symbol].damage
        return 0

class PatrolStep:
    def __init__(self, direction: str, distance: int):
        self.direction = direction
        self.distance = distance

class Agent:
    def __init__(self, hp_init: int, hp_max: int, potions):
        self.hp_max = hp_max
        self.hp = hp_init
        self.potions = potions  # list of Potion objects
    def use_potions(self, needed_hp_loss: int):
        # Before stepping into a trap cell with damage needed_hp_loss, try to heal optimally using potions
        # Since agent can use any combination of potions any number of times (with restrictions?), 
        # but problem states only "more than one type at once", no limit on count of potions use is specified.
        # So we can use each potion at most once per cell? Problem does not specify usage restrictions, so assume each potion can be used once per cell step.
        # Because number of potions is small (<=12), we try all subsets to maximize healing but only to just cover damage.
        # Goal: maximize healing without exceeding hp_max or over-heal unnecessarily.

        # We want to pick subset of potions (once each max) summing healing h so that hp + h - damage > 0
        # Or hp + h > damage

        # We try from minimal needed healing upward to minimal subset sum that covers needed.

        # But also must not exceed hp_max.

        # We'll consider subsets with pruning to not exceed hp_max.

        from itertools import combinations
        pot_heals = [p.heal_amount for p in self.potions]
        # If no potions, just skip
        if not pot_heals:
            return
        max_healing = 0
        best_subset = []
        # Generate all subsets; up to 2^P where P<=12, feasible
        n = len(pot_heals)
        for r in range(1, n+1):
            for combi in combinations(range(n), r):
                heal_sum = sum(pot_heals[i] for i in combi)
                # can't heal beyond hp_max
                if self.hp + heal_sum > self.hp_max:
                    heal_sum = self.hp_max - self.hp  # effective healing max
                # if after healing the hp is enough to survive damage:
                if self.hp + heal_sum > needed_hp_loss:
                    # pick minimal healing that allows survive but maximizes hp after
                    # but problem is just to survive, so pick minimal healing that make hp+heal > damage
                    if max_healing == 0 or heal_sum < max_healing:
                        max_healing = heal_sum
                        best_subset = combi
        if max_healing > 0:
            # apply the best healing
            self.hp += max_healing
            if self.hp > self.hp_max:
                self.hp = self.hp_max

class PatrolRoute:
    def __init__(self, steps):
        self.steps = steps  # list of PatrolStep
    def expand_path(self, start_pos: Position):
        path = []
        current = start_pos
        for step in self.steps:
            for _ in range(step.distance):
                current = current.move(step.direction)
                path.append(current)
        return path

class DungeonQuestII:
    def __init__(self):
        self.datasets = []

    def read_dataset(self, input_lines):
        # parse one dataset from input_lines iterator, return None if termination line encountered
        hp_init_max = next(input_lines).strip()
        if hp_init_max == '0 0':
            return None
        hp_init, hp_max = map(int, hp_init_max.split())
        R, C = map(int, next(input_lines).split())
        layout = [list(next(input_lines).rstrip('\n')) for _ in range(R)]
        T = int(next(input_lines))
        trap_types = {}
        for _ in range(T):
            line = next(input_lines).split()
            symbol = line[0]
            damage = int(line[1])
            trap_types[symbol] = TrapType(symbol, damage)
        S = int(next(input_lines))
        steps = []
        for _ in range(S):
            direction, n = next(input_lines).split()
            steps.append(PatrolStep(direction, int(n)))
        P = int(next(input_lines))
        potions = []
        for _ in range(P):
            pval = int(next(input_lines))
            potions.append(Potion(pval))
        return hp_init, hp_max, R, C, layout, trap_types, steps, potions

    def judge_patrol(self, hp_init, hp_max, R, C, layout, trap_types, steps, potions) -> str:
        cave = Cave(R, C, layout, trap_types)
        agent = Agent(hp_init, hp_max, potions)
        route = PatrolRoute(steps)
        start_pos = Position(0,0)
        # Must note: top-left corner has no traps guaranteed
        # path is all cells stepped on after each move
        path = route.expand_path(start_pos)

        # For each cell stepped into, agent uses potions before stepping in. If hp <=0 dies.
        for pos in path:
            damage = cave.get_trap_damage(pos)
            agent.use_potions(damage)
            # take damage
            agent.hp -= damage
            if agent.hp <= 0:
                return "NO"
        return "YES"

    def run(self):
        import sys
        input_lines = iter(sys.stdin.readline, '')
        # Python readline iterator stops at '' (empty), not at EOF, so wrap input
        # We'll use sys.stdin as iterable lines, stopping at "0 0"

        lines_buffer = []
        for line in sys.stdin:
            lines_buffer.append(line)
        input_lines = iter(lines_buffer)

        while True:
            dataset = self.read_dataset(input_lines)
            if dataset is None:
                break
            hp_init, hp_max, R, C, layout, trap_types, steps, potions = dataset
            result = self.judge_patrol(hp_init, hp_max, R, C, layout, trap_types, steps, potions)
            print(result)

if __name__ == "__main__":
    game = DungeonQuestII()
    game.run()