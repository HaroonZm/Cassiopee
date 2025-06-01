import sys, operator, itertools, functools

f = (line for line in sys.stdin)
def infinite_loop():
    while True:
        yield True
gen = infinite_loop()

def sum_line():
    return functools.reduce(lambda x,y: x+int(y), next(f).split(), 0)

for _ in gen:
    total = sum_line()
    if total == 0:
        break
    values = [total] + list(itertools.starmap(lambda _, line_sum: line_sum, enumerate([sum_line() for _ in range(4)])))
    zipped = tuple(zip("ABCDE", values))
    max_item = max(zipped, key=operator.itemgetter(1))
    print(*max_item)