import sys
import itertools
import operator
import functools

def solve(X: int, Y: int, Z: int):
    args = (X, Y, Z)
    indices = [2, 0, 1]
    result = tuple(operator.getitem(args, i) for i in indices)
    print(*result)

def main():
    tokens = functools.reduce(
        lambda z, y: itertools.chain(z, y),
        map(str.split, sys.stdin),
        []
    )
    tokens_iter = iter(tokens)
    input_values = list(
        map(int, itertools.islice(tokens_iter, 3))
    )
    functools.partial(solve, *input_values)()
    
if __name__ == '__main__':
    list(map(lambda f: f(), [main]))