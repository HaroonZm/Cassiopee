from functools import reduce
from itertools import chain, islice, repeat
import sys

def main():
    m, k = map(int, input().split())
    lim = 1 << m

    def _err(): print(-1); sys.exit(0)

    (lambda:
        (lambda: print('0 0'), lambda: _err())[k != 0]() if m == 0 else
        (lambda: print('0 0 1 1'), lambda: _err())[k == 0]( ) if m == 1 else
        (lambda:
            (lambda arr:
                print(' '.join(map(str, arr)))
            )(
                reduce(
                    lambda a, b: a + b,
                    (
                        [k],
                        list(islice((i for i in range(lim) if i != k), 0, k)),
                        list(islice(reversed([i for i in range(lim) if i != k]), 0, lim - k -1)),
                        [k],
                    )
                )
            )
        )()
    )() if k < lim else _err()

main()