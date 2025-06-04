class ConveyorLane:
    def __init__(self, lane_id: int):
        self.lane_id = lane_id
        self.connected_lanes = set()

    def connect(self, other: 'ConveyorLane'):
        self.connected_lanes.add(other.lane_id)

class RobotArm:
    def __init__(self, position_x: int, lane_index: int):
        self.position_x = position_x
        self.lane_index = lane_index  # connects lane_index and lane_index + 1

class ConveyorGraph:
    def __init__(self, n: int):
        self.lanes = [ConveyorLane(i) for i in range(1, n+1)]
        self.n = n

    def add_robot_arm(self, arm: RobotArm):
        y = arm.lane_index
        self.lanes[y-1].connect(self.lanes[y])
        self.lanes[y].connect(self.lanes[y-1])

    def build_components(self):
        # Find connected components via Union Find
        uf = UnionFind(self.n)
        for lane in self.lanes:
            for other_id in lane.connected_lanes:
                uf.union(lane.lane_id - 1, other_id - 1)
        return uf

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0]*size
        self.component_size = [1]*size

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                rx, ry = ry, rx
            self.parent[ry] = rx
            self.component_size[rx] += self.component_size[ry]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def size(self, x: int) -> int:
        return self.component_size[self.find(x)]

class ProblemCSolver:
    def __init__(self, n: int, robot_arms: list):
        self.n = n
        self.robot_arms = robot_arms
        self.graph = ConveyorGraph(n)

    def solve(self):
        # Add robot arms edges
        for arm in self.robot_arms:
            self.graph.add_robot_arm(arm)
        uf = self.graph.build_components()
        # Number of manufacturing lines for storage(i) is size of its connected component
        return [uf.size(i) for i in range(self.n)]

def parse_input():
    import sys
    input_line = sys.stdin.readline().strip()
    n, m = map(int, input_line.split())
    robot_arms = []
    for _ in range(m):
        x_i, y_i = map(int, sys.stdin.readline().strip().split())
        robot_arms.append(RobotArm(x_i, y_i))
    return n, robot_arms

def main():
    n, robot_arms = parse_input()
    solver = ProblemCSolver(n, robot_arms)
    result = solver.solve()
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()