from collections import deque
A = deque()
n = int(input())
for i in range(n):
    tmp = input().split()
#    print(tmp,A)
    if tmp[0] == "0" and tmp[1] == "0":
        A.appendleft(tmp[2])
    elif tmp[0] == "0" and tmp[1] == "1":
        A.append(tmp[2])
    elif tmp[0] == "1":
        print(A[int(tmp[1])])
    elif tmp[1] == "0":
        A.popleft()
    else:
        A.pop()