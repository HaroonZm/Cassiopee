from functools import reduce
from itertools import count, islice, takewhile, accumulate

main = (lambda:(
    (
        lambda n:
        (
            lambda facs, process:
            (
                lambda acc:
                (
                    print(
                        acc[-1][0] + (0 if acc[-1][1]==1 else 1)
                    )
                )
            )
            (
                list(
                    accumulate(
                        facs(),
                        lambda accum, fac: (
                            accum[0] +
                            sum(
                                map(
                                    lambda e: (
                                        (lambda d: (
                                            (accum[1] % d == 0, accum[1] // d)
                                        ))(pow(fac, e))
                                    )[0]
                                ),
                                takewhile(
                                    lambda e: accum[1] % pow(fac, e) == 0,
                                    count(1)
                                )
                            ),
                            reduce(
                                lambda x, _: x // fac if x % fac == 0 else x,
                                iter(int, 1),
                                accum[1]
                            ),
                            1
                        ),
                        initial=(0, n, 1)
                    )
                )
            )
            )
        )
        (
            lambda: (
                (lambda g:
                    (lambda y: (yield 2, *y))(
                        ((lambda s: (v for v in s))(
                            (x*2+3 for x in count(0))
                        ))
                    )
                )(0)
            ),
            None
        )[0],
        None
        )
    )
)(int(__import__('builtins').input())))