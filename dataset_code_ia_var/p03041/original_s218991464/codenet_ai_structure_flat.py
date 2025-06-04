n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])
s = input()
ans = s[:k-1] + s[k-1].lower() + s[k:]
print(ans)