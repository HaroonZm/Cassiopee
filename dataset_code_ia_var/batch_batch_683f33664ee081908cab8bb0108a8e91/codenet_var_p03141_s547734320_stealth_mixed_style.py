from numpy import array, zeros, sort, sum as np_sum

def proc():
    N = int(input())
    A = []
    B = zeros(N, dtype=int)
    for j in range(N):
        vals = input().split()
        if j % 2 == 0:
            A.append(int(vals[0]))
            B[j] = int(vals[1])
        else:
            A += [int(vals[0])]
            B[j] = int(vals[1])

    a = array(A)
    c = []
    idx = 0
    while idx < N:
        c.append(a[idx] + B[idx])
        idx += 1

    csorted = list(sort(c))
    csorted = csorted[::-1]
    tot = np_sum(B)
    result = 0
    for k in range(N):
        if not k % 2:
            result += int(csorted[k])
    answer = result - tot
    print(answer)

proc()