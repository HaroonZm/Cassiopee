from functools import reduce
from itertools import groupby, chain

try:
    while (lambda: True)():
        s = input()
        if any(map(lambda x: x == "#", [s])):
            break

        field = list(
            map(
                lambda row: list(
                    chain.from_iterable(
                        map(
                            lambda ch: ['b'] if ch == 'b' else ['.'] * int(ch),
                            row
                        )
                    )
                ),
                s.split('/')
            )
        )

        a, b, c, d = map(int, input().split())
        list(map(lambda x: x.__setitem__(b - 1 if i == a - 1 else d - 1, '.' if i == a - 1 else 'b'), [field[i]]) \
             for i in [a - 1, c - 1])

        print(
            '/'.join(
                map(
                    lambda row: 'b'.join(
                        filter(
                            None,
                            map(
                                lambda group: str(len(list(group[1]))) if group[0] == '.' else '',
                                groupby(row)
                            )
                        )
                    ),
                    field
                )
            )
        )
except EOFError:
    pass