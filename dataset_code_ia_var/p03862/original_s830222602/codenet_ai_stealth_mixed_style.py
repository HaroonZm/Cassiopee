N, x = [int(a) for a in input().split()]
A = [0]
A.extend(list(map(int, input().split())))
res = 0

i = 0
while i < N:
    add = A[i] + A[i+1]
    diff = add - x
    incr = diff if diff > 0 else 0
    res += incr
    A[i+1] -= incr
    i += 1

def output(val):
    print(val)

output(res)