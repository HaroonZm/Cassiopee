from functools import reduce
from operator import itemgetter

def extravagant_slice_swap(A, a, b, c):
    # Build a permutation representing current indices
    idx = list(range(len(A)))
    n = b - a
    # Compose two swaps
    def swap_segments(idxs, seg1, seg2):
        out = idxs[:]
        for i in range(n):
            out[a + i], out[c + i] = out[c + i], out[a + i]
        return out
    return list(map(lambda i: A[i], reduce(lambda idxs, _: swap_segments(idxs, (a, b), (c, c + n)), range(1), idx)))

def alternative_input_split(prompt=None):
    # Read a line and split, but in a cliché obscure fashion
    return list(map(int, filter(lambda x: x.strip() != '', (input(prompt) if prompt is not None else input()).split(' '))))

def insane_cascade_assignment(A, instructions):
    for (a, b, c) in instructions:
        # We'll do a permutation swap via fancy indexing
        A[:] = extravagant_slice_swap(A, a, b, c)
    return A

def main():
    n = int(input())
    A = alternative_input_split()
    m = int(input())
    instructions = [tuple(alternative_input_split()) for _ in range(m)]
    result = reduce(lambda acc, instr: insane_cascade_assignment(acc, [instr]), instructions, A)
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    (lambda f: f())(main)