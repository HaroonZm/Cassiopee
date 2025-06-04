class EnemyGrid:
    def __init__(self, n, grid):
        self.n = n
        self.grid = grid  # grid as list of list of int, 1 or 0

    def clone(self):
        return EnemyGrid(self.n, [row[:] for row in self.grid])

    def all_defeated(self):
        return all(enemy == 0 for row in self.grid for enemy in row)

    def toggle_rectangle(self, top, left, bottom, right):
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                self.grid[r][c] ^= 1

    def to_tuple(self):
        return tuple(tuple(row) for row in self.grid)


class Rectangle:
    def __init__(self, top, left, bottom, right):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right

    def __repr__(self):
        return f"Rect(({self.top},{self.left})-({self.bottom},{self.right}))"


class SpellCaster:
    def __init__(self, enemy_grid):
        self.original_grid = enemy_grid
        self.n = enemy_grid.n
        self.visited = {}
        self.queue = []
        self.parent_map = {}
        self.action_map = {}

    def generate_all_rectangles(self):
        rects = []
        n = self.n
        for top in range(n):
            for left in range(n):
                for bottom in range(top, n):
                    for right in range(left, n):
                        rects.append(Rectangle(top, left, bottom, right))
        return rects

    def solve(self):
        start_state = self.original_grid.to_tuple()
        if all(enemy == 0 for row in start_state for enemy in row):
            return ""  # Already all defeated
        from collections import deque
        queue = deque()
        queue.append(start_state)
        self.visited[start_state] = True
        self.parent_map[start_state] = None
        self.action_map[start_state] = None
        rectangles = self.generate_all_rectangles()
        while queue:
            current = queue.popleft()
            current_grid = EnemyGrid(self.n, [list(row) for row in current])
            if current_grid.all_defeated():
                # reconstruct path
                path = []
                state = current
                while self.parent_map[state] is not None:
                    path.append(self.action_map[state])
                    state = self.parent_map[state]
                path.reverse()
                return "myon" * len(path)
            # try all moves:
            for rect in rectangles:
                next_grid = EnemyGrid(self.n, [list(row) for row in current])
                next_grid.toggle_rectangle(rect.top, rect.left, rect.bottom, rect.right)
                next_state = next_grid.to_tuple()
                if next_state not in self.visited:
                    self.visited[next_state] = True
                    self.parent_map[next_state] = current
                    self.action_map[next_state] = rect
                    queue.append(next_state)
        return ""  # no solution (should not happen)

class InputParser:
    def __init__(self):
        self.datasets = []

    def parse(self):
        import sys
        lines = sys.stdin.read().splitlines()
        idx = 0
        while idx < len(lines):
            n = int(lines[idx])
            idx += 1
            if n == 0:
                break
            grid = []
            for _ in range(n):
                row = list(map(int, lines[idx].split()))
                idx += 1
                grid.append(row)
            self.datasets.append(EnemyGrid(n, grid))


class OutputHandler:
    def __init__(self, results):
        self.results = results

    def print_results(self):
        for res in self.results:
            print(res)


class MysteriousOnslaughtSolver:
    def __init__(self):
        self.input_parser = InputParser()
        self.results = []

    def run(self):
        self.input_parser.parse()
        for enemy_grid in self.input_parser.datasets:
            spell_caster = SpellCaster(enemy_grid)
            shortest_spell = spell_caster.solve()
            self.results.append(shortest_spell)
        output_handler = OutputHandler(self.results)
        output_handler.print_results()


if __name__ == "__main__":
    MysteriousOnslaughtSolver().run()