class IUserIdentifier:
    def get_id(self) -> int:
        raise NotImplementedError

class User(IUserIdentifier):
    __slots__ = ['_id']
    def __init__(self, user_id: int):
        self._id = user_id
    def get_id(self) -> int:
        return self._id
    def __repr__(self):
        return f"User({self._id})"

class IRelation:
    def get_endpoints(self) -> tuple:
        raise NotImplementedError

class Relation(IRelation):
    __slots__ = ['_user1', '_user2']
    def __init__(self, user1: IUserIdentifier, user2: IUserIdentifier):
        self._user1 = user1
        self._user2 = user2
    def get_endpoints(self) -> tuple:
        return (self._user1.get_id(), self._user2.get_id())
    def __repr__(self):
        return f"Relation({self._user1}, {self._user2})"

class IDisjointSet:
    def find(self, x: int) -> int:
        raise NotImplementedError
    def union(self, x: int, y: int) -> None:
        raise NotImplementedError
    def is_connected(self, x: int, y: int) -> bool:
        raise NotImplementedError

class DisjointSet(IDisjointSet):
    def __init__(self, size: int):
        self._parent = list(range(size))
        self._rank = [0]*size
    def find(self, x: int) -> int:
        while self._parent[x] != x:
            self._parent[x] = self._parent[self._parent[x]]
            x = self._parent[x]
        return x
    def union(self, x: int, y: int) -> None:
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self._rank[xroot] < self._rank[yroot]:
            self._parent[xroot] = yroot
        elif self._rank[xroot] > self._rank[yroot]:
            self._parent[yroot] = xroot
        else:
            self._parent[yroot] = xroot
            self._rank[xroot] += 1
    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

class ISNS:
    def add_relation(self, relation: IRelation) -> None:
        raise NotImplementedError
    def query_reachable(self, user1: IUserIdentifier, user2: IUserIdentifier) -> bool:
        raise NotImplementedError

class SocialNetworkService(ISNS):
    def __init__(self, user_count: int):
        self._user_count = user_count
        self._relations = []
        self._ds = DisjointSet(user_count)
    def add_relation(self, relation: IRelation) -> None:
        self._relations.append(relation)
        s, t = relation.get_endpoints()
        self._ds.union(s, t)
    def query_reachable(self, user1: IUserIdentifier, user2: IUserIdentifier) -> bool:
        return self._ds.is_connected(user1.get_id(), user2.get_id())

class InputParser:
    def __init__(self):
        self._line_index = 0
        self._lines = []
    def read_all(self):
        import sys
        self._lines = sys.stdin.read().splitlines()
    def next_line(self) -> str:
        line = self._lines[self._line_index]
        self._line_index += 1
        return line
    def parse_ints(self, line: str):
        return tuple(map(int, line.strip().split()))

class OutputWriter:
    @staticmethod
    def write_lines(lines):
        print('\n'.join(lines))

def main():
    parser = InputParser()
    parser.read_all()
    n,m = parser.parse_ints(parser.next_line())
    sns = SocialNetworkService(n)
    for _ in range(m):
        s,t = parser.parse_ints(parser.next_line())
        sns.add_relation(Relation(User(s), User(t)))
    q = int(parser.next_line())
    results = []
    for _ in range(q):
        s,t = parser.parse_ints(parser.next_line())
        reachable = sns.query_reachable(User(s), User(t))
        results.append("yes" if reachable else "no")
    OutputWriter.write_lines(results)

if __name__ == "__main__":
    main()