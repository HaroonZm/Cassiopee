from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Dict, Tuple, List

class Unit(ABC):
    @abstractmethod
    def to_base(self) -> int:
        pass

    @classmethod
    @abstractmethod
    def from_base(cls, value: int) -> 'Unit':
        pass

class WeightUnit(Unit):
    """
    Represents weight in 'ボッコ'(Bokko) units.
    1 Bokko unit weight = 2^x grams, x >= 0 integer.
    For the problem, weight is given as integer count of Bokko units.
    """
    def __init__(self, bokko: int):
        if bokko < 0:
            raise ValueError("Bokko unit must be non-negative")
        self.bokko = bokko

    def to_base(self) -> int:
        # Base weight unit: 1 gram
        # But problem only manipulates Bokko units as integers, so base is Bokko units directly
        return self.bokko

    @classmethod
    def from_base(cls, value: int) -> 'WeightUnit':
        if value < 0:
            raise ValueError("Base weight must be non-negative")
        return cls(value)

    def __add__(self, other: 'WeightUnit') -> 'WeightUnit':
        return WeightUnit(self.bokko + other.bokko)

    def __eq__(self, other) -> bool:
        if not isinstance(other, WeightUnit):
            return False
        return self.bokko == other.bokko

    def __lt__(self, other: 'WeightUnit') -> bool:
        return self.bokko < other.bokko

    def __hash__(self):
        return hash(self.bokko)

    def __repr__(self):
        return f"WeightUnit({self.bokko})"

class QuantityUnit(Unit):
    """
    Represents quantity in 'マルグ'(Marugu) units.
    1 Marugu unit = 2^y items, y >= 0 integer.
    Here quantity stored as integer count of Marugu units.
    """
    def __init__(self, marugu: int):
        if marugu < 0:
            raise ValueError("Marugu unit must be non-negative")
        self.marugu = marugu

    def to_base(self) -> int:
        # Base quantity unit is the Marugu count itself; the problem does not specify conversions for y
        return self.marugu

    @classmethod
    def from_base(cls, value: int) -> 'QuantityUnit':
        if value < 0:
            raise ValueError("Base quantity must be non-negative")
        return cls(value)

    def __add__(self, other: 'QuantityUnit') -> 'QuantityUnit':
        return QuantityUnit(self.marugu + other.marugu)

    def __eq__(self, other) -> bool:
        if not isinstance(other, QuantityUnit):
            return False
        return self.marugu == other.marugu

    def __repr__(self):
        return f"QuantityUnit({self.marugu})"

class AlloyChunk:
    """
    Represents a single chunk of alloy:
    weight: WeightUnit
    quantity: QuantityUnit
    """
    def __init__(self, weight: WeightUnit, quantity: QuantityUnit):
        self.weight = weight
        self.quantity = quantity

    def total_weight(self) -> int:
        # total weight in Bokko units * counts in Marugu units (sum total weight)
        return self.weight.to_base() * self.quantity.to_base()

    def __repr__(self):
        return f"AlloyChunk(weight={self.weight.bokko}, quantity={self.quantity.marugu})"

class CollectionVehicle:
    """
    Represents a vehicle collecting a certain amount of alloy chunks.
    """
    def __init__(self, chunk: AlloyChunk):
        self.chunk = chunk

    def total_weight(self) -> int:
        return self.chunk.total_weight()

    def __repr__(self):
        return f"CollectionVehicle({self.chunk})"

class AlloyRecyclingSystem:
    """
    Handles collecting alloy chunks from vehicles and recombining them.
    """

    def __init__(self):
        self.vehicles: List[CollectionVehicle] = []

    def add_vehicle_data(self, a_i: int, b_i: int):
        weight = WeightUnit(a_i)
        quantity = QuantityUnit(b_i)
        chunk = AlloyChunk(weight, quantity)
        vehicle = CollectionVehicle(chunk)
        self.vehicles.append(vehicle)

    def total_weight(self) -> int:
        # sum all chunk total weights
        return sum(v.total_weight() for v in self.vehicles)

    def regenerate_min_chunks(self) -> List[AlloyChunk]:
        # sum total weight from all vehicles
        total_weight = self.total_weight()

        # The problem wants to minimize the number of chunks after regen.
        # Minimizing number of chunks means make the quantity to zero (storage in one chunk),
        # and set weight to total_weight, quantity 0 (which corresponds to 1 item)

        # We must convert total_weight (grams in bokko units * marugu counts) into (bokko, marugu).

        # Based on problem statement,
        # The 'marugu' unit is 2^y items.
        # We want to find x,y such that 2^x * 2^y = total_weight
        # But we don't know x,y, and problem does not give those.

        # The input/output format treats a,b as the bokko weight and marugu counts.
        # Actually, the problem expects output of chunks with b=0, as sample shows.

        # So minimizing chunk count means all combined into some chunks with b=0.

        # The sample merges all chunks weight sums, outputting one or more chunks with b=0.

        # Since b=0 means quantity = 1 (2^0=1).

        # We can combine all into single chunk with quantity=1, weight=total_weight.

        # However, the problem example shows multiple chunks if input contains multiple different weights.

        # Reconsider:

        # Because weight unit is 2^x grams, quantity unit 2^y items, total mass:
        # total_mass_grams = sum a_i * 2^x * b_i * 2^y

        # But we only know a_i and b_i.

        # The problem does not specify x and y, so we treat a_i and b_i as integers and calculate weight = a_i * b_i

        # Then we want to find minimal number of chunks each having quantity = 2^y and weight = 2^x, so total mass:

        # Minimal number of chunks is obtained by writing total_mass = sum of weight_i * quantity_i, each weight_i and quantity_i are integers.

        # But with no other constraint, minimal chunk count is achieved by choosing all quantity_i=0 -> quantity=1 and weight_i = total_mass (since b=0 means quantity=1).

        # The problem suggests "weight of small units" in bokko units and quantity units in marugu.

        # HOWEVER, the 'Sample Output 1' gives TWO lines:

        # 3 0
        # 5 0

        # Where sum a_i * b_i from input is:
        # 2*1 + 1*3 + 2*2 = 2 + 3 + 4 = 9

        # Output weights sum: 3 + 5 = 8 ?

        # Output quantities are 0 meaning quantity=1 each.

        # Contradiction? Wait, sample output 1 is:
        # 3 0
        # 5 0

        # Sum of weights = 3 + 5 = 8 < 9 input total weight

        # Why? It means the problem is to output chunks in (a,b) such that sum a_i * 2^x * b_i * 2^y = input total mass.

        # The problem gives no x,y and no transformations, so likely a_i and b_i are exponents for 2^x and 2^y:

        # Actually problem statement says:

        # "x" is the exponent in the weight unit 2^x grams

        # Similarly for y

        # Each chunk weight = a_i * 2^x grams

        # Number of item = b_i * 2^y

        # So total mass from chunk i = a_i * 2^x * b_i * 2^y = a_i * b_i * 2^{x+y}

        # But x,y are unknown but same for all

        # So total mass = (sum a_i * b_i) * 2^{x+y}

        # Since 2^{x+y} is constant but unknown, as is x,y >=0, to minimize chunk count

        # The problem is to express sum over chunks: a_i*b_i with minimal number of chunks a_j*b_j with total sum equal.

        # The solution is to find minimal partition of sum(a_i * b_i)

        # Which equals minimal number of addends adding to sum.

        # Minimum chunks = number of 1s in the binary representation of sum(a_i*b_i)

        # Because each chunk has weight and quantity in units of powers of two.

        # So minimal chunk count equals popcount of sum(a_i*b_i).

        # Each chunk corresponds to a power of two.

        # So, decompose total sum = sum of powers of 2, output each power as a chunk with a_j = power and b_j = 0

        # But as sample output 1 shows output 3 0 and 5 0, sums to 8, but input sum is 9

        # Sample input 1: (2 1, 1 3, 2 2)

        # sum a_i * b_i = 2*1 + 1*3 + 2*2 = 2 + 3 + 4 = 9

        # Output is 3 0 and 5 0, sum 3 +5 =8 not 9 : discrepancy

        # re-check sample output 1: "3 0" and "5 0" ?

        # The problem's sample output seems inconsistent as posted?

        # Wait original output is:

        # Sample Output 1
        # 3 0
        # 5 0

        # That's 3 and 5 weight with zero quantity, zero quantity means 2^0=1 item each chunk

        # Total weight = sum weight * quantity = (3 * 1) + (5 * 1) = 8

        # Input total mass = 9 ? 

        # There's a note in the problem statement or a discrepancy ?

        # Ah, re-check problem statement:

        # Output must be sorted by weight ascending.

        # Perhaps the minimal number of chunks are those that when merged by common divisors.

        # Another idea: sum all total weights = sum_i a_i * b_i

        # Output chunks weight and quantity b_j (marugu units) that multiply to the elements of binary representation of total weight.

        # Maybe quantity b_j might be non-zero.

        # But problem output has only zeros in output samples, might mean quantity fixed 1.

        # Possibly, we can store total weight as sum of powers of two (numbers with quantity=0)

        # 9 = 8 + 1

        # So output chunks with weight 1 and 8

        # but sample output is 3 and 5

        # 3 + 5 = 8 only

        # So is it typo in sample output ?

        # Maybe 3 and 5 are a and b are exponent indices, not exact number.

        # Guess: a_i and b_i are exponents for 2^x and 2^y

        # Then weight per chunk: mass_i = 2^{a_i} * 2^{b_i} = 2^{a_i + b_i}

        # So mass per chunk is 2^{a_i + b_i}. So mass is just power of 2.

        # So input lines give exponents a_i,b_i.

        # Sample input 1:

        # 3
        # 2 1  -> mass = 2^{2+1} = 2^3 =8
        # 1 3  -> mass = 2^{1+3} = 2^4 = 16
        # 2 2  -> mass = 2^{2+2} =2^4=16

        # Total mass = 8 + 16 +16 = 40

        # Output 3 0 and 5 0 means:

        # 2^{3+0}=8 and 2^{5+0}=32

        # sum = 8+32 =40

        # This matches total mass!

        # So the input and output units represent powers of 2 on exponentials.

        # The problem states:

        # weight = 2^a, quantity =2^b, total mass per chunk = 2^{a+b}

        # The problem wants minimal number of chunks such that sum of 2^{a_j + b_j} = total mass.

        # Since mass is a power of 2 exponent, it's sum of powers of two.

        # Thus, we get total mass exponent by summing 2^{a_i + b_i}.

        # Then minimal chunk number is popcount of total mass.

        # Then output chunks with a and b where a+b is exponent of each bit set in total mass.

        # How to split exponent into a and b?

        # Output requires a_j, b_j such that a_j+b_j equals the bit position.

        # Since problem wants minimal chunks = popcount, we can in output set b_j=0 for all, a_j=bit positions

        # Or set a_j=bit positions, b_j=0

        # So final output is output bits of total mass as pairs (a_j,b_j)

        # Sample output 1:

        # bits in 40 (binary 101000):

        # positions (zero-based): bits set at 3 and 5 (counting from LSB as position 0)

        # bit 3: 8

        # bit 5: 32

        # output:

        # 3 0

        # 5 0

        # Exactly sample output.

        # Therefore the problem is to:

        # 1. compute total mass = sum 2^{a_i + b_i}

        # 2. decompose total mass into powers of two

        # 3. for each power of two set bit at position k output a chunk a_j=k, b_j=0 sorting by a_j ascending

        # Now implement this.

class InputProcessor:
    """
    Parses input data into appropriate objects.
    """

    def __init__(self):
        self.N: int = 0
        self.exponents: List[Tuple[int,int]] = []

    def read_input(self):
        self.N = int(input())
        for _ in range(self.N):
            a_i, b_i = map(int, input().split())
            self.exponents.append((a_i, b_i))

class AlloyRecyclingSolver:
    """
    Solution solver operating on exponents to minimize chunk count.
    """

    def __init__(self, exponent_pairs: List[Tuple[int,int]]):
        self.exponent_pairs = exponent_pairs

    def total_mass_bitsum(self) -> int:
        total = 0
        for a,b in self.exponent_pairs:
            total += 2 ** (a + b)
        return total

    def decompose_mass(self, total_mass: int) -> List[Tuple[int,int]]:
        """
        Decompose total_mass (integer) into powers of two.
        Return list of (a_j,b_j) pairs such that a_j + b_j = bit position.
        Choose b_j=0 for minimal complexity.
        """
        chunks = []
        bit_pos = 0
        while total_mass > 0:
            if total_mass & 1:
                chunks.append((bit_pos, 0))
            total_mass >>= 1
            bit_pos += 1
        return sorted(chunks,key=lambda x: x[0])

    def solve(self) -> List[Tuple[int,int]]:
        total_mass = self.total_mass_bitsum()
        return self.decompose_mass(total_mass)

def main():
    input_processor = InputProcessor()
    input_processor.read_input()

    solver = AlloyRecyclingSolver(input_processor.exponents)
    answer = solver.solve()
    for a, b in answer:
        print(a, b)

if __name__ == '__main__':
    main()