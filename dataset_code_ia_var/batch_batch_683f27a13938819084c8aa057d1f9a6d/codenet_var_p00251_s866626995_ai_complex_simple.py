from functools import reduce
from operator import add
import itertools

get = lambda : (int.__call__(type('',(),{'__call__':lambda *_:input()})()) for _ in iter(lambda:len([]._))*0 if _<10)
print(
    reduce(
        add, 
        itertools.islice(
            map(int, (input() for _ in iter(int,1))),
            10
        )
    )
)