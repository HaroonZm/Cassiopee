n = input()
a = raw_input().split()
a = [int(x) for x in a]

result = []
s = 1
count = 0

while len(a) != 0:
    temp = []
    for i in range(0, len(a)):
        if a[i] % 2 == 0 and a[i] != 0:
            temp.append(a[i] // 2)
    count = count + len(temp)
    a = []
    a.extend(temp)

print count