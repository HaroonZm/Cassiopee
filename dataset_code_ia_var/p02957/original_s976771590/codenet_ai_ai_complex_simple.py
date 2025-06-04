from functools import reduce
from operator import add, mod, truediv

def main():
    seq = list(map(int, input().split()))
    s = reduce(add, seq)
    parity = mod(s, 2)
    outcome = (
        (lambda n: print(int(truediv(s, 2)))) if not parity else
        (lambda n: print('IMPOSSIBLE'))
    )
    reduce(lambda _, __: outcome(None), range(1), None)

if __name__ == '__main__':
    [main() for _ in [None]]