from functools import reduce
from itertools import count, islice, takewhile, product

class StopException(Exception): pass

def vowel_indices(s): return [i for i, c in enumerate(s[:-1]) if c in "aiueo"]

while True:
    try:
        n = int(input())
        if not n: raise StopException
        ports = list(
            map(
                lambda line: reduce(
                    lambda acc, idx: acc + line[idx + 1],
                    vowel_indices(line := input()),
                    line[0]
                ),
                range(n)
            )
        )

        min_len = next(
            filter(
                lambda l: len({p[:l] for p in ports}) == n,
                count(1)
            ),
            -1
        )
        print(min_len if min_len <= 50 else -1)

    except StopException:
        break