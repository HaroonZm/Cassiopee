def solve():
    import sys
    from itertools import takewhile

    def square(ans, rest, limit):
        if rest == 0:
            yield ans
            return
        yield from (result for i in range(min(rest, limit), 0, -1)
                    for result in square(ans + [i], rest - i, i))

    answers = ( ' '.join(map(str, partition))
                for n in map(int, sys.stdin) if n != 0
                for partition in square([], n, n) )

    print('\n'.join(answers))

solve()