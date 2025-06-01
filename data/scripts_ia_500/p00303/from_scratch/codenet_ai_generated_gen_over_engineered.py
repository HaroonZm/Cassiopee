from abc import ABC, abstractmethod
from typing import Dict, Set, List, Tuple

class Node(ABC):
    @abstractmethod
    def id(self) -> str:
        pass

class User(Node):
    def __init__(self, uid: int):
        self.uid = uid

    def id(self) -> str:
        return f"U{self.uid}"

    def __hash__(self):
        return hash(self.id())

    def __eq__(self, other):
        return isinstance(other, User) and self.uid == other.uid

class Data(Node):
    def __init__(self, did: int):
        self.did = did

    def id(self) -> str:
        return f"D{self.did}"

    def __hash__(self):
        return hash(self.id())

    def __eq__(self, other):
        return isinstance(other, Data) and self.did == other.did

class DependencyGraph:
    def __init__(self):
        # adjacency list from node to set of nodes
        self.adj: Dict[Node, Set[Node]] = {}
        self.users: Dict[int, User] = {}
        self.datas: Dict[int, Data] = {}

    def get_or_create_user(self, uid: int) -> User:
        if uid not in self.users:
            self.users[uid] = User(uid)
        return self.users[uid]

    def get_or_create_data(self, did: int) -> Data:
        if did not in self.datas:
            self.datas[did] = Data(did)
        return self.datas[did]

    def add_edge(self, from_node: Node, to_node: Node) -> None:
        if from_node not in self.adj:
            self.adj[from_node] = set()
        self.adj[from_node].add(to_node)

    def build_from_relations(self, relations: List[Tuple[int, str, int]]) -> None:
        # According to rules:
        # - If user u lock data d => data->user edge
        # - If user u wait data d => user->data edge
        for u, rel_type, d in relations:
            user = self.get_or_create_user(u)
            data = self.get_or_create_data(d)
            if rel_type == "lock":
                # edge: data -> user
                self.add_edge(data, user)
            elif rel_type == "wait":
                # edge: user -> data
                self.add_edge(user, data)
            else:
                raise ValueError(f"Unknown relation type: {rel_type}")

    def has_cycle(self) -> bool:
        visited: Set[Node] = set()
        rec_stack: Set[Node] = set()

        def dfs(node: Node) -> bool:
            visited.add(node)
            rec_stack.add(node)
            for neighbour in self.adj.get(node, []):
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
                elif neighbour in rec_stack:
                    return True
            rec_stack.remove(node)
            return False

        for node in self.adj.keys():
            if node not in visited:
                if dfs(node):
                    return True
        return False

class DeadlockDetector:
    def __init__(self, relations: List[Tuple[int, str, int]]):
        self.graph = DependencyGraph()
        self.graph.build_from_relations(relations)

    def detect(self) -> int:
        if self.graph.has_cycle():
            return 1
        else:
            return 0

def main():
    import sys

    input = sys.stdin.readline
    N = int(input())
    relations = []
    for _ in range(N):
        line = input().strip().split()
        u = int(line[0])
        rel = line[1]
        d = int(line[2])
        relations.append((u, rel, d))

    detector = DeadlockDetector(relations)
    print(detector.detect())

if __name__ == "__main__":
    main()