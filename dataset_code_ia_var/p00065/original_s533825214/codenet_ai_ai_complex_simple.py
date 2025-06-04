from sys import stdin
from itertools import groupby, count, chain, tee
from operator import itemgetter, add

def ultra_counter(seq):
    # Returns a dict mapping int values to their counts
    return dict((x, sum(1 for _ in y)) for x, y in groupby(sorted(seq)))

def elaborate_data_struct():
    # Returns two lists accumulating the numbers
    streams = [[], []]
    index = 0
    for line in chain(stdin, ['\n']):  # Add trailing empty to process last group
        if line == '\n':
            index += 1
        elif index < 2:
            a, b = map(int, map(str.strip, line.split(',')))
            streams[index].append(a)
    return streams

def over_thought_process():
    streams = elaborate_data_struct()
    grand_range = set(chain(*streams))
    counters = list(map(ultra_counter, streams))
    pairs = filter(lambda t: all(counters[x].get(t, 0) for x in (0,1)), grand_range)
    for k in sorted(pairs):
        print k, sum(c.get(k,0) for c in counters)

over_thought_process()