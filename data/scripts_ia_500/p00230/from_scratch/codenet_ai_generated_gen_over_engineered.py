class WallType:
    NORMAL = 0
    LADDER = 1
    SLIPPERY = 2

class Building:
    def __init__(self, floors, walls):
        self.floors = floors
        self.walls = walls

    def wall_type(self, floor):
        # floor is 1-based index
        return self.walls[floor-1]

class NinjaPosition:
    def __init__(self, building_index, floor):
        self.building_index = building_index
        self.floor = floor

    def __hash__(self):
        return hash((self.building_index, self.floor))

    def __eq__(self, other):
        return (self.building_index, self.floor) == (other.building_index, other.floor)

class JumpRule:
    def __init__(self, max_floor):
        self.max_floor = max_floor

    def possible_destinations(self, current_pos):
        # jumps from current_pos to opposite building
        opp_building = 1 - current_pos.building_index
        candidates = []
        for diff in (0, 1, 2):
            nf = current_pos.floor + diff
            if nf <= self.max_floor:
                candidates.append(NinjaPosition(opp_building, nf))
        return candidates

class WallEffectResolver:
    def __init__(self, buildings):
        self.buildings = buildings
        self.max_floor = buildings[0].floors

    def resolve(self, pos):
        # resolve wall effects to single final position after landing
        visited = set()
        current = pos
        while True:
            if current in visited:
                # cycle safeguard
                break
            visited.add(current)
            wall_type = self.buildings[current.building_index].wall_type(current.floor)
            if wall_type == WallType.NORMAL:
                # just stay on this floor
                return current
            elif wall_type == WallType.LADDER:
                # move to top of ladder - find the top floor of ladder starting at this floor
                # by problem statement ladder spans multiple floors until no longer ladder
                top = current.floor
                while top < self.max_floor and self.buildings[current.building_index].wall_type(top+1) == WallType.LADDER:
                    top += 1
                current = NinjaPosition(current.building_index, top)
            elif wall_type == WallType.SLIPPERY:
                # slide down to either normal or ladder top below this floor
                below_floor = current.floor - 1
                while below_floor > 0:
                    below_wall = self.buildings[current.building_index].wall_type(below_floor)
                    if below_wall == WallType.NORMAL:
                        current = NinjaPosition(current.building_index, below_floor)
                        return current
                    elif below_wall == WallType.LADDER:
                        # find top of that ladder
                        top = below_floor
                        while top < self.max_floor and self.buildings[current.building_index].wall_type(top+1) == WallType.LADDER:
                            top += 1
                        current = NinjaPosition(current.building_index, top)
                        return current
                    else:
                        below_floor -= 1
                # if no normal or ladder found below, stay where we are
                return current
        return current

class NinjaClimbSolver:
    def __init__(self, floors, building_walls):
        self.floors = floors
        self.buildings = [Building(floors, building_walls[0]), Building(floors, building_walls[1])]
        self.jump_rule = JumpRule(floors)
        self.wall_effect = WallEffectResolver(self.buildings)

    def solve(self):
        from collections import deque
        max_floor = self.floors
        # start states: can start at floor 1 on either building
        start_positions = [NinjaPosition(0,1), NinjaPosition(1,1)]
        visited = set()
        queue = deque()
        # resolve starting positions with wall effect
        for pos in start_positions:
            resolved = self.wall_effect.resolve(pos)
            queue.append((resolved, 0))
            visited.add(resolved)

        while queue:
            current_pos, jumps = queue.popleft()
            # check if reached rooftop:
            # rooftop means floor == max_floor, can go out from there
            if current_pos.floor == max_floor:
                return jumps
            # next jumps
            for dest in self.jump_rule.possible_destinations(current_pos):
                resolved_dest = self.wall_effect.resolve(dest)
                if resolved_dest not in visited:
                    visited.add(resolved_dest)
                    queue.append((resolved_dest, jumps+1))
        return None

class ProblemReader:
    def __init__(self):
        self.datasets = []

    def read(self):
        import sys
        lines = sys.stdin.read().strip().splitlines()
        idx = 0
        while True:
            if idx >= len(lines):
                break
            nline = lines[idx].strip()
            idx += 1
            if nline == '0':  # end of input
                break
            n = int(nline)
            if n < 3 or n > 100:
                # invalid n, skip dataset
                continue
            # Read two lines of walls
            a_line = lines[idx].strip()
            idx += 1
            b_line = lines[idx].strip()
            idx += 1
            a_walls = list(map(int, a_line.split()))
            b_walls = list(map(int, b_line.split()))
            if len(a_walls) != n or len(b_walls) != n:
                # invalid data
                continue
            self.datasets.append( (n, (a_walls, b_walls)) )

class NinjaClimbController:
    def __init__(self):
        self.reader = ProblemReader()

    def run(self):
        self.reader.read()
        for (n, walls) in self.reader.datasets:
            solver = NinjaClimbSolver(n, walls)
            result = solver.solve()
            if result is None:
                print("NA")
            else:
                print(result)

if __name__ == '__main__':
    controller = NinjaClimbController()
    controller.run()