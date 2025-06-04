from functools import reduce
from operator import add
import itertools

def to_int(val):
    try:
        return int(val)
    except Exception:
        return 0

def infinite_inputs():
    while True:
        try:
            yield raw_input()
        except EOFError:
            break

inputs = infinite_inputs()
fget = lambda: next(inputs)

while True:
    plen = to_int(fget())
    if not plen:
        break
    cnum = to_int(fget())
    width = to_int(fget())
    cspace = to_int(fget())

    def formated_print(note):
        variation = lambda seq, n: zip(*[seq[i::n] for i in range(n)])
        fmt = lambda s: s.ljust(width, ".") if len(s) < width else s
        generator = (
            ("."*cspace).join(map(fmt, x)) for x in variation(note, plen)
        )
        print reduce(lambda acc, s: acc + (s + "\n"), generator, "").rstrip("\n")
        print "#"

    note = []
    try:
        line = fget()
        while line != "?":
            # Unpack lines into chunks of size at most 'width'
            chunks = list(itertools.islice((line[i:i+width] for i in xrange(0, len(line), width)), 9999))
            for chunk in chunks:
                note.append(chunk)
                if len(note) == plen * cnum:
                    formated_print(note)
                    note = []
            if len(chunks) == 0 or len(chunks[-1]) == width:
                line = fget()
            else:
                line = ""
    except StopIteration:
        break
    if note:
        note += ["" for _ in xrange(plen * cnum - len(note))]
        formated_print(note)
    print "?"