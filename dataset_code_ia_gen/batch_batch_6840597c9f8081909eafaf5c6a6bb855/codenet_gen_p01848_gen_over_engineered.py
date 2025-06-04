class Participant:
    def __init__(self, id_, oversleep_prob, contacts):
        self.id = id_
        self.oversleep_prob = oversleep_prob
        self.contacts = contacts

class MorningCallNetwork:
    def __init__(self, participants):
        self.participants = participants
        self.N = len(participants)
        self.reachability = None

    def compute_reachability(self):
        # Adjacency matrix for reachability by morning calls
        adj = [[False]*self.N for _ in range(self.N)]
        for p in self.participants:
            adj[p.id][p.id] = True  # Each can reach themselves
            for c in p.contacts:
                adj[p.id][c] = True
        # Floyd-Warshall for transitive closure to find all reachable participants from each participant
        for k in range(self.N):
            for i in range(self.N):
                if adj[i][k]:
                    for j in range(self.N):
                        if adj[k][j]:
                            adj[i][j] = True
        self.reachability = adj

    def all_awake_prob(self):
        # Probability all awake = Sum over all subsets of participants who wake initially,
        # of the probability that initial awake set is that subset * indicator(all reachable)
        # But number participants <= 100, 2^100 too large for brute force.
        # Apply DP over subsets with careful state compression impossible.
        # Instead, use inclusion-exclusion over initial awake sets or simulate the effect in another way.
        # Here, we note that if some people wake up initially, they wake everyone reachable from them.
        # So the final awake set is the union of reachability from awake initial participant set.
        # To solve efficiently,
        # Define dp[mask]: probability that exactly this mask of people are awake (impossible to enumerate).
        # Instead, we think reversely: probability that a person is awake:
        # Due to must-call rule, if a person i is awake, all reachable from i are awake.

        # Idea:
        # The probability that the final awake set is S (closed under reachability),
        # is the probability that initial awake set is some subset of S and no one outside S is awake initially,
        # and everyone in S is reachable from initial awake set in S.

        # To avoid complicated calculations, we rely on a Markov chain approach where
        # We model waking process as fixed points.

        # Instead, use matrix multiplications or linear algebra is not ideal here.

        # Alternate solution:
        # The problem can be modeled as the probability that no participant in the final reachable set is asleep.
        # The participants that can be awakened from any initial awake participant must be awake.
        # The only way that a participant is asleep at the end is if all participants from which there is a path to them overslept.

        # Let's find the condensation graph strongly connected components (SCC).
        # For each SCC, if any participant wakes up initially (not sleeps), then all SCC members wake.
        # The graph of SCCs is a DAG, so we can traverse from awake SCCs down to other SCCs reachable.

        # But easier approach with given constraints:

        # For each subset of participants who woke initially (not slept), the final awake set is union of reachabilities.
        # Probability initial awake set A = Π_{i in A}(1-p_i) * Π_{i not in A} p_i

        # Because participants are independent in oversleep.

        # The final awake set is union over all i in A of reachable[i].

        # We want probability that final awake set = all participants = set {0,...,N-1}

        # This means at least one initial awake participant can reach each participant.

        # So final awake set = union of reachable[i] for i in A = full set.

        # Then, probability = summation over all subsets A of initial awake participants whose reachabilities union is entire set.

        # Let’s precalculate for each participant the reachable set as an integer bitmask.

        # Let’s define:
        # masks = [bitmask of reachable set for participant i]

        # Then, for subset A, union_of_reach = OR of masks[i] for i in A.

        # We want sum over subsets A where union_of_reach == full mask.

        # Since N ≤ 100, bitmask integer operations are impractical at full length.

        # A solution is to use Inclusion-Exclusion principle approach for subsets, but with 100 participants is impossible.

        # Alternative:

        # Let’s cheat for coding task by Monte Carlo or (no, not allowed).

        # Another method:

        # We consider the minimal sets of participants who can wake everyone (set cover of full set by reachable sets).

        # Since problem constraints are moderate, we can build a DP over sets.

        # But 2^100 is too big.

        # Instead let's approximate:

        # Define f[S] = probability that the final awake set is contained in S (closed under reach)

        # f[S] = ∏_{i=0}^{N-1} [ if i in S then (1-p_i + p_i * indicator(i can be woken from S (always true)) else p_i ]

        # Not applicable easily.

        # Due to complexity, let’s write code reflecting the solution that enumerates initial awake subsets with pruning for test.

        # Given problem constraints and sample outputs, problem expects exact calculations.

        # We implement a DP from subsets covering the participants step by step.

        full_mask = (1 << self.N) - 1
        masks = []
        for p in self.participants:
            bitmask = 0
            for j in range(self.N):
                if self.reachability[p.id][j]:
                    bitmask |= 1 << j
            masks.append(bitmask)

        from collections import defaultdict
        dp = defaultdict(float)
        # dp[mask] = prob sum of initial awake subsets covering reachable union = mask
        dp[0] = 1.0
        for i in range(self.N):
            p = self.participants[i]
            awake_prob = 1 - p.oversleep_prob
            asleep_prob = p.oversleep_prob
            next_dp = defaultdict(float)
            for covered_mask, prob in dp.items():
                # Case: participant i sleeps
                next_dp[covered_mask] += prob * asleep_prob
                # Case: participant i wakes
                new_mask = covered_mask | masks[i]
                next_dp[new_mask] += prob * awake_prob
            dp = next_dp

        return dp[full_mask]

import sys
import math

class InputParser:
    def __init__(self):
        self.lines = sys.stdin.read().strip().split('\n')
        self.index = 0

    def has_next(self):
        return self.index < len(self.lines)

    def next_line(self):
        line = self.lines[self.index]
        self.index += 1
        return line

    def parse_dataset(self):
        if not self.has_next():
            return None
        N_line = self.next_line()
        while N_line == '':
            if not self.has_next():
                return None
            N_line = self.next_line()
        if N_line == '0':
            return None
        N = int(N_line)
        participants = []
        for i in range(N):
            parts = self.next_line().split()
            p_i = float(parts[0])
            m_i = int(parts[1])
            contacts = list(int(x)-1 for x in parts[2:2+m_i])
            participant = Participant(i, p_i, contacts)
            participants.append(participant)
        return participants

def main():
    parser = InputParser()
    while True:
        participants = parser.parse_dataset()
        if participants is None:
            break
        network = MorningCallNetwork(participants)
        network.compute_reachability()
        prob = network.all_awake_prob()
        print(f"{prob:.9f}")

if __name__ == "__main__":
    main()