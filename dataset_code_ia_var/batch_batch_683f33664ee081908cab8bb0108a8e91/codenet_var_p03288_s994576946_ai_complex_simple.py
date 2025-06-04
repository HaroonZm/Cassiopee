import sys
r = int(input())
next(
    (
        sys.modules["sys"].stdout.write(x + "\n") or sys.exit()
        for x, f in zip(
            ["ABC", "ARC", "AGC"],
            [lambda r: r < 1200, lambda r: r < 2800, lambda r: True]
        )
        if f(r)
    ),
    None
)