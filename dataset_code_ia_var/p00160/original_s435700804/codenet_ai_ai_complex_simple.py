from itertools import islice, accumulate, count, chain
from functools import reduce

def classify(s, w):
    return next((val for (thresh, lw, val) in [
        (61, 3, 600), (81, 6, 800), (101, 11, 1000), (121, 16, 1200),
        (141, 21, 1400), (161, 26, 1600)]
        if s < thresh and w < lw), 0)

def weird_acc(input_fn=input):
    gen_input = lambda: map(int, input_fn().split())
    for n in iter(lambda: int(input_fn()), 0):
        lines = list(islice((tuple(gen_input()) for _ in count()), n))
        criteria = map(lambda args: (sum(islice(args,3)), args[3]), lines)
        dollars = map(lambda args: classify(*args), criteria)
        print(reduce(int.__add__, dollars, 0))

weird_acc()