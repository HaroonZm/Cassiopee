class Microbe:
    def __init__(self, index: int, release: int, capacity: int):
        self.index = index
        self.release = release
        self.capacity = capacity

    def can_survive(self, total_release: int, count: int) -> bool:
        # Each microbe takes equal amount: total_release / count
        # Must not exceed capacity
        return total_release <= self.capacity * count


class PetriDish:
    def __init__(self, microbes):
        self.microbes = microbes
        self.N = len(microbes)

    def max_survivors(self) -> int:
        # Sort microbes by capacity to release ratio or by capacity to enable a smart check
        # But condition is total_release / count <= min capacity among selected microbes
        # We'll use a binary search on k (number of microbes)
        left, right = 1, self.N
        microbes = self.microbes
        # Pre-sort by capacity asc and by release asc to facilitate efficient checks
        microbes_sorted = sorted(microbes, key=lambda m: (m.capacity, m.release))

        # To check if we can select k microbes with max total release <= capacity*k for all
        # We will attempt to select k microbes with minimal total release such that for each selected microbe, total_release <= capacity * k

        def can(k: int) -> bool:
            # Strategy:
            # For a fixed k, select k microbes that have the lowest release such that each microbe's capacity >= total_release/k
            # But total_release depends on selected microbes -> circular dependency
            # Approach:
            # Select microbes whose capacity >= threshold. Threshold = total_release / k.
            # So we try candidate microbes with capacity >= some threshold.
            # Instead, we do:
            # For microbe with capacity b_i, max total release allowed is b_i * k.
            #
            # Accordingly, if we select k microbes, total_release <= min(b_i * k)
            #
            # So for candidate k,
            # 1) Sort microbes by capacity
            # 2) Select the k microbes with lowest releases among those that have capacity * k >= total_release
            # But total_release is sum of release_i of these microbes
            
            # We do instead:
            # For each microbe, define max total_release allowed = b_i * k
            # So the minimal among these is min(b_i * k)
            # We want sum of release_i <= min(b_i * k)
            #
            # To maximize survivors, pick k microbes with minimal release with capacity constraints
            
            # We'll select all microbes with capacity * k >= X (some threshold)
            # We want minimal total release sum among k microbes with capacity*b_i >= sum_release, circular
            #
            # The accepted approach:
            # Sort microbes by capacity ascending
            # For k, collect all microbes with b_i >= threshold
            # select k microbes with smallest release from those
            #
            # Try all k from 1..N
            
            # Because constraints are large, use an efficient way:
            # For given k, find all microbes where b_i >= min_b = (sum_release / k )
            # Instead of iterating, we binary search on capacity
            
            # To avoid circular dependency, use the classical binary search on k and a priority queue
            # The approach from editorials: 
            # For fixed k, select microbes with minimal release whose capacity >= S/k where S is sum release and S depends on selection
            
            # We try:
            # Sort microbes by capacity ascending
            # Maintain a heap of releases to select k minimal releases from those that satisfy b_i*k >= total_release
            
            # Implement a solution similar to editorial:
            # For fixed k:
            # 1. Filter microbes where capacity >= minimal capacity required
            # 2. From these, pick k microbes with smallest releases
            # 3. If sum of releases <= min capacity * k (which is capacity * k of minimal microbe in the set), return True

            # But we don't know threshold in advance, try an alternative approach:
            # Sort by capacity ascending.
            # For k, traverse from large capacity to small => can pick sets with capacity>= current capacity
            # We can do a data structure approach: pick k microbes with minimal release among microbes with capacity >= threshold

            # More pragmatic approach:
            # We try to pick k microbes that satisfy b_i >= X (some threshold)
            # For all possible threshold, try selecting k microbes with capacity >= threshold
            # And sum releases <= threshold * k
            #
            # Because of constraints, we simulate:
            # Sort all microbes by capacity ascending.
            # For largest capacity assigned to the k-th microbe in the selected group,
            # sum of their releases must <= capacity * k

            # Binary search on k tries:
            # For each k, from microbes sorted by capacity descending, try to pick k microbes with minimal release values.

            # Implementation:
            # Sort microbes by capacity descending (because minimal b_i * k is determined by minimal capacity in selected set)
            # Then for given k, take first k microbes with smallest release (use a min-heap or sort the k first microbes by release)
            # Calculate total release and check if total_release <= minimal b_i * k among selected microbes

            # So pick k microbes with largest capacity, and within them choose those with smallest release.

            # We'll pick top N by capacity descending, pick top k minimal releases among them.

            candidates = [m for m in microbes if m.capacity >= 0]  # all microbes
            candidates.sort(key=lambda m: -m.capacity)

            # To pick k microbes with smallest releases among first idx microbes
            heap = []
            total_release = 0
            count = 0
            min_capacity = None

            for i in range(len(candidates)):
                m = candidates[i]
                # Push release
                if len(heap) < k:
                    import heapq
                    heapq.heappush(heap, -m.release)  # max heap by pushing negative
                    total_release += m.release
                    count += 1
                    # Track min capacity in selected
                    if min_capacity is None or m.capacity < min_capacity:
                        min_capacity = m.capacity
                else:
                    # Check if current release smaller than max in heap
                    if -heap[0] > m.release:
                        removed = -heapq.heappop(heap)
                        total_release -= removed
                        heapq.heappush(heap, -m.release)
                        total_release += m.release
                        if m.capacity < min_capacity:
                            min_capacity = m.capacity
                    # else skip

                if count == k:
                    # Check condition total_release <= min_capacity * k
                    if total_release <= min_capacity * k:
                        return True
            return False

        # classic binary search for max k
        while left < right:
            mid = (left + right + 1) // 2
            if can(mid):
                left = mid
            else:
                right = mid - 1
        return left


class MicrobeFactory:
    @staticmethod
    def from_input() -> PetriDish:
        import sys
        input = sys.stdin.readline
        N = int(input())
        microbes = []
        for i in range(N):
            a, b = map(int, input().split())
            microbes.append(Microbe(i + 1, a, b))
        return PetriDish(microbes)


def main():
    petri_dish = MicrobeFactory.from_input()
    print(petri_dish.max_survivors())


if __name__ == "__main__":
    main()