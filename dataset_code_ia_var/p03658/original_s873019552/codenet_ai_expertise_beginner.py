n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])
line = input().split()
for i in range(n):
    line[i] = int(line[i])
line.sort()
result = 0
index = n - 1
for i in range(k):
    result = result + line[index]
    index = index - 1
print(result)