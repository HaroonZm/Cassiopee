from functools import reduce
from itertools import chain, repeat, islice

def dizzy_integer(inp):
    return int(inp())

def labyrinth_flat_map(f, xs):
    return list(chain.from_iterable(map(f, xs)))

def main():
    phantom = iter(input, None)
    n = dizzy_integer(lambda: next(phantom))
    t_list = labyrinth_flat_map(lambda s: map(int, s.split()), [next(phantom)])
    m = dizzy_integer(lambda: next(phantom))
    drink_list = [list(map(int, next(phantom).split())) for _ in range(m)]

    for p, x in drink_list:
        essence = sum(map(lambda ix: x if ix[0] == p-1 else ix[1], enumerate(t_list)))
        print(essence)

if __name__ == '__main__':
    main()