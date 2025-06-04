from typing import List, Tuple, Optional

class AmidaLine:
    def __init__(self, index: int):
        self.index = index
        self.connections = dict()  # height -> connected line

    def add_connection(self, height: int, other_index: int):
        self.connections[height] = other_index

    def __repr__(self):
        return f"AmidaLine({self.index}, connections={self.connections})"

class HorizontalLine:
    def __init__(self, height: int, left: int, right: int):
        self.height = height
        # Ensure left < right for consistency
        self.left = min(left, right)
        self.right = max(left, right)

    def connects(self, line_idx: int, height: int) -> Optional[int]:
        # Returns the opposite line index if this horizontal line connects to line_idx at height
        if self.height != height:
            return None
        if line_idx == self.left:
            return self.right
        elif line_idx == self.right:
            return self.left
        return None

    def __repr__(self):
        return f"HLine(h={self.height}, {self.left}<->{self.right})"

class AmidaLadder:
    def __init__(self, num_lines: int, horizontal_lines: List[HorizontalLine]):
        self.num_lines = num_lines
        self.horizontal_lines = horizontal_lines
        # We'll organize horizontal lines by their height for quick access
        self.height_lines_map = self._organize_lines()

    def _organize_lines(self) -> dict:
        # Maps height to list of horizontal lines at that height (for efficiency)
        mapping = dict()
        for hl in self.horizontal_lines:
            mapping.setdefault(hl.height, []).append(hl)
        return mapping

    def trace_line(self, start_line: int) -> int:
        # We must track the traversal from top to bottom.
        # Since heights can be arbitrary, get all heights sorted ascending.
        all_heights = sorted(self.height_lines_map.keys())

        current_line = start_line
        for height in all_heights:
            # Check if at this height there is a horizontal line connecting current_line
            h_lines_at_height = self.height_lines_map[height]
            # Since no two horizontal lines at the same height touch the same line,
            # at most one line will connect to current_line.
            moved = False
            for hl in h_lines_at_height:
                opposite = hl.connects(current_line, height)
                if opposite is not None:
                    current_line = opposite
                    moved = True
                    break
            # If no horizontal line at height connects current_line, continue down without change
        return current_line

class AmidaElectionProcessor:
    def __init__(self):
        self.datasets = []

    def add_dataset(self, n: int, m: int, a: int, horizontal_data: List[Tuple[int,int,int]]):
        horizontal_lines = [HorizontalLine(h,p,q) for (h,p,q) in horizontal_data]
        self.datasets.append( (n,m,a,horizontal_lines) )

    def process_all(self) -> List[int]:
        results = []
        for n,m,a,horizontal_lines in self.datasets:
            ladder = AmidaLadder(n, horizontal_lines)
            winner_line = ladder.trace_line(a)
            results.append(winner_line)
        return results

class AmidaInputParser:
    @staticmethod
    def parse(input_lines: List[str]) -> AmidaElectionProcessor:
        processor = AmidaElectionProcessor()
        idx = 0
        while True:
            if idx >= len(input_lines):
                break
            line = input_lines[idx].strip()
            idx += 1
            if not line:
                continue
            nma = line.split()
            if len(nma) != 3:
                continue
            n,m,a = map(int,nma)
            if n == 0 and m == 0 and a == 0:
                break
            horizontal_data = []
            for _ in range(m):
                hpl = input_lines[idx].strip().split()
                idx += 1
                h,p,q = map(int,hpl)
                horizontal_data.append( (h,p,q) )
            processor.add_dataset(n,m,a,horizontal_data)
        return processor

def main():
    import sys
    lines = sys.stdin.readlines()
    processor = AmidaInputParser.parse(lines)
    results = processor.process_all()
    for result in results:
        print(result)

if __name__ == "__main__":
    main()