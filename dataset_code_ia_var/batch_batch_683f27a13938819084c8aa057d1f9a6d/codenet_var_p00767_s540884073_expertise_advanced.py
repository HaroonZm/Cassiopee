from dataclasses import dataclass, field
from functools import total_ordering

@total_ordering
@dataclass(order=False, frozen=True, slots=True)
class T:
    h: int
    w: int
    d: int = field(init=False)
    
    def __post_init__(self):
        object.__setattr__(self, 'd', self.h * self.h + self.w * self.w)
    
    def __lt__(self, other):
        return (self.d, self.h) < (other.d, other.h)
    
    def __eq__(self, other):
        return (self.h, self.w, self.d) == (other.h, other.w, other.d)

from bisect import bisect_right

t = [T(i, j) for i in range(1, 151) for j in range(i + 1, 151)]
t.sort()

try:
    while True:
        h, w = map(int, input().split())
        if not (h or w):
            break
        hw = T(h, w)
        idx = bisect_right(t, hw)
        if idx < len(t):
            print(f"{t[idx].h} {t[idx].w}")
except EOFError:
    pass