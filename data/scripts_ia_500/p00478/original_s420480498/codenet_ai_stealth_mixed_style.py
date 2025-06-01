m = input()
n = int(input())
x = []
for i in range(n):
    line = input()
    x.append(line)

count = 0
i = 0
while i < n:
    x[i] = x[i] + x[i][:11]
    if m in x[i]:
        count += 1
    i += 1

print(count)