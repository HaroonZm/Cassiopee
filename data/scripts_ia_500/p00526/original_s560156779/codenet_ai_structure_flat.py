N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    if (i & 1) == 1:
        A[i] ^= 1
B = []
prev = A[0]
cnt = 0
for i in range(N):
    if A[i] != prev:
        B.append(cnt)
        cnt = 1
    else:
        cnt += 1
    prev = A[i]
B.append(cnt)
if len(B) == 1:
    print(B[0])
elif len(B) == 2:
    print(B[0] + B[1])
else:
    max_sum = B[0] + B[1] + B[2]
    for i in range(1, len(B) - 2 + 1):
        s = B[i] + B[i+1] + B[i+2]
        if s > max_sum:
            max_sum = s
    print(max_sum)