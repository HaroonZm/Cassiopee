from dataclasses import dataclass, field
import sys

BIG_NUM = 2_000_000_000
HUGE_NUM = 99_999_999_999_999_999
MOD = 1_000_000_007
EPS = 1e-9
sys.setrecursionlimit(100_000)

@dataclass(order=True, slots=True, frozen=True)
class Info:
    sort_index: tuple = field(init=False, repr=False)
    name: str
    index: int
    value: int

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', (-self.value, self.index))

def main():
    first = True
    it = iter(sys.stdin.readline, '')
    while True:
        try:
            line = next(it)
        except StopIteration:
            break
        N = int(line)
        if N == 0:
            break
        if not first:
            print()
        first = False

        infos = [
            Info(
                name,
                idx,
                3 * int(win) + int(draw)
            )
            for idx, (name, win, lose, draw)
            in enumerate(
                (input().split() for _ in range(N))
            )
        ]
        for info in sorted(infos):
            print(f"{info.name},{info.value}")

if __name__ == "__main__":
    main()