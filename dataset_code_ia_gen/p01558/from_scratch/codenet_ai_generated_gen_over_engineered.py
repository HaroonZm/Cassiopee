import sys
import threading

class Query:
    __slots__ = ('delta_l', 'delta_r')
    def __init__(self, command: str):
        # Map the command to delta changes on l and r pointers
        self.delta_l = 0
        self.delta_r = 0
        if command == "L++":
            self.delta_l = +1
        elif command == "L--":
            self.delta_l = -1
        elif command == "R++":
            self.delta_r = +1
        elif command == "R--":
            self.delta_r = -1
        else:
            raise ValueError(f"Invalid query command: {command}")

class CoordinateManager:
    # Manage coordinate boundaries and validations for multiple queries
    def __init__(self, n: int):
        self.n = n
        self.l_values = []
        self.r_values = []

    def add_initial(self):
        self.l_values.append(1)
        self.r_values.append(1)

    def append(self, query: Query):
        l_prev = self.l_values[-1]
        r_prev = self.r_values[-1]
        l_new = l_prev + query.delta_l
        r_new = r_prev + query.delta_r
        # Enforce boundaries after each update to keep 1 ≤ l[k] ≤ r[k] ≤ n 
        # We will correct later if out of bounds, but problem states constraints always valid
        if l_new < 1 or r_new > self.n or l_new > r_new:
            # This is the problem's trust constraint; for safety:
            raise ValueError("Query results out of bounds or invalid substring range")
        self.l_values.append(l_new)
        self.r_values.append(r_new)

    def get_ranges(self):
        # Return all (l, r) for k in [1..m]
        return zip(self.l_values[1:], self.r_values[1:])

class RollingHash:
    # Implements double polynomial rolling hash with two mod bases
    __slots__ = ('s', 'n', 'base1', 'mod1', 'base2', 'mod2', 'hash1', 'hash2', 'pow1', 'pow2')
    def __init__(self, s: str):
        # Predefine bases and moduli - large primes
        self.s = s
        self.n = len(s)
        self.base1 = 911
        self.mod1 = 10**9 + 7
        self.base2 = 3571
        self.mod2 = 10**9 + 9
        self.hash1 = [0] * (self.n + 1)
        self.hash2 = [0] * (self.n + 1)
        self.pow1 = [1] * (self.n + 1)
        self.pow2 = [1] * (self.n + 1)
        self._build()

    def _build(self):
        for i in range(self.n):
            c = ord(self.s[i]) - ord('a') + 1
            self.hash1[i+1] = (self.hash1[i] * self.base1 + c) % self.mod1
            self.hash2[i+1] = (self.hash2[i] * self.base2 + c) % self.mod2
            self.pow1[i+1] = (self.pow1[i] * self.base1) % self.mod1
            self.pow2[i+1] = (self.pow2[i] * self.base2) % self.mod2

    def get_hash(self, l: int, r: int):
        # Return hash of s[l:r], 0-based indexing, excluding s[r]
        # Caller uses 1-based indexing and includes s[r], so adapt outside
        x1 = self.hash1[r] - self.hash1[l] * self.pow1[r - l] % self.mod1
        if x1 < 0:
            x1 += self.mod1
        x2 = self.hash2[r] - self.hash2[l] * self.pow2[r - l] % self.mod2
        if x2 < 0:
            x2 += self.mod2
        return (x1, x2)

class InputReader:
    # A wrapper class anticipating extensions on input format or preprocessing
    def __init__(self):
        self.n = 0
        self.m = 0
        self.s = ""
        self.queries = []

    def read(self):
        input_buffer = sys.stdin.read().split()
        self.n, self.m = map(int, input_buffer[0:2])
        self.s = input_buffer[2]
        self.queries = input_buffer[3:3+self.m]

class SubstringUniquenessProcessor:
    # The orchestrator abstracting characters, queries, substring extraction, and unique counting
    def __init__(self, n: int, m: int, s: str, queries: list):
        self.n = n
        self.m = m
        self.s = s
        self.queries = queries
        # Initialize component abstractions
        self.coordinate_manager = CoordinateManager(n)
        self.rolling_hash = RollingHash(s)

    def process(self) -> int:
        self.coordinate_manager.add_initial()
        # Parse queries as objects (abstraction anticipating new commands)
        query_objects = list(map(Query, self.queries))
        for q in query_objects:
            self.coordinate_manager.append(q)
        ranges = self.coordinate_manager.get_ranges()
        seen_hashes = set()
        # Compute hashes for each substring defined by l[k], r[k]
        # l and r are 1-based inclusive indices; convert to 0-based exclusive for rolling hash
        for l, r in ranges:
            # s[l-1:r] in 0-based indexing
            h = self.rolling_hash.get_hash(l - 1, r)
            seen_hashes.add(h)
        return len(seen_hashes)

def main():
    ir = InputReader()
    ir.read()
    processor = SubstringUniquenessProcessor(ir.n, ir.m, ir.s, ir.queries)
    answer = processor.process()
    print(answer)

# Run main in a thread for fast IO on large inputs
threading.Thread(target=main).start()