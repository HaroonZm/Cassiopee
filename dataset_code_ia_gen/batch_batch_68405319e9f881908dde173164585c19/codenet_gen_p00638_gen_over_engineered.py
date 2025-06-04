class Island:
    def __init__(self, treasure: int, bridge_limit: int):
        self.treasure = treasure
        self.bridge_limit = bridge_limit

class IslandNetwork:
    def __init__(self, islands):
        self.islands = islands
        self.n = len(islands)
        self.total_treasure = sum(island.treasure for island in islands)

    def can_complete_tour(self) -> bool:
        # The thief starts and ends on the empty island (index -1)
        # Bridge constraints are symmetric with each island:
        # When going out from empty island to island i: max carrying treasure is island[i].bridge_limit
        # When returning back from island i to empty island: same limit applies
        # The thief collects treasures in order of visiting islands.

        # We try to find an order visiting each island exactly once,
        # such that at every crossing (both ways) the carried treasure is <= bridge limit of the island we're crossing
        # The carried treasure when going from empty island to first island: 0 (no treasure yet)
        # When returning, the thief carries all treasures collected (sum all treasures)
        # Since only the bridges to empty island can break, and bridges between islands don't exist (or are too fragile),
        # the crossing sequences are: empty -> island -> empty -> island -> ...
        # But problem states: he "tries to visit all islands one by one", so order must be a permutation of islands,
        # and route is: empty -> first island -> empty -> second island -> empty -> ... last island -> empty.

        # Interpreting "old bridge between this island and each of all other n islands" means that only way to go from empty island to others and back.
        # So thief must always go empty->island->empty->island->empty->... - visiting islands one by one and returning to empty island each time

        # But problem states "visits with bringing all treasures that he has picked up"
        # So after first island visited, next trip empty->island involves already having treasures from previous islands, so crossing bridge with possibly more treasure.
        # So crossing empty->island: carrying sum of treasures of already collected islands.
        # Crossing island->empty: carrying also all treasures collected including the island currently visited.

        # Ordering is crucial: he can choose order to avoid exceeding bridge limits

        # To conclude:

        # Each trip is empty->island->empty
        # For the i-th visited island in order:
        #   crossing empty->island_i: he carries sum of treasures collected so far (before visiting island_i)
        #   crossing island_i->empty: he carries sum of treasures collected so far + island_i.treasure

        # Each crossing must <= island_i.bridge_limit

        # Our goal: find permutation p of islands s.t for all i:
        #   carried_outbound = sum of treasures collected before this island <= island[p[i]].bridge_limit
        #   carried_inbound = carried_outbound + island[p[i]].treasure <= island[p[i]].bridge_limit

        # So carried_inbound <= island[p[i]].bridge_limit means carried_inbound cannot exceed limit
        # But carried_outbound <= carried_inbound (since treasure[i]>0), so carried_outbound <= island[p[i]].bridge_limit also holds

        # So condition reduces to:
        # For each island in order:
        #   carried_outbound <= island[p[i]].bridge_limit
        #   carried_outbound + island[p[i]].treasure <= island[p[i]].bridge_limit
        # This means:
        #   carried_outbound + island[p[i]].treasure <= island[p[i]].bridge_limit
        #   => sum_so_far + treasure[i] <= limit_i

        # So at visit i:
        #    sum_so_far + treasure_i <= bridge_limit_i
        # (sum_so_far is current sum of collected treasures before visiting island i)

        # At visit 0, sum_so_far=0

        # So algorithm: find permutation p st for all i sum(treasure[p[j]] j=0..i) <= bridge_limit[p[i]]

        # Let's implement this as a backtracking search.

        def backtrack(visited_mask, collected_so_far):
            if visited_mask == (1 << self.n) - 1:
                # all visited
                return True
            for i in range(self.n):
                if (visited_mask & (1 << i)) == 0:
                    treasure_i = self.islands[i].treasure
                    limit_i = self.islands[i].bridge_limit
                    new_collected = collected_so_far + treasure_i
                    # Check constraint sum_so_far + treasure_i <= bridge_limit_i
                    if new_collected <= limit_i:
                        if backtrack(visited_mask | (1 << i), new_collected):
                            return True
            return False

        return backtrack(0, 0)

class ProblemBSolver:
    def __init__(self):
        self.datasets = []

    def read_input(self):
        while True:
            n = int(input())
            if n == 0:
                break
            islands = []
            for _ in range(n):
                t, l = map(int, input().split())
                islands.append(Island(t, l))
            self.datasets.append(IslandNetwork(islands))

    def solve(self):
        for network in self.datasets:
            print("Yes" if network.can_complete_tour() else "No")

def main():
    solver = ProblemBSolver()
    solver.read_input()
    solver.solve()

if __name__ == "__main__":
    main()