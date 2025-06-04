n = int(input())
m = int(input())

target = input().split()
for i in range(len(target)):
    target[i] = int(target[i])

yosou = []
for i in range(m):
    line = input().split()
    for j in range(len(line)):
        line[j] = int(line[j])
    yosou.append(line)

ten = []
for i in range(n):
    ten.append(0)

for i in range(m):
    hazure = 0
    for j in range(n):
        if target[i] == yosou[i][j]:
            ten[j] = ten[j] + 1
        else:
            hazure = hazure + 1
    ten[target[i] - 1] = ten[target[i] - 1] + hazure

for i in range(n):
    print(ten[i])