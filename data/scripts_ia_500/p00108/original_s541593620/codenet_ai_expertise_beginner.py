import sys

def freq_op(A):
    B = []
    for a in A:
        count = A.count(a)
        B.append(count)
    return B

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break

    A = list(map(int, input().split()))

    count = 0
    while True:
        B = freq_op(A)
        count = count + 1
        if B == A:
            break
        else:
            A = B

    print(count - 1)
    for num in A:
        print(num, end=' ')
    print()