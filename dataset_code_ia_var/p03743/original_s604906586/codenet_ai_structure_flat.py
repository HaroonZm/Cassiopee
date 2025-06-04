import sys
readline = sys.stdin.readline

N_D = readline().split()
N = int(N_D[0])
D = int(N_D[1])
A = list(map(int, readline().split()))
A.append(0)

reach = [None]*(N+2)
reach[-1] = D
i = 0
while i < N+1:
    r = reach[i-1]
    a = A[i]
    reach[i] = min(r, abs(r-a))
    i += 1

putter = [0]*(N+2)
i = N
while i >= 0:
    p = putter[i+1]
    a = A[i]
    if 2*p+1 >= a:
        p += a
    putter[i] = p
    i -= 1

res = ['NO']*N
i = 0
while i < N:
    if reach[i-1] > putter[i+1]:
        res[i] = 'YES'
    i += 1

Q = int(readline())
query_indices = readline().split()
output = []
i = 0
while i < len(query_indices):
    idx = int(query_indices[i])-1
    output.append(res[idx])
    i += 1
print('\n'.join(output))