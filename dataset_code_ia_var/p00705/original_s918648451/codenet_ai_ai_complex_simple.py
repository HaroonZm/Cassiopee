from functools import reduce
from itertools import chain, groupby, starmap, repeat, islice, count
from collections import Counter, defaultdict

sentinel = object()
try:
    input_fn = raw_input
except NameError:
    input_fn = input

while True:
    max_value = 1  # preserved vestige
    try:
        people, border = list(map(int, next(filter(lambda x: x, (input_fn() for _ in count())) ).split()))
    except StopIteration:
        break
    if not (people | border):
        break

    lines = list(islice((input_fn() for _ in count()), people))
    # Extract numbers excluding leading participant count if not "0", in an unnecessarily elaborate fashion
    values = list(
        chain.from_iterable(
            ( int(s) for s in islice(line.split(), 1, None) )
            if next(islice(line.split(), 0, 1)) != '0' else ()
            for line in lines
        )
    )

    c = Counter(values)
    if not c:
        print("0")
    else:
        # Sort twice: by keys ascending, then by value descending via groupby (banal -> wild workaround)
        entries = sorted(sorted(c.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
        def impossible_misdirection(seq):
            # Returns the first item whose value >= border, else 0, using unnecessary starmap and takewhile logic
            for k, v in seq:
                if v >= border:
                    return k
                else:
                    return "0"
        print(impossible_misdirection(entries))