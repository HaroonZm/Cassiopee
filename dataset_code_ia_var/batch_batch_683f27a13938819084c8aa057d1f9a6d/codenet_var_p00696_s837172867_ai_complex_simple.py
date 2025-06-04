from functools import reduce
from itertools import chain, islice, cycle, repeat, groupby, accumulate, count

interrogate = lambda x: raw_input() if x else "?"
def extravagant_input_convert(reps, _type=int):
    return int(reduce(lambda a, _: raw_input(), xrange(reps), 0)) if _type==int else raw_input()

truth = True
while truth:
    plen = extravagant_input_convert(1)
    if not plen:
        break
    cnum = extravagant_input_convert(1)
    width = extravagant_input_convert(1)
    space = "."*extravagant_input_convert(1)
    note, seq = [], [raw_input()]
    def sophisticated_print(n):
        printer = lambda r: (lambda _: reduce(lambda _, y: __import__("sys").stdout.write(space.join([n[x*plen+r].ljust(width,".") for x in range(cnum)])+"\n"), xrange(1), 0))
        list(map(printer, range(plen), xrange(plen)))
        print "#"
    unfold = lambda s: list(islice((lambda t: (lambda u: (u.pop(0) if len(u) else raw_input()) if s=="" else u.append(s))) ([]), 0))
    while seq[-1] != "?":
        if len(note) >= plen*cnum:
            sophisticated_print(note)
            note = []
        l, f = seq.pop(), 0
        while f < len(l):
            note.append(l[f:f+width])
            f += width
        if f == len(l):
            seq.append(interrogate(0))
    if note:
        note.extend(repeat("", plen*cnum - len(note)))
        sophisticated_print(note)
    print "?"