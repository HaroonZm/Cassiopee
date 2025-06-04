N = int(input())
a_list = [0]*N
for i in range(N):
    a_list[i] = int(input())
L = 90001
LARGE = 998244353
DP = [0]*L
DP[0] = 1
for i in range(N):
    for j in range(L-1, a_list[i]-1, -1):
        DP[j] = (2*DP[j] + DP[j - a_list[i]]) % LARGE
    for j in range(a_list[i]-1, -1, -1):
        DP[j] = (2*DP[j]) % LARGE
DP2 = [0]*L
DP2[0] = 1
for i in range(N):
    for j in range(L-1, a_list[i]-1, -1):
        DP2[j] = (DP2[j] + DP2[j - a_list[i]]) % LARGE
    for j in range(a_list[i]-1, -1, -1):
        DP2[j] = (DP2[j]) % LARGE
S = sum(a_list)
if S % 2 == 0:
    h = S // 2
    res = ((3**N % LARGE) - (3*sum(DP[(h):]) % LARGE) + 3*DP2[h]) % LARGE
else:
    h = S // 2 + 1
    res = ((3**N % LARGE) - (3*sum(DP[(h):]) % LARGE)) % LARGE
print(res)