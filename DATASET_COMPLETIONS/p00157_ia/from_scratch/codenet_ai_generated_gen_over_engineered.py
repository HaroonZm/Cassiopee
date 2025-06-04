from typing import List, Tuple, Optional, Iterator
import sys

class Doll:
    __slots__ = ['height', 'radius']
    def __init__(self, height: int, radius: int):
        self.height = height
        self.radius = radius

    def can_contain(self, other: 'Doll') -> bool:
        return self.height > other.height and self.radius > other.radius

    def __repr__(self):
        return f"Doll(h={self.height}, r={self.radius})"

class MatryoshkaSet:
    def __init__(self, dolls: List[Doll]):
        self.dolls = dolls

    def __len__(self):
        return len(self.dolls)

    def __iter__(self):
        return iter(self.dolls)

    def __repr__(self):
        return f"MatryoshkaSet({self.dolls})"

    def merge(self, other: 'MatryoshkaSet') -> 'MatryoshkaSet':
        # Combine dolls lists, no sorting here as the main solver will handle sorting and dp
        combined = self.dolls + other.dolls
        return MatryoshkaSet(combined)

class NestingDollSolver:
    def __init__(self, matryoshka1: MatryoshkaSet, matryoshka2: MatryoshkaSet):
        self.matryoshka1 = matryoshka1
        self.matryoshka2 = matryoshka2
        self.all_dolls = self.matryoshka1.merge(self.matryoshka2).dolls

    def _sort_dolls_desc(self):
        # Sort dolls descending by height then radius for correct nesting order
        self.all_dolls.sort(key=lambda d: (d.height, d.radius), reverse=True)

    def _calculate_longest_nesting(self) -> int:
        n = len(self.all_dolls)
        # dp[i] = length of longest nesting doll sequence starting at i
        dp = [1]*n

        for i in range(n):
            for j in range(i):
                if self.all_dolls[j].can_contain(self.all_dolls[i]):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
        return max(dp) if dp else 0

    def solve(self) -> int:
        self._sort_dolls_desc()
        max_nested = self._calculate_longest_nesting()
        return max_nested

class InputParser:
    def __init__(self, stream: Optional[Iterator[str]] = None):
        self.stream = stream or sys.stdin

    def __iter__(self):
        return self

    def __next__(self) -> Tuple[MatryoshkaSet, MatryoshkaSet]:
        line = None
        while True:
            line = self._safe_readline()
            if line is None:
                raise StopIteration
            if line.strip() == '':
                continue
            if line.strip() == '0':
                raise StopIteration
            else:
                break

        n = int(line)
        dolls1 = self._read_dolls(n)
        m_line = self._safe_readline()
        if m_line is None:
            raise StopIteration
        m = int(m_line)
        dolls2 = self._read_dolls(m)
        return MatryoshkaSet(dolls1), MatryoshkaSet(dolls2)

    def _safe_readline(self) -> Optional[str]:
        if isinstance(self.stream, list) or isinstance(self.stream, tuple):
            # If the input is a list (for testing), pop front
            if not self.stream:
                return None
            return self.stream.pop(0)
        else:
            return self.stream.readline()

    def _read_dolls(self, count: int) -> List[Doll]:
        dolls = []
        for _ in range(count):
            line = None
            while True:
                line = self._safe_readline()
                if line is None:
                    raise ValueError("Unexpected end of input during dolls reading")
                if line.strip() == '':
                    continue
                else:
                    break
            h, r = map(int, line.strip().split())
            dolls.append(Doll(h, r))
        return dolls

def main():
    parser = InputParser()
    results = []
    for mat1, mat2 in parser:
        solver = NestingDollSolver(mat1, mat2)
        max_k = solver.solve()
        # k must be greater than max(n,m) or otherwise maximum achievable nesting length
        # The problem states if k > max(n,m), the objective achieved.
        # But we output k as max nesting possible given combined dolls.
        results.append(str(max_k))
    print('\n'.join(results))

if __name__ == '__main__':
    main()