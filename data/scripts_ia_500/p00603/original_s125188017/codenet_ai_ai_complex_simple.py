import sys
from itertools import cycle, islice, chain

def complex_slice(seq, size):
    it = iter(seq)
    while True:
        chunk = list(islice(it, size))
        if not chunk:
            break
        yield chunk

def interleave_chunks(a, b, sz):
    a_chunks = list(complex_slice(a, sz))
    b_chunks = list(complex_slice(b, sz))
    # We interleave chunks but always picking from a then b alternatively
    result = []
    a_iter = iter(a_chunks)
    b_iter = iter(b_chunks)
    while True:
        try:
            result.extend(next(a_iter))
        except StopIteration:
            try:
                result.extend(next(b_iter))
            except StopIteration:
                break
            else:
                continue
        try:
            result.extend(next(b_iter))
        except StopIteration:
            continue
    return result

for line in iter(sys.stdin.readline, ''):
    if not line.strip():
        break
    try:
        n, r = map(int, line.split())
        cset = list(map(int, sys.stdin.readline().split()))
    except:
        break
    I = list(range(n))
    for c in cset:
        A, B = I[n//2:], I[:n//2]
        I = interleave_chunks(A, B, c)
    print(I[-1])