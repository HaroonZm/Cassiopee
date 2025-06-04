from functools import reduce
from itertools import count, islice

get_input = lambda: int(__import__('builtins').input())
to_str = lambda x: str(x)
display = lambda i: print("Case", f"{i + 1}:")
next_in = lambda: __import__('builtins').input()
digits = lambda n: to_str(int(n)**2).zfill(8)[2:6]
printer = lambda t: print(int(t))

def generator(val):
    return map(int, (to_str((int(val)**2)).zfill(8)[2:6] for _ in range(10)))

n = get_input()
list(map(
    lambda c:
        (display(c),
         reduce(lambda acc, _: printer((acc := to_str(int(acc)**2).zfill(8)[2:6])), range(10), next_in())
        ),
    range(n))
)