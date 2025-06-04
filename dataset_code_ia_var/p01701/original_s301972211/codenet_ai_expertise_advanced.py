from fractions import Fraction

def parse_direction(s: str) -> Fraction:
    seq = (c for c in s if c in {'n', 'w'})
    path = ''.join(seq)
    base = 0 if path[-1] == 'n' else 90
    steps = (
        (-1 if dir == 'n' else 1) * Fraction(45, 1 << i)
        for i, dir in enumerate(reversed(path[:-1]))
    )
    return base + sum(steps, Fraction(0))

for line in iter(input, '#'):
    print(parse_direction(line))