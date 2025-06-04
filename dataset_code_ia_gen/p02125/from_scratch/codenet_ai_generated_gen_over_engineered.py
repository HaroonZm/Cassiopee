class BinaryRepresentation:
    def __init__(self, number: int):
        self.number = number

    def to_binary(self) -> str:
        if self.number == 0:
            return "0"
        bits = []
        num = self.number
        while num > 0:
            bits.append(str(num % 2))
            num //=2
        bits.reverse()
        return ''.join(bits)
    
class BitSumFunction:
    def __init__(self, binary_str: str):
        self.binary_str = binary_str
    
    def calculate(self) -> int:
        return sum(int(bit) for bit in self.binary_str)

class MaxBitSumCalculator:
    def __init__(self, limit: int):
        self.limit = limit

    def max_bit_sum(self) -> int:
        # Since f(x) is the count of 1s in binary representation of x,
        # the maximum is the maximum number of ones present in any number from 0 to N.
        # The best candidate is the number with all bits set to 1 just less or equal to N.
        # We find the highest bit of N, and create a number with that many bits set to 1 
        # and if that's > N, we reduce one bit at a time.
        
        # Abstract the process in a helper class:
        candidate_finder = MaxOnesCandidateFinder(self.limit)
        candidate = candidate_finder.find_candidate()
        bit_sum_fn = BitSumFunction(BinaryRepresentation(candidate).to_binary())
        return bit_sum_fn.calculate()

class MaxOnesCandidateFinder:
    def __init__(self, limit:int):
        self.limit = limit

    def find_candidate(self) -> int:
        # find highest bit of limit
        highest_bit = self.limit.bit_length()
        # make a number with all bits set to 1 with length highest_bit
        all_ones = (1 << highest_bit) - 1
        if all_ones <= self.limit:
            return all_ones
        # else try one bit less: number with highest_bit-1 bits set to 1
        return (1 << (highest_bit - 1)) -1

class InputHandler:
    def __init__(self):
        pass

    def read_input(self) -> int:
        return int(input().strip())

class OutputHandler:
    def __init__(self):
        pass

    def output(self, value: int):
        print(value)

class Solution:
    def __init__(self):
        self.input_handler = InputHandler()
        self.output_handler = OutputHandler()

    def run(self):
        n = self.input_handler.read_input()
        calculator = MaxBitSumCalculator(n)
        result = calculator.max_bit_sum()
        self.output_handler.output(result)

if __name__ == "__main__":
    Solution().run()