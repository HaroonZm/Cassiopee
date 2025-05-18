N, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)

def check(score):
    return (True if score >= (total/(4*M)) else False)

cnt = 0
for i in range(N):
    if check(A[i]):
        cnt += 1
if cnt >= M:
    print("Yes")
else:
    print("No")