n = int(input())
_A = list(map(int, input().split()))
ans = 1000
A = [_A[0]]
B = []
for i in range(n-1):
    if _A[i] != _A[i+1]:
        A.append(_A[i+1])
flag = 0
if len(A) < 2:
    print(ans)
    exit()
for i in range(len(A)-1):
    if flag == 0 and A[i] < A[i+1]:
        flag = 1
        B.append(A[i])
    elif flag == 1 and A[i] > A[i+1]:
        flag = 0
        B.append(A[i])
if (A[-1] > A[-2] and flag == 1) or (A[-1] < A[-2] and flag == 0):
    B.append(A[-1])
if len(B) < 2:
    print(ans)
    exit()
if B[-1] < B[-2]:
    B.pop(-1)
stock = 0
for i, b in enumerate(B):
    if i % 2 == 0:
        stock = ans // b
        ans = ans % b
    else:
        ans = ans + stock * b
        stock = 0
print(ans)