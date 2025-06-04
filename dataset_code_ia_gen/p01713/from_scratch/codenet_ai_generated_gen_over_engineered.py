import sys
from abc import ABC, abstractmethod
from typing import List, Dict, Tuple, Optional, Iterator

sys.setrecursionlimit(10**7)

class DoorType:
    EXIT = 0
    ENTRANCE = 1  # constructed by positive a_i
    FIRE_DOOR = 2

class Unit:
    def __init__(self, index: int, value: int):
        self.index = index
        self.value = value  # a_i
        self.door_type = self.determine_door_type()
        self.fire_time: Optional[int] = (-value if value < 0 else None)
        self.entry_times: List[int] = []  # times at which people appear here (if entrance)
        self.graph_nodes: List['Node'] = []
    def determine_door_type(self) -> int:
        if self.value == 0:
            return DoorType.EXIT
        elif self.value < 0:
            return DoorType.FIRE_DOOR
        else:
            return DoorType.ENTRANCE

class Node:
    def __init__(self, unit: Unit, time: int):
        self.unit = unit
        self.time = time
        self.id = self._gen_id()
        self.edges: List['Edge'] = []
        self.is_entering = False  # source connection or sink connection will mark later

    def _gen_id(self) -> int:
        # unique integer key for node = unit_index * max_time + time
        # max_time is not fixed here; we will assign in graph builder
        # but for indexing we can assign externally
        return (self.unit.index, self.time)

    def __repr__(self):
        return f"Node(u={self.unit.index},t={self.time})"

class Edge:
    def __init__(self, from_node: Node, to_node: Node, capacity: int):
        self.from_node = from_node
        self.to_node = to_node
        self.capacity = capacity
        self.flow = 0
        self.rev: Optional[Edge] = None

    def residual_capacity(self) -> int:
        return self.capacity - self.flow

    def __repr__(self):
        return f"Edge({self.from_node} -> {self.to_node}, c={self.capacity}, f={self.flow})"

class FlowNetwork:
    def __init__(self):
        self.adj: Dict[Node, List[Edge]] = {}
        self.nodes: List[Node] = []
        self.source: Optional[Node] = None
        self.sink: Optional[Node] = None

    def add_node(self, node: Node) -> None:
        if node not in self.adj:
            self.adj[node] = []
            self.nodes.append(node)

    def add_edge(self, u: Node, v: Node, capacity: int) -> None:
        e = Edge(u, v, capacity)
        re = Edge(v, u, 0)
        e.rev = re
        re.rev = e
        self.adj[u].append(e)
        self.adj[v].append(re)

    def bfs(self, s: Node, t: Node) -> Optional[Dict[Node, Edge]]:
        parent: Dict[Node, Edge] = {}
        queue = [s]
        visited = {s}
        while queue:
            u = queue.pop(0)
            for e in self.adj[u]:
                v = e.to_node
                if v not in visited and e.residual_capacity() > 0:
                    visited.add(v)
                    parent[v] = e
                    if v == t:
                        return parent
                    queue.append(v)
        return None

    def max_flow_edmonds_karp(self, s: Node, t: Node) -> int:
        flow = 0
        while True:
            parent = self.bfs(s, t)
            if parent is None:
                break
            # find bottleneck
            v = t
            bottleneck = float('inf')
            while v != s:
                e = parent[v]
                bottleneck = min(bottleneck, e.residual_capacity())
                v = e.from_node
            # apply flow
            v = t
            while v != s:
                e = parent[v]
                e.flow += bottleneck
                e.rev.flow -= bottleneck
                v = e.from_node
            flow += bottleneck
        return flow

class EvacuationModel:
    def __init__(self, W: int, a: List[int]):
        self.W = W
        self.a = a
        self.units: List[Unit] = [Unit(i, a[i]) for i in range(W)]
        self.max_time = self.determine_max_time()
        self.network = FlowNetwork()
        self.node_map: Dict[Tuple[int,int], Node] = {}  # (unit,time) -> Node
        self.source = Node(Unit(-1, 0), -1)  # dummy source node
        self.sink = Node(Unit(-2, 0), -1)    # dummy sink node

    def determine_max_time(self) -> int:
        # The maximum relevant time is constrained by:
        # - max fire door closing time
        # - max entrance count (times people appear)
        # We take max(|a_i|) for fire doors plus max a_i for entrances plus some margin=10
        max_fire_close = 0
        max_entrance_time = 0
        for v in self.a:
            if v < 0:
                max_fire_close = max(max_fire_close, -v)
            elif v > 0:
                max_entrance_time = max(max_entrance_time, v)
        # Also add W for max steps people can move along the corridor
        return max_fire_close + max_entrance_time + self.W + 10

    def node(self, unit_idx: int, time: int) -> Node:
        key = (unit_idx, time)
        if key not in self.node_map:
            node = Node(self.units[unit_idx], time)
            self.node_map[key] = node
            self.network.add_node(node)
        return self.node_map[key]

    def build_graph(self) -> None:
        # Add source and sink nodes
        self.network.add_node(self.source)
        self.network.add_node(self.sink)
        self.network.source = self.source
        self.network.sink = self.sink

        # Add edges for person appearances (entrances)
        for u in self.units:
            if u.door_type == DoorType.ENTRANCE:
                for t in range(u.value):
                    # At time t, one person appears at unit u.index
                    # The model states the people start at this unit at time t,
                    # but only move from t+1.
                    start_node = self.node(u.index, t)
                    # connect source to start_node with capacity 1 per person appearance
                    self.network.add_edge(self.source, start_node, 1)

        # For each time for each unit we create edges from node(t) to node(t+1)
        # allowing moves to i-1, i, i+1 provided fire door is not closed and units exist
        for t in range(self.max_time):
            for i in range(self.W):
                if self.units[i].fire_time is not None and t >= self.units[i].fire_time:
                    # Unit closed from this time onwards, no nodes or edges here.
                    continue
                u_now = self.node(i, t)
                # Now add edges from u_now to u_next nodes at t+1
                if t+1 >= self.max_time:
                    continue
                for ni in [i-1, i, i+1]:
                    if 0 <= ni < self.W:
                        if self.units[ni].fire_time is not None and (t+1) >= self.units[ni].fire_time:
                            continue  # next unit closed at t+1
                        u_next = self.node(ni, t+1)
                        # unlimited capacity since unlimited people can be there simultaneously
                        self.network.add_edge(u_now, u_next, 10**9)

        # Connect all exit door nodes at any time to sink with infinite capacity
        for u in self.units:
            if u.door_type == DoorType.EXIT:
                for t in range(self.max_time):
                    # If unit is closed before t by fire door, skip
                    if u.fire_time is not None and t >= u.fire_time:
                        break
                    exit_node = self.node(u.index, t)
                    self.network.add_edge(exit_node, self.sink, 10**9)

    def solve(self) -> int:
        self.build_graph()
        return self.network.max_flow_edmonds_karp(self.source, self.sink)

def main() -> None:
    input = sys.stdin.readline
    W = int(input())
    a = list(map(int, input().split()))
    model = EvacuationModel(W, a)
    print(model.solve())

if __name__ == '__main__':
    main()