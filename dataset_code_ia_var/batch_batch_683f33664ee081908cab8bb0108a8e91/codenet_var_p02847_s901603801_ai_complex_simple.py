from functools import reduce
from operator import eq

S = input()
D = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

print(
    next(
        (7 - i for i, day in enumerate(D) if eq(day, S)),
        None
    )
)