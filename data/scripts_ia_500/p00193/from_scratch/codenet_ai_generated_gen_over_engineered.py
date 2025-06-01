class HexGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[Block(x + 1, y + 1) for y in range(height)] for x in range(width)]

    def in_bounds(self, x: int, y: int) -> bool:
        return 1 <= x <= self.width and 1 <= y <= self.height

    def neighbors(self, x: int, y: int) -> list:
        # Hex grid neighbors depend on row parity
        # Odd row's neighbors
        if y % 2 == 1:
            candidates = [
                (x - 1, y), (x, y - 1), (x, y + 1),
                (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
            ]
        else:
            # Even row neighbors
            candidates = [
                (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                (x, y - 1), (x, y + 1), (x + 1, y)
            ]
        return [(nx, ny) for (nx, ny) in candidates if self.in_bounds(nx, ny)]

    def blocks(self):
        for x_blocks in self.grid:
            for block in x_blocks:
                yield block

    def block_at(self, x: int, y: int):
        if not self.in_bounds(x, y):
            raise IndexError("Coordinates out of bound")
        return self.grid[x - 1][y - 1]


class Block:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        # will hold list of nearest convenience store ids it is uniquely closest to
        self.closest_stores = []
        self.distance = None


class ConvenienceStore:
    def __init__(self, id: int, x: int, y: int):
        self.id = id
        self.x = x
        self.y = y


class DistanceMap:
    def __init__(self, hexgrid: HexGrid, stores: list):
        self.hexgrid = hexgrid
        self.stores = stores
        # distance maps from each store to all blocks; store id -> dict coordinate->distance
        self.distances_by_store = {store.id: {} for store in stores}
        # will hold for each block a tuple (min_distance, list_of_store_ids_with_that_distance)
        self.block_min_distances = {}

    def calculate_all_distances(self):
        # For each store perform BFS to calculate distance to all blocks
        for store in self.stores:
            self.distances_by_store[store.id] = self._bfs_distances_from(store.x, store.y)

    def _bfs_distances_from(self, sx, sy) -> dict:
        from collections import deque
        dist_map = {}
        visited = set()
        q = deque()
        q.append((sx, sy, 0))
        visited.add((sx, sy))
        dist_map[(sx, sy)] = 0
        while q:
            x, y, d = q.popleft()
            for nx, ny in self.hexgrid.neighbors(x, y):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dist_map[(nx, ny)] = d + 1
                    q.append((nx, ny, d + 1))
        return dist_map

    def resolve_closest_stores_per_block(self):
        # For all blocks decide which store(s) have minimum distance
        for block in self.hexgrid.blocks():
            min_dist = None
            min_stores = []
            for store_id, distances in self.distances_by_store.items():
                d = distances.get((block.x, block.y))
                if d is None:
                    continue
                if (min_dist is None) or (d < min_dist):
                    min_dist = d
                    min_stores = [store_id]
                elif d == min_dist:
                    min_stores.append(store_id)
            block.distance = min_dist
            block.closest_stores = min_stores


class CoverageAnalyzer:
    def __init__(self, hexgrid: HexGrid, existing_stores: list, candidate_stores: list):
        self.hexgrid = hexgrid
        self.existing_stores = existing_stores
        self.candidate_stores = candidate_stores

    def analyze(self):
        # Step1: Calculate distances and closest stores for existing stores
        dmap_existing = DistanceMap(self.hexgrid, self.existing_stores)
        dmap_existing.calculate_all_distances()
        dmap_existing.resolve_closest_stores_per_block()

        # Count coverage by existing stores
        coverage_counts = {store.id: 0 for store in self.existing_stores}
        for block in self.hexgrid.blocks():
            if len(block.closest_stores) == 1:
                coverage_counts[block.closest_stores[0]] += 1

        # Prepare coverage for candidates by simulating their additions one by one
        max_coverage = 0
        for candidate in self.candidate_stores:
            extended_stores = self.existing_stores + [candidate]
            # Calculate distances with candidate included
            dmap_extended = DistanceMap(self.hexgrid, extended_stores)
            dmap_extended.calculate_all_distances()
            dmap_extended.resolve_closest_stores_per_block()

            # Count blocks uniquely closest to candidate
            candidate_coverage = 0
            for block in self.hexgrid.blocks():
                if len(block.closest_stores) == 1 and block.closest_stores[0] == candidate.id:
                    candidate_coverage += 1
            if candidate_coverage > max_coverage:
                max_coverage = candidate_coverage
        return max_coverage


def parse_input():
    import sys
    datasets = []
    lines = iter(sys.stdin.read().strip().split('\n'))
    while True:
        try:
            m_n_line = next(lines).strip()
            if m_n_line == '0 0':
                break
            m, n = map(int, m_n_line.split())
            s = int(next(lines).strip())
            existing_stores = []
            for i in range(s):
                x, y = map(int, next(lines).strip().split())
                existing_stores.append(ConvenienceStore(i + 1, x, y))
            t = int(next(lines).strip())
            candidate_stores = []
            for i in range(t):
                x, y = map(int, next(lines).strip().split())
                candidate_stores.append(ConvenienceStore(s + i + 1, x, y))  # id distinct from existing
            datasets.append((m, n, existing_stores, candidate_stores))
        except StopIteration:
            break
    return datasets


def main():
    datasets = parse_input()
    for m, n, existing_stores, candidate_stores in datasets:
        hexgrid = HexGrid(m, n)
        analyzer = CoverageAnalyzer(hexgrid, existing_stores, candidate_stores)
        result = analyzer.analyze()
        print(result)


if __name__ == '__main__':
    main()