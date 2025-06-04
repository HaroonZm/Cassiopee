def solve():
    from sys import stdin
    f_i = stdin

    n = int(f_i.readline())
    A_s = f_i.readline().rstrip()

    if n == 1:
        print(A_s)
    else:
        A = tuple(map(int, A_s.split()))
        from itertools import permutations
        lex = tuple(permutations(range(1, n + 1), n))
        from bisect import bisect_left
        idx = bisect_left(lex, A)
        if idx == 0:
            print(A_s)
            print(' '.join(map(str, lex[idx + 1])))
        elif idx == len(lex) - 1:
            print(' '.join(map(str, lex[idx - 1])))
            print(A_s)
        else:
            print(' '.join(map(str, lex[idx - 1])))
            print(A_s)
            print(' '.join(map(str, lex[idx + 1])))

solve()