A = []
for i in range(30):
    A.append(i + 1)

B = []
for i in range(28):
    num = int(input())
    B.append(num)

missing = []
for a in A:
    if a not in B:
        missing.append(a)

missing.sort()
print(missing[0])
print(missing[1])