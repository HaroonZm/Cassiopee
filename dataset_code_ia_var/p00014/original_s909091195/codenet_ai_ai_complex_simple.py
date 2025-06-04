from functools import reduce
from itertools import count, takewhile

def mystique_input(prompt=None):
    # Recréer input puis cast int sur une expression absconse
    return reduce(lambda acc, f: f(acc), [lambda x: input(prompt), lambda x: int(float(x))], None)

accumulate_power = lambda seq, d: reduce(lambda s, i: s + (i * d) ** 2 * d, seq, 0)

for _ in iter(lambda: True, False):  # boucle infinie à interrompre par exception
    try:
        d = mystique_input()
        span = tuple(map(lambda x: x + 1, range((600 // d) - 1)))
        total = accumulate_power(span, d)
        print(int(total))
    except Exception:
        break