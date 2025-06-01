from collections import Counter
from typing import List, Tuple
import itertools

class StickSet:
    def __init__(self, sticks: List[int]):
        if len(sticks) != 12:
            raise ValueError("Exactly 12 sticks are required")
        self.sticks = sticks
    
    def count_lengths(self) -> Counter:
        return Counter(self.sticks)

class RectangleValidator:
    def __init__(self, sticks_counter: Counter):
        self.counter = sticks_counter

    def can_form_rectangle_edges(self) -> bool:
        # A rectangular cuboid requires 3 pairs of edges with lengths a,b,c each repeated 4 times:
        # 12 sticks can be grouped as 3 groups of 4 equal lengths
        length_groups = sorted(self.counter.elements())
        # instead of flat elements, we process the counter items to find counts of each length
        counts = [count for length, count in sorted(self.counter.items())]

        # The requirement for a cuboid:
        # Each of the 3 distinct edge lengths should appear exactly 4 times (for edges)
        # Or some equalities to allow cubes (all equal length 12 times)
        # So frequencies must be divisible by 2 (to make pairs) and then group into 3 pairs
        
        # Because there are 12 sticks, the count of their lengths must be exactly either:
        # - 3 different lengths, each appearing 4 times
        # - 2 different lengths appearing (8 + 4) or (4 + 8) times? No, impossible to build a cuboid with only 2 lengths in 12 sticks
        # - 1 length appearing 12 times (cube)
        
        # Let's check the counts list directly
        length_freqs = sorted(self.counter.values())
        if length_freqs == [12]:
            # cube case
            return True
        
        # We want to form 3 pairs of equal lengths, each repeated 4 times, so counts must be [4,4,4].
        if length_freqs == [4,4,4]:
            return True
        
        # Another check: since edges need to be grouped in pairs:
        # We can try to form six pairs from these sticks - each pair representing an edge length.
        # So try to create six pairs (each length repeated twice) that can form 3 edges repeated twice.
        
        # For a cuboid, the edges appear in pairs: the twelve sticks correspond to 6 pairs (2 sticks per edge), representing the three edges doubled.
        # So among the sticks, we must get exactly 6 pairs, and pairs must be grouped into three pairs of equal length pairs.
        
        pairs = []
        for length, count in self.counter.items():
            if count % 2 != 0:
                return False
            pairs.extend([length]*(count//2))
        
        if len(pairs) != 6:
            return False
        
        # Now pairs group into 3 groups of 2 equal
        # Try all partitions of these 6 pairs into three pairs of equal length pairs
        
        # Group pairs count
        pairs_counter = Counter(pairs)
        # We want to find if pairs_counter can be partitioned into 3 pairs (2 sticks each)
        # That means pairs_counter will have 3 lengths, each appearing twice.
        lengths_appear_twice = list(pairs_counter.values()).count(2)
        if lengths_appear_twice == 3 and len(pairs_counter) == 3:
            return True
        
        # Alternatively, if pairs_counter has 1 length appearing 6 times (all pairs equal),
        # that gives cube edges (= same length)
        if len(pairs_counter) == 1 and list(pairs_counter.values())[0] == 6:
            return True
        
        return False

class CuboidChecker:
    def __init__(self, sticks: List[int]):
        self.stick_set = StickSet(sticks)
        self.validator = RectangleValidator(self.stick_set.count_lengths())
    
    def check(self) -> str:
        return "yes" if self.validator.can_form_rectangle_edges() else "no"

def main(input_line: str) -> None:
    sticks = list(map(int, input_line.strip().split()))
    checker = CuboidChecker(sticks)
    print(checker.check())