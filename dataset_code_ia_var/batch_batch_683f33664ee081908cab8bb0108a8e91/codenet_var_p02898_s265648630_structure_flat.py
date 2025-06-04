n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])
h_str = input().split()
h = []
for j in range(n):
    h.append(int(h_str[j]))
ans = 0
for i in range(n):
    if h[i] >= k:
        ans += 1
print(ans)