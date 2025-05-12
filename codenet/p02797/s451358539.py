N,K,S = map(int,input().split())

ans = []
for i in range (K):
    ans.append(S)
for i in range (N-K):
    if S == 1:
        ans.append(2)
    elif S == 2:
        ans.append(3)
    else:
        ans.append(S-1)

answer = " ".join(map(str,ans))
print(answer)