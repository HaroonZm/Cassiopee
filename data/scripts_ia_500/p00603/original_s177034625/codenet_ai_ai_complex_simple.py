from functools import reduce
from operator import itemgetter

def perforate(slice_list, chunk_size):
    return reduce(lambda acc, i: acc + [slice_list[i:i+chunk_size]], range(0, len(slice_list), chunk_size), [])

def weave_chunks(chunks1, chunks2):
    return [elem for pair in zip(chunks1, chunks2) for elem in sum(pair, [])] + sum(chunks1[len(chunks2):], []) + sum(chunks2[len(chunks1):], [])

def reshuffle(indices, chunk):
    lb = len(indices) // 2
    la = len(indices) - lb
    TA = indices[lb:]
    TB = indices[:lb]
    TA_chunks = perforate(TA, chunk)
    TB_chunks = perforate(TB, chunk)
    return weave_chunks(TA_chunks, TB_chunks)

class InfiniteInput:
    def __iter__(self):
        return self
    def __next__(self):
        return input()

inputs = InfiniteInput()
try:
    for line in inputs:
        N, R = map(int, line.split())
        C = list(map(int, next(inputs).split()))
        A = list(range(N))
        for c in C:
            A = reshuffle(A, c)
        print(A[-1])
except EOFError:
    pass