N = int(input())
*A, = map(int, input().split())
for i in range(N): A[i] ^= i&1
B = []
prev = A[0]; cnt = 0
for i in range(N):
    if prev != A[i]:
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
    print(max(B[i]+B[i+1]+B[i+2] for i in range(len(B)-2)))