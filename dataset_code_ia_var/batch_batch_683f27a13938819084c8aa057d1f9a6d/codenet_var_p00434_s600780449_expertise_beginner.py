n = []
for i in range(28):
    num = int(input())
    n.append(num)

for j in range(1, 31):
    if j not in n:
        print(j)