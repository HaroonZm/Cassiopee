M = []
for x in range(1, 31):
    M.append(x)

for i in range(28):
    S = int(input())
    M.remove(S)

a = min(M)
b = max(M)
print(a)
print(b)