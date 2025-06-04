import sys

n = int(input())
alpnum = [0]*26
alpnumtmp = [0]*26
tmp = input()
for j in range(len(tmp)):
    alpnum[ord(tmp[j])-ord("a")] += 1
for i in range(1, n):
    tmp = input()
    for j in range(26):
        alpnumtmp[j] = 0
    for j in range(len(tmp)):
        alpnumtmp[ord(tmp[j])-ord("a")] += 1
    for j in range(26):
        alpnum[j] = min(alpnum[j], alpnumtmp[j])
ans = ""
for i in range(26):
    for j in range(alpnum[i]):
        ans += chr(97+i)
print(ans)