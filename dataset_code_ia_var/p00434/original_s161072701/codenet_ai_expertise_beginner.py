n = []
for i in range(30):
    n.append(i+1)

for i in range(28):
    x = int(input())
    if x in n:
        n.remove(x)

for i in n:
    print(i)