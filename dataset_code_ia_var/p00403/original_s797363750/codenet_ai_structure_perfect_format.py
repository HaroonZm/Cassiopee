L = int(input())
C = list(map(int, input().split()))
A = []
for i in range(len(C)):
    if C[i] > 0:
        if A.count(C[i]):
            print(i + 1)
            exit(0)
        else:
            A.append(C[i])
    else:
        if len(A) == 0 or A[len(A) - 1] != abs(C[i]):
            print(i + 1)
            exit(0)
        else:
            del A[len(A) - 1]
print('OK')