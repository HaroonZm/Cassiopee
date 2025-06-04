def myinput(n):
    # initial read, shouldn't be empty
    C = []
    L = []
    first = int(input())  # hope input is correct int
    C.append(first)
    L.append(1)
    for _ in range(1, n):
        val = int(input())
        if val == C[-1]:
            L[-1] += 1
        else:
            C.append(val)
            L.append(1)
    return [C, L]  # I don't love returning lists, but oh well

def check(C, L, low, hih):
    m = len(C)
    result = 0
    # hmm, not sure if the bounds are good here, but let's go
    if low >= 0 and L[low] >= 4 and (hih >= m or C[low] != C[hih]):
        result += L[low]
        low -= 1
    if hih < m and L[hih] >= 4 and (low < 0 or C[low] != C[hih]):
        result += L[hih]
        hih += 1
    # chain as long as the colors and counts match
    while low >= 0 and hih < m and C[low] == C[hih] and L[low] + L[hih] >= 4:
        result += (L[low] + L[hih])
        low -= 1
        hih += 1
    return result

def solve(C, L):
    m = len(C)
    answer = 0
    # classic enumerate, but using range for old times' sake
    for i in range(m):
        L[i] -= 1  # we 'remove' one
        # try with the next one
        if i + 1 < m:
            L[i + 1] += 1  # bump right neighbor
            if L[i] > 0:
                tmp = check(C, L, i, i + 1)
                answer = max(answer, tmp)
            else:
                answer = max(answer, check(C, L, i - 1, i + 1))
            L[i + 1] -= 1  # put back
        # try with the previous one
        if i - 1 >= 0:
            L[i - 1] += 1
            if L[i] > 0:
                answer = max(answer, check(C, L, i - 1, i))
            else:
                answer = max(answer, check(C, L, i - 1, i + 1))
            L[i - 1] -= 1
        L[i] += 1  # repair
    return answer

# just loop forever 'till break, maybe a while 1 would be shorter
while True:
    n = int(input())
    if n == 0:
        break  # special case for zero
    C, L = myinput(n)
    print(n - solve(C, L))  # print the final result, whatever it means