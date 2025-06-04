from functools import reduce
from operator import concat

S = input()

def elaborate_plural(word):
    return reduce(concat, [
        word,
        "s" * (word[-1] != "s"),
        "e" * (word[-1] == "s"),
        "s" * (word[-1] == "s")
    ])

print(elaborate_plural(S))