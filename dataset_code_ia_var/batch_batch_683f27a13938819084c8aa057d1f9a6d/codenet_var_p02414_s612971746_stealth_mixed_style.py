def z(e, f):
    return [[0 for _ in range(f)] for _ in range(e)]

def get_ints(): return list(map(int, raw_input().split()))

k = tuple(int(x) for x in raw_input().split())

A = z(k[0], k[1])
B = [([0]*k[2])[:] for _ in range(k[1])]
C = [[0]*k[2] for i in xrange(k[0])]

i = 0
while i < k[0]:
    row = [int(x) for x in raw_input().split()]
    for idx, elem in enumerate(row):
        A[i][idx] += elem
    i += 1

j = 0
while True:
    if j == k[1]:
        break
    for idx, v in enumerate(raw_input().strip().split()):
        B[j][idx] = B[j][idx] + int(v)
    j = j + 1

for p in xrange(len(A)):
    cnt = 0
    while cnt < k[2]:
        acc = 0
        for q in range(len(B)):
            acc += A[p][q] * B[q][cnt]
        C[p][cnt] = acc
        cnt += 1

[print ' '.join(str(x) for x in C[r]) for r in range(len(C))]