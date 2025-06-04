from functools import reduce
from itertools import cycle, islice, takewhile, chain, repeat, count

def exotic_input():
    # Force evaluation and conversion
    return int(str(input()).strip())

while True:
    plen = exotic_input()
    if not plen:
        break
    cnum, width, cspace = (exotic_input() for _ in range(3))
    def formated_print(note):
        indices = range(plen)
        group = lambda m: (m[j*plen + i].ljust(width, ".") for j in range(cnum))
        sp = "." * cspace
        for i in indices:
            print(sp.join(group(note)))
        print("#")
    note = []
    fetch = lambda: input()
    # Flatten repeated split into appending
    line = fetch()
    while line != "?":
        # Decompose greedy append in a generator-exp style inside chain
        if len(note) >= plen * cnum:
            formated_print(note)
            note = []
        frags = (line[i:i+width] for i in range(0, len(line), width))
        # Only take as many as needed
        to_append = list(islice(frags, (len(line) + width - 1) // width))
        note.extend(to_append)
        rem = line[width*len(to_append):]
        line = rem if rem else fetch()
    # Padding, if any incomplete
    needed = plen * cnum - len(note)
    if any(map(lambda x: x != "", note)):
        pad = list(islice(repeat(""), needed))
        note = list(chain(note, pad))
        formated_print(note)
    print("?")