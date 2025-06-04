m = input()
n = int(input())
x = []
for i in range(n):
    x.append(input())
c = 0
for i in range(n):
    x[i] = x[i] + x[i][:11]
    if m in x[i]:
        c += 1
print(c)