from functools import reduce
from itertools import count, islice
from operator import add

def main():
    ask = lambda: int(input())
    e = [ask(), ask(), ask()]
    finder = (
        lambda x13: (
            lambda v: [
                e[0], e[1], x13,
                v - e[0] - (v - x13 - e[2]),
                e[2], v - (v - e[0] - (v - x13 - e[2])) - e[2],
                v - x13 - e[2], v - e[1] - e[2], v - x13 - (v - (v - e[0] - (v - x13 - e[2])) - e[2])
            ]
        )(reduce(add, (e[0], e[1], x13)))
    )
    valid = lambda L: (
        sum(L[6:9]) == sum(L[:3]) and
        sum(L[0::4]) == sum(L[:3])
    )
    next(islice((L for x13 in count() if valid((L := finder(x13))), 1), 1))
    print('\n'.join(' '.join(map(str, finder(x13)[i*3:i*3+3])) for i in range(3)))

if __name__ == '__main__':
    main()