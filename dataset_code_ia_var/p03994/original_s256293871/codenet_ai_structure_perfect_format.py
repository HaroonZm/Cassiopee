alpha2num = lambda c: ord(c) - ord('a') + 1
num2alpha = lambda c: chr(c + ord('a') - 1)
S = list(map(alpha2num, input()))
K = int(input())
for i in range(len(S)):
    if K <= 0:
        break
    if S[i] == 1:
        continue
    elif 27 - S[i] <= K:
        K -= (27 - S[i])
        S[i] = 1
if K >= 1:
    S[-1] = (S[-1] + K) % 26
    if S[-1] == 0:
        S[-1] = 26
S = list(map(num2alpha, S))
print(*S, sep='')