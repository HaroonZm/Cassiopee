class Leaf:
    def __init__(self, index: int, dirtiness: int):
        self.index = index
        self.dirtiness = dirtiness

    def is_dirty_enough_to_consider(self, threshold: int) -> bool:
        return self.dirtiness >= threshold

    def is_clean_enough_to_revoke(self, threshold: int) -> bool:
        return self.dirtiness <= threshold


class Cabbage:
    def __init__(self, leaves):
        self.leaves = leaves
        self.N = len(leaves)

    def outer_to_inner_generator(self):
        for i in range(self.N):
            yield self.leaves[i]

    def inner_to_outer_generator(self, discard_candidates):
        for leaf in reversed(discard_candidates):
            yield leaf


class DiscardStrategy:
    def __init__(self, cabbage, M, A, B):
        self.cabbage = cabbage
        self.M = M
        self.A = A
        self.B = B
        # Track which leaves are discard candidates (indices)
        self.discard_candidates = []
        # Keep track of which leaves have been inspected for initial discarding
        self.inspected_outer_index = 0
        # Track which leaves inside discard_candidates have been inspected in revocation phase
        self.inspected_inner_index = -1  # start from the innermost discarded

    def initial_discard_selection(self):
        # Step 1: From outside to inside, select leaves with dirtiness >= A
        for leaf in self.cabbage.outer_to_inner_generator():
            if leaf.is_dirty_enough_to_consider(self.A):
                self.discard_candidates.append(leaf)
                self.inspected_outer_index += 1
            else:
                break

    def revocation_phase(self):
        # Repeat process until discard candidates condition is met
        while True:
            non_discard_count = self.cabbage.N - len(self.discard_candidates)
            if non_discard_count >= self.M:
                break  # Enough clean leaves, stop revocation

            if len(self.discard_candidates) == 0:
                break  # No discard candidates, end

            # The innermost leaf in discard_candidates
            leaf = self.discard_candidates[-1]

            if leaf.is_clean_enough_to_revoke(self.B):
                # Remove this leaf from discard candidates
                self.discard_candidates.pop()
                continue  # Check condition again

            else:
                # Discard all leaves in discard_candidates forcibly
                break  # end revocation phase immediately

    def execute_strategy(self):
        self.initial_discard_selection()
        self.revocation_phase()
        return len(self.discard_candidates)


class InputParser:
    @staticmethod
    def parse_input():
        N, M, A, B = map(int, input().split())
        dirtiness_list = list(map(int, input().split()))
        leaves = [Leaf(i+1, d) for i, d in enumerate(dirtiness_list)]
        return N, M, A, B, leaves


class OutputFormatter:
    @staticmethod
    def print_result(discard_count: int):
        print(discard_count)


def main():
    # Parsing input through abstraction
    N, M, A, B, leaves = InputParser.parse_input()

    # Instantiate domain entities
    cabbage = Cabbage(leaves)

    # Use strategy pattern for discard logic
    strategy = DiscardStrategy(cabbage, M, A, B)
    discard_count = strategy.execute_strategy()

    # Output with formatting abstraction
    OutputFormatter.print_result(discard_count)


if __name__ == "__main__":
    main()