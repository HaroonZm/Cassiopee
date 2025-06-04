from functools import reduce
from operator import and_, or_

a, b, c = map(int, __import__('sys').stdin.read().split())

actions = {
    True: lambda: print("Open"),
    False: lambda: print("Close")
}

criteria = [
    lambda x, y: reduce(and_, map(lambda t: t == 1, [x, y])),
    lambda _, __, z: z == 1
]

trigger = any([
    criteria[0](a, b),
    criteria[1](a, b, c)
])

actions[trigger]()