class NoteSequence:
    def __init__(self, notes, beauty_values, L):
        self.notes = notes
        self.beauty_values = beauty_values
        self.L = L
        self.N = len(notes)
        self.M = len(beauty_values)
        self.prefix_beauty_sums = self._compute_prefix_beauty_sums()
        self.repel_cache = {}

    def _compute_prefix_beauty_sums(self):
        prefix_sums = [0] * (self.M + 1)
        for i in range(1, self.M + 1):
            prefix_sums[i] = prefix_sums[i-1] + self.beauty_values[i-1]
        return prefix_sums

    def musical_beauty_sum(self, a, b):
        # Sum of S_a to S_b inclusive. 1-based indices a,b.
        return self.prefix_beauty_sums[b] - self.prefix_beauty_sums[a-1]

    def repulsion(self, a, b):
        # a,b are pitches, 1 <= a <= b <= M
        key = (a,b)
        if key not in self.repel_cache:
            total_beauty = self.musical_beauty_sum(a,b)
            self.repel_cache[key] = total_beauty // self.L
        return self.repel_cache[key]

class CircularPermutationOptimizer:
    def __init__(self, notes, note_sequence):
        self.notes = notes
        self.N = len(notes)
        self.seq = note_sequence
        self.min_spirit = float('inf')

    def compute_repulsion_between_notes(self, i, j):
        # index i,j in notes, 0-based
        a = self.notes[i]
        b = self.notes[j]
        if a > b:
            a, b = b, a
        return self.seq.repulsion(a, b)

    def build_adj_matrix(self):
        # Build adjacency matrix of repulsions between consecutive notes
        # Only needed for DP edges
        self.adj = [[0]*self.N for _ in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                if i != j:
                    self.adj[i][j] = self.compute_repulsion_between_notes(i,j)

    def solve(self):
        # Reduce symmetricity by fixing note 0 at first position
        # Use bitmask DP for TSP-like cycle on notes 1..N-1
        # dp[mask][last] = min spirit consumed placing subset mask of notes {1..N-1} with last at last position
        self.build_adj_matrix()
        N = self.N - 1
        dp = [[float('inf')] * (N+1) for _ in range(1<<N)]
        dp[0][0] = 0  # starting at note 0, no other notes placed

        for mask in range(1<<N):
            for last in range(N+1):
                if dp[mask][last] == float('inf'):
                    continue
                for nxt in range(1, N+1):
                    bit = 1 << (nxt-1)
                    if not (mask & bit):
                        cost = dp[mask][last] + self.adj[last][nxt]
                        if cost < dp[mask | bit][nxt]:
                            dp[mask | bit][nxt] = cost

        full_mask = (1 << N) -1
        res = float('inf')
        for last in range(1, N+1):
            cost = dp[full_mask][last] + self.adj[last][0]
            if cost < res:
                res = cost
        return res

class MagicalCircle:
    def __init__(self, N, M, L, notes, beauty_values):
        self.N = N
        self.M = M
        self.L = L
        self.notes = notes
        self.beauty_values = beauty_values
        self.note_sequence = NoteSequence(notes, beauty_values, L)
        self.optimizer = CircularPermutationOptimizer(notes, self.note_sequence)

    def minimal_spirit_consumption(self):
        return self.optimizer.solve()

def main():
    import sys
    sys.setrecursionlimit(10**7)
    N, M, L = map(int, sys.stdin.readline().split())
    notes = list(map(int, sys.stdin.readline().split()))
    beauty_values = list(map(int, sys.stdin.readline().split()))
    magical_circle = MagicalCircle(N, M, L, notes, beauty_values)
    ans = magical_circle.minimal_spirit_consumption()
    print(ans)

if __name__ == "__main__":
    main()