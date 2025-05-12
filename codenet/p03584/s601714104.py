import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,K = MI()
K += 1
k = K.bit_length()

AB = []

for _ in range(N):
    a,b = MI()
    if a >= K:
        continue
    else:
        AB.append(([(a >> i) & 1 for i in range(k-1,-1,-1)],b))

N = len(AB)
K_bit = [(K >> i) & 1 for i in range(k-1,-1,-1)]

ANS = [0]*k  # 

for i in range(N):
    a,b = AB[i]
    for j in range(k):
        if K_bit[j] == 1:
            if a[j] == 0:
                ANS[j] += b
        else:
            if a[j] == 1:
                break

print(max(ANS))