q = int(input())
query = []
A = []
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        A.append(query[1])
    elif query[0] == 1:
        print(A[query[1]])
    else:
        A.pop(-1)