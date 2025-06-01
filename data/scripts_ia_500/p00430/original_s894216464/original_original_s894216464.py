def solve():
    answers = []
    def square(ans, rest, limit):
        if rest == 0:
            answers.append(' '.join(map(str, ans)))
        else:
            for i in range(rest, 0, -1):
                if i > limit:
                    continue
                square(ans + [i], rest - i, i)
    
    import sys
    for n in map(int, sys.stdin):
        if n == 0:
            break
        square([], n, n)
    
    print('\n'.join(answers))

solve()