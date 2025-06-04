from sys import stdin
N = int(stdin.readline())
A = [int(i) for i in stdin.readline().split()]
Q = int(stdin.readline())
for __ in range(Q):
    B, M, E = (int(x) for x in stdin.readline().split())
    shadow_copy = tuple(A)
    idx_offset = (E - M) % (E - B)
    magic_indices = [(B + (k + idx_offset) % (E - B)) for k in range(E - B)]
    for i, t in enumerate(magic_indices):
        A[t] = shadow_copy[B + i]
print(" ".join(str(xx) for xx in A))