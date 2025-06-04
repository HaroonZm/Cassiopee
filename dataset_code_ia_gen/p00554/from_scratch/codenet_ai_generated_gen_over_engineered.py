class PointCard:
    def __init__(self, total_slots: int, hit_count: int, miss_count: int):
        self.total_slots = total_slots
        self.hit_count = hit_count
        self.miss_count = miss_count

    def cost_to_reach_target(self, target_hits: int) -> int:
        if self.hit_count >= target_hits:
            return 0
        needed = target_hits - self.hit_count
        # We can convert misses to hits at a cost of 1 per slot
        return max(needed, 0)

class PointCardCollection:
    def __init__(self, cards, N):
        self.cards = cards
        self.target = N
        self.M = len(cards)

    def minimum_cost_for_prizes(self):
        # Calculate all needed costs to make each card eligible for prize
        costs = [card.cost_to_reach_target(self.target) for card in self.cards]
        # Sort costs to pick the cheapest (M-1) cards to convert
        costs.sort()
        # We want M - 1 cards with hits >= target with minimal total cost
        # Select smallest M-1 costs
        return sum(costs[:self.M -1])

class InputParser:
    @staticmethod
    def parse_input():
        import sys
        lines = sys.stdin.read().strip().split('\n')
        N, M = map(int, lines[0].split())
        cards = []
        total_slots = 2 * N
        for i in range(1, M+1):
            A, B = map(int, lines[i].split())
            cards.append(PointCard(total_slots=total_slots, hit_count=A, miss_count=B))
        return N, M, cards

class JOISolver:
    def __init__(self):
        pass

    def solve(self):
        N, M, cards = InputParser.parse_input()
        collection = PointCardCollection(cards, N)
        print(collection.minimum_cost_for_prizes())

if __name__ == "__main__":
    JOISolver().solve()