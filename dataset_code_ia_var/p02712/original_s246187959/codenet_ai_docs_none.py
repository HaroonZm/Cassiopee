a = int(input())
b = []
for i in range(a+1):
    if i % 3 == 0 and i % 5 == 0:
        continue
    if i % 3 == 0:
        continue
    if i % 5 == 0:
        continue
    b.append(i)
print(sum(b))