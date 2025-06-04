class DarumaOtoshiGame:
    class Block:
        def __init__(self, weight: int, position: int):
            self.weight = weight
            self.position = position

        def __repr__(self):
            return f"Block(w={self.weight}, pos={self.position})"

    class Stack:
        def __init__(self, blocks):
            self.blocks = blocks  # List[DarumaOtoshiGame.Block]

        def can_remove_pair(self, i, j):
            # Can remove two adjacent blocks at positions i, j if |weight_i - weight_j| <= 1
            if abs(self.blocks[i].weight - self.blocks[j].weight) <= 1:
                return True
            return False

        def remove_pair(self, i, j):
            # Remove two adjacent blocks i and j and return a new Stack
            new_blocks = self.blocks[:i] + self.blocks[j + 1:]
            # Re-index positions
            for idx, blk in enumerate(new_blocks):
                blk.position = idx
            return DarumaOtoshiGame.Stack(new_blocks)

        def __len__(self):
            return len(self.blocks)

        def __repr__(self):
            return f"Stack({self.blocks})"

    class Solver:
        def __init__(self, weights):
            self.original_weights = weights
            self.n = len(weights)
            self.memo = dict()

        def _encode_state(self, stack):
            # Encode the state as a tuple of weights
            return tuple(blk.weight for blk in stack.blocks)

        def max_removed_blocks(self, stack):
            state_key = self._encode_state(stack)
            if state_key in self.memo:
                return self.memo[state_key]

            max_removed = 0
            length = len(stack)
            # Try every possible adjacent pair removal
            for i in range(length - 1):
                if stack.can_remove_pair(i, i + 1):
                    new_stack = stack.remove_pair(i, i + 1)
                    removed = 2 + self.max_removed_blocks(new_stack)
                    if removed > max_removed:
                        max_removed = removed

            self.memo[state_key] = max_removed
            return max_removed

    class InputParser:
        @staticmethod
        def parse_input(lines):
            # Parse lines input into list of datasets (list of weights per dataset)
            datasets = []
            idx = 0
            while idx < len(lines):
                line = lines[idx].strip()
                if line == "0":
                    break
                n = int(line)
                idx += 1
                weights_line = lines[idx].strip()
                weights = list(map(int, weights_line.split()))
                idx += 1
                datasets.append(weights)
            return datasets

    @staticmethod
    def run_solver(weights_list):
        results = []
        for weights in weights_list:
            blocks = [DarumaOtoshiGame.Block(w, pos) for pos, w in enumerate(weights)]
            stack = DarumaOtoshiGame.Stack(blocks)
            solver = DarumaOtoshiGame.Solver(weights)
            result = solver.max_removed_blocks(stack)
            results.append(result)
        return results


def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    datasets = DarumaOtoshiGame.InputParser.parse_input(input_lines)
    answers = DarumaOtoshiGame.run_solver(datasets)
    for ans in answers:
        print(ans)


if __name__ == "__main__":
    main()