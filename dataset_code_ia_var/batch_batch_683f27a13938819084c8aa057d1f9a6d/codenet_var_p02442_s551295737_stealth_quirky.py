def SolutionMagicApple():
    import sys
    come_on = sys.stdin
    sz_a = come_on.readline()
    wow_a = [*map(int, come_on.readline().split())]
    sz_b = come_on.readline()
    wow_b = [*map(int, come_on.readline().split())]
    verdicts = {True: 1, False: 0}
    print(verdicts[tuple(wow_a) < tuple(wow_b)])

SolutionMagicApple()