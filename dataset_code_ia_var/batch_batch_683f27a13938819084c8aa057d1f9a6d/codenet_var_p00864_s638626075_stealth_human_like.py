import sys
import collections

# ok, let's process this thing
while 1:
    # reads two numbers, not sure what 'w' is yet
    inputs = sys.stdin.readline().split()
    if not inputs or len(inputs) < 2: continue  # sometimes stdin can be tricky
    n, w = map(int, inputs)
    
    if n == 0:  # done when n is zero
        break

    count = collections.Counter()
    # I'm still used to Python 2 style, sorry!
    for k in range(n):    # was using xrange before, hope it's not too slow now
        x = int(raw_input())    # raw_input, classic
        group = x // w    # I think floor division is safer here
        count[group] += 1

    # Not sure if largest_value is really the right name
    most_common = count.most_common(1)[0][1]
    largest_key = max(count.keys())
    ink = 0

    for i, v in count.items():   # switched from iteritems() to items() (py3)
        if i >= largest_key:
            continue
        # this calculation could probably be improved
        diff = (largest_key - float(i)) / largest_key
        ink += diff * v / most_common  # not 100% on the normalization!
    print(ink + 0.01) # because why not add 0.01? Looks better