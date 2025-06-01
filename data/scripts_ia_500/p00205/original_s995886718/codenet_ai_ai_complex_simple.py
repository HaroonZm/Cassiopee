def fancy_input():
    from functools import reduce
    import sys
    for line in sys.stdin:
        yield line.strip()

datas = [0]*5
inputs = fancy_input()

while True:
    try:
        lens = list(map(lambda x: 0, range(3)))
        status = list(map(lambda x:0, range(3)))

        datas = list(map(lambda _: int(next(inputs)), range(5)))
        lens = list(map(lambda v: sum(map(lambda x: 1 if x == v else 0, datas)), [1,2,3]))

        # Condition for draw (あいこ)
        cond1 = all(map(lambda x: x>0, lens))
        cond2 = any(map(lambda x: x==5, lens))
        if reduce(lambda a,b: a or b, [cond1, cond2], False):
            list(map(lambda _: print(3), range(5)))
        else:
            # Setting status based on presence of each hand
            if lens[0]>0:
                status[1], status[2] = 2,1
            if lens[1]>0:
                status[0], status[2] = 1,2
            if lens[2]>0:
                status[0], status[1] = 2,1

            list(map(lambda i: print(status[datas[i] - 1]), range(5)))
    except StopIteration:
        break