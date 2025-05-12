"""
Nは10**5以下。O(N)なら通る
"""

N = int(input())
A = []
B = []
for i in range(N):
    s = list(map(int, input().split()))
    A.append(s[0])
    B.append(s[1])

count = 0
for i in reversed(range(N)):
    if (count + A[i]) % B[i] == 0:
        continue
    else:
        s = B[i] - (count + A[i]) % B[i]
        count += s

print(count)