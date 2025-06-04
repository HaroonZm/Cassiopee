from dataclasses import dataclass
from typing import Optional, List
import re
import sys

@dataclass(slots=True, frozen=True)
class Panel:
    name: str
    depth: int
    child: int
    x1: int
    y1: int
    x2: int
    y2: int

    def touch(self, x: int, y: int, depth: int) -> Optional['Panel']:
        if depth < self.depth and self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2:
            return self
        return None

    def __repr__(self):
        return f"{self.name} {self.child}"

def solve():
    input_iter = iter(sys.stdin.read().splitlines())
    panel_base = Panel("OUT OF MAIN PANEL", 0, 1, 0, 0, 10000, 10000)
    tag_re = re.compile(r"<([^>]+)>(\d+),(\d+),(\d+),(\d+)(.*?)</\1>")
    while True:
        try:
            N = int(next(input_iter))
        except StopIteration:
            break
        if N == 0:
            break
        S = next(input_iter)
        panels: List[Panel] = [panel_base]

        def rec(s: str, depth: int) -> int:
            count = 0
            idx = 0
            while idx < len(s):
                m = tag_re.match(s, idx)
                if not m:
                    break
                name, x1, y1, x2, y2, inside = m.group(1), *(int(m.group(i)) for i in range(2,6)), m.group(6)
                child = rec(inside, depth + 1)
                panels.append(Panel(name, depth, child, x1, y1, x2, y2))
                idx = m.end()
                count += 1
            return count

        rec(S, 1)

        for _ in range(N):
            x, y = map(int, next(input_iter).split())
            res = panels[0]
            for p in panels[1:]:
                res = p.touch(x, y, res.depth) or res
            print(res)

if __name__ == "__main__":
    solve()