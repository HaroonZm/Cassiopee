from functools import reduce
from itertools import groupby, cycle
import operator

def main():
    s = list(map(str, input()))
    unique_count = len(set(s))
    result = (
        (lambda: (
            next(
                cycle(
                    ("First", "Second")
                ) if operator.eq(s[0], s[-1]) else cycle(
                    ("Second", "First")
                )
            ) if len(s) % 2 else (
                next(
                    cycle(
                        ("First", "Second")
                    )
                ) if operator.eq(s[0], s[-1]) else next(cycle(("Second", "First")))
            )
        ))()
        if unique_count != 2 else "Second"
    )
    print(result)

if __name__ == "__main__":
    main()