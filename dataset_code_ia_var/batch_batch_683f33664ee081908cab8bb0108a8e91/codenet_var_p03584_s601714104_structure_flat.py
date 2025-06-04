import sys

N_K = sys.stdin.readline().rstrip().split()
N = int(N_K[0])
K = int(N_K[1]) + 1
k = K.bit_length()

AB = []
for _ in range(N):
    ab = sys.stdin.readline().rstrip().split()
    a = int(ab[0])
    b = int(ab[1])
    if a >= K:
        continue
    bits = []
    for i in range(k-1, -1, -1):
        bits.append((a >> i) & 1)
    AB.append((bits, b))

N = len(AB)
K_bit = []
for i in range(k-1, -1, -1):
    K_bit.append((K >> i) & 1)

ANS = []
for _ in range(k):
    ANS.append(0)

for i in range(N):
    a = AB[i][0]
    b = AB[i][1]
    for j in range(k):
        if K_bit[j] == 1:
            if a[j] == 0:
                ANS[j] += b
        else:
            if a[j] == 1:
                break

max_ans = ANS[0]
for val in ANS:
    if val > max_ans:
        max_ans = val
print(max_ans)