class StampType:
    J = 'J'
    O = 'O'
    I = 'I'
    ALL = (J, O, I)

class StampSequence:
    TARGET = (StampType.J, StampType.O, StampType.I)

    @staticmethod
    def matches(seq):
        return tuple(seq) == StampSequence.TARGET

class StampCollection:
    def __init__(self, stamps):
        self.stamps = list(stamps)

    def insert(self, index, stamp):
        # index is position where new store is inserted (between index and index+1)
        self.stamps.insert(index, stamp)

    def __len__(self):
        return len(self.stamps)

    def __getitem__(self, index):
        return self.stamps[index]

class CombinationCounter:
    def __init__(self, stamp_collection):
        self.stamp_collection = stamp_collection
        self.N = len(stamp_collection)
        # Precompute prefix counts of J, O, I to optimize queries
        self.prefix_counts = {s: [0] * (self.N + 1) for s in StampType.ALL}
        for i, ch in enumerate(stamp_collection):
            for s in StampType.ALL:
                self.prefix_counts[s][i+1] = self.prefix_counts[s][i] + (1 if ch == s else 0)

    def count(self):
        # Count number of (i,j,k) with i < j < k and stamps[i] = J, stamps[j]=O, stamps[k]=I
        # Use prefix sums for O(N) counting
        total = 0
        for j in range(self.N):
            if self.stamp_collection[j] == StampType.O:
                # count how many J before j
                count_J_before = self.prefix_counts[StampType.J][j]
                # count how many I after j
                count_I_after = self.prefix_counts[StampType.I][self.N] - self.prefix_counts[StampType.I][j+1]
                total += count_J_before * count_I_after
        return total

class JOIShopStreet:
    def __init__(self, stamps):
        self.original = StampCollection(stamps)

    def max_stamp_triplets_after_insertion(self):
        max_count = 0
        n = len(self.original)
        # Possible insertion positions: 0 .. n - insert before shop 1 (pos=0), between shops, after shop n (pos=n)
        for pos in range(n + 1):
            for stamp in StampType.ALL:
                new_stamps = StampCollection(self.original.stamps.copy())
                new_stamps.insert(pos, stamp)
                counter = CombinationCounter(new_stamps)
                count = counter.count()
                if count > max_count:
                    max_count = count
        return max_count

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    S = input().strip()

    street = JOIShopStreet(S)
    print(street.max_stamp_triplets_after_insertion())

if __name__ == "__main__":
    main()