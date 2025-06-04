class LinearCongruentialGenerator:
    def __init__(self, a: int, b: int, c: int, seed: int):
        self.a = a
        self.b = b
        self.c = c
        self.current = seed

    def next(self) -> int:
        self.current = (self.a * self.current + self.b) % self.c
        return self.current

    def reset(self, seed: int):
        self.current = seed


class ReelCondition:
    def __init__(self, target_value: int):
        self.target_value = target_value

    def matches(self, value: int) -> bool:
        return self.target_value == value


class FrameAnalyzer:
    MAX_FRAMES = 10000

    def __init__(self, n: int, lcg: LinearCongruentialGenerator, conditions: list[ReelCondition]):
        self.n = n
        self.lcg = lcg
        self.conditions = conditions

    def find_min_frame(self) -> int:
        '''
        Returns the minimal frame count (1-based) at which all reels can be stopped
        with the respective target values on the RNG sequence. Returns -1 if impossible
        within MAX_FRAMES.
        '''
        # The stopping process requires N button presses, exactly one per reel in left-right order.
        # Frame counting is 1-based per problem statement.
        # However, if the needed value for a reel is exactly the initial RNG value, 
        # we can consider that reel stopped at frame 0 (without waiting).
        current_rng_value = self.lcg.current
        time = 0
        # We will simulate frame by frame the RNG values, keeping track when each reel can be stopped.
        # For reel i, we want to find the earliest frame >= time + 1 (because pressing stops leftmost)
        # where RNG matches conditions[i].target_value.
        # Then update time to that frame index.
        for i in range(self.n):
            target = self.conditions[i].target_value
            if i == 0 and current_rng_value == target:
                # Can stop first reel immediately, no wait
                continue
            # Otherwise we must find the earliest frame > time where RNG == target
            found_frame = -1
            # We continue RNG sequence from frame (time+1)
            # Let's compute the RNG after time frames since seed:
            # We don't reset RNG, but we can simulate frame by frame for clarity
            # Save current RNG and restore after search to avoid side effects
            saved_state = self.lcg.current
            # Advance RNG to frame time (run RNG for 'time' times because current is initial)
            self.lcg.current = current_rng_value
            for _ in range(time):
                self.lcg.next()
            # From frame time+1 to MAX_FRAMES search for matching target
            for frame in range(time + 1, self.MAX_FRAMES + 1):
                val = self.lcg.next()
                if val == target:
                    found_frame = frame
                    break
            self.lcg.current = saved_state
            if found_frame == -1:
                return -1
            time = found_frame
        return time


class SlotMachineSolver:
    def __init__(self):
        self.results = []

    def parse_and_solve(self, input_lines: list[str]):
        index = 0
        while True:
            if index >= len(input_lines):
                break
            line = input_lines[index].strip()
            index += 1
            if not line:
                continue
            n_a_b_c_x = list(map(int, line.split()))
            if len(n_a_b_c_x) != 5:
                # Malformed input, ignore or break
                break
            n, a, b, c, x = n_a_b_c_x
            if n == 0 and a == 0 and b == 0 and c == 0 and x == 0:
                break  # end of input
            if index >= len(input_lines):
                break
            condition_line = input_lines[index].strip()
            index += 1
            y_list = list(map(int, condition_line.split()))
            if len(y_list) != n:
                # malformed input
                break
            lcg = LinearCongruentialGenerator(a, b, c, x)
            conditions = [ReelCondition(y) for y in y_list]
            analyzer = FrameAnalyzer(n, lcg, conditions)
            res = analyzer.find_min_frame()
            self.results.append(res)

    def output_results(self):
        for res in self.results:
            print(res)


def main():
    import sys
    solver = SlotMachineSolver()
    solver.parse_and_solve(sys.stdin.readlines())
    solver.output_results()


if __name__ == "__main__":
    main()