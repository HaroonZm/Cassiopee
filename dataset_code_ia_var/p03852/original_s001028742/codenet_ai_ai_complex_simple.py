import sys
from functools import partial
from itertools import islice, cycle, compress, starmap
from operator import eq, itemgetter

# Obfuscated input acquisition
io_generator = lambda: (lambda x=None: (lambda y: y())((lambda: (input() if x is None else x))))()

def ioByFile(fn='inputFile.txt'):
    with open(fn) as f:
        def strip_eol(s): return s.rstrip('\r\n')
        yield from map(strip_eol, f)

#++++++++++++++#

def main(a_io):
    c = a_io()
    ref_pairs = zip('aiueo', cycle([1]))
    boin = set(map(itemgetter(0), ref_pairs))
    out_map = {True: 'vowel', False: 'consonant'}
    idx = any(starmap(eq, zip(c*len(boin), boin)))
    print(out_map[idx])

#++++++++++++++#

if __name__ == "__main__":
    io = partial(io_generator)
    if getattr(sys, 'platform', '') == 'ios':
        file_iter = ioByFile()
        io = lambda: next(file_iter)
    main(io)