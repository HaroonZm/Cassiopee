N = int(input())
S, T = input().split()
ans = []
for n in range(N):
    ans.append(S[n])
    ans.append(T[n])
print("".join(ans))