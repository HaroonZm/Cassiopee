class Ring:
    def __init__(self, engraving: str):
        self.engraving = engraving
        self.length = len(engraving)
        # Extended engraving to simulate the ring's continuity
        self._extended = engraving * 2

    def contains(self, query: str) -> bool:
        # We only need to check a substring of length len(query) within the doubled engraving
        max_start = self.length  # only check start positions within original length
        qlen = len(query)
        for start in range(max_start):
            segment = self._extended[start:start + qlen]
            if segment == query:
                return True
        return False


class RingCollection:
    def __init__(self):
        self.rings = []

    def add_ring(self, ring: Ring):
        self.rings.append(ring)

    def count_rings_containing(self, query: str) -> int:
        # Count rings which contain query as substring in their ring engraving
        return sum(1 for ring in self.rings if ring.contains(query))


class InputParser:
    @staticmethod
    def parse():
        query = input().strip()
        n = int(input().strip())
        ring_collection = RingCollection()
        for _ in range(n):
            engraving = input().strip()
            ring_collection.add_ring(Ring(engraving))
        return query, ring_collection


class OutputPresenter:
    @staticmethod
    def present(count: int):
        print(count)


class Solution:
    def __init__(self):
        self.query = None
        self.rings = None

    def run(self):
        self.query, self.rings = InputParser.parse()
        count = self.rings.count_rings_containing(self.query)
        OutputPresenter.present(count)


if __name__ == "__main__":
    solution = Solution()
    solution.run()