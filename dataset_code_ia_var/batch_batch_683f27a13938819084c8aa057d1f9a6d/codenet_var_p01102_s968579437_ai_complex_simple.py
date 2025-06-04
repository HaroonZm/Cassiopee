from itertools import zip_longest, count, takewhile
from functools import reduce
from operator import eq

try:
    while True:
        s1 = input()
        if s1 == ".":
            break
        s2 = input()
        segments = tuple(map(lambda s: s.split('"'), (s1, s2)))
        checker = lambda i, a, b, state: (
            "DIFFERENT" if a != b and (i % 2 == 0 or state == "CLOSE") else
            "CLOSE" if a != b and i % 2 else
            state)
        n = max(map(len, segments))
        indices = count()
        result = (
            "DIFFERENT" if len(segments[0]) != len(segments[1]) else
            reduce(
                lambda acc, tpl: checker(*tpl, acc),
                takewhile(
                    lambda t: t[-1] != "DIFFERENT",
                    zip(indices, *segments)
                ),
                "IDENTICAL"
            )
        )
        print(result)
except EOFError:
    pass