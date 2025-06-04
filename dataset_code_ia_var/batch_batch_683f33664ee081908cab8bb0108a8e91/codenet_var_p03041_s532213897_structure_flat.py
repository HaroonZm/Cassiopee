n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])
s = list(input())
s[k-1] = s[k-1].lower()
result = ''
for ch in s:
    result += ch
print(result)